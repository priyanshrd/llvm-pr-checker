import os
import sys
import requests
from groq import Groq
from dotenv import load_dotenv
from clang_genai_review.parse_diff import parse_patch_string

load_dotenv()

# === Setup Groq client ===
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY. Please set it in your .env file or environment.")

client = Groq(api_key=GROQ_API_KEY)


def groq_review(filename, line_data):
    full_text = "\n".join(line_data[filename])
    prompt = f"""
You are a code reviewer for the LLVM project. Given the following modified lines in the file `{filename}`, 
identify any issues with code style, naming conventions, or clarity, according to the LLVM coding standards.

Modified lines:```{full_text}```

Provide suggestions, and corrected code if necessary.
"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a code reviewer for the LLVM project."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def save_combined_review_md(all_reviews, output_file="llvm_review.md"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Combined LLVM Code Review\n\n")
        for filename, review_text in all_reviews.items():
            f.write(f"## `{filename}`\n\n")
            f.write(review_text.strip() + "\n\n---\n\n")
    print(f"[✅] Combined review saved to {output_file}")


def extract_added_lines_per_file(patch_text, filenames):
    line_data = {filename: [] for filename in filenames}
    current_file = None
    collecting = False

    for line in patch_text.splitlines():
        if line.startswith("+++ b/"):
            current_file = line[6:]
            collecting = current_file in filenames
            continue

        if line.startswith("diff --git") or line.startswith("---"):
            collecting = False

        if collecting and line.startswith("+") and not line.startswith("+++"):
            line_data[current_file].append(line[1:])

    return line_data


def run_review_from_patch(patch_text, save_markdown=False, output_path="llvm_review.md"):
    parsed = parse_patch_string(patch_text)
    combined_reviews = {}

    for file_diff in parsed:
        filename = file_diff.get("filename")
        modified_lines = file_diff.get("lines", [])

        if not filename or not modified_lines:
            print(f"[⚠️] Skipping invalid diff entry: {file_diff}")
            continue

        print(f"[+] Found file: {filename}")
        print(f"[*] Modified lines: {modified_lines}")

        line_data = {filename: []}
        collecting = False
        for line in patch_text.splitlines():
            if f"+++ b/{filename}" in line:
                collecting = True
                continue
            if collecting:
                if line.startswith("diff --git") or line.startswith("---"):
                    collecting = False
                elif line.startswith("+") and not line.startswith("+++"):
                    line_data[filename].append(line[1:])

        print("[DEBUG] line_data:")
        for f, lines in line_data.items():
            print(f" - {f}: {len(lines)} lines")

        review = groq_review(filename, line_data)
        print(f"\n🔍 GenAI Review for {filename}\n{review}")
        combined_reviews[filename] = review

    if save_markdown:
        save_combined_review_md(combined_reviews, output_file=output_path)


def fetch_patch_from_pr(pr_number, repo="llvm/llvm-project"):
    url = f"https://patch-diff.githubusercontent.com/raw/{repo}/pull/{pr_number}.patch"
    print(f"[INFO] Fetching patch from GitHub PR #{pr_number}...")
    resp = requests.get(url)

    if resp.status_code != 200:
        raise Exception(f"[❌] Failed to fetch PR #{pr_number}. Status: {resp.status_code}")

    return resp.text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            pr_number = int(sys.argv[1])
            patch = fetch_patch_from_pr(pr_number)
        except ValueError:
            print("[❌] Invalid PR number. Usage: python genai_review.py [PR_NUMBER]")
            sys.exit(1)
    else:
        print("[INFO] Generating diff.patch from local git changes...")
        os.system("git diff origin/main...HEAD -U0 > diff.patch")
        with open("diff.patch", "r", encoding="utf-8") as f:
            patch = f.read()

    run_review_from_patch(patch, save_markdown=True)
