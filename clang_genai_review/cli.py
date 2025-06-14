import argparse
import os
from clang_genai_review.fetch_pr_patch import fetch_patch_from_pr
from clang_genai_review.genai_review import run_review_from_patch

def main():
    parser = argparse.ArgumentParser(description="GenAI Code Review for LLVM Pull Requests")
    parser.add_argument("--pr", type=int, help="LLVM PR number to review")
    parser.add_argument("--show", action="store_true", help="Show previously saved review if available")
    args = parser.parse_args()

    pr_number = args.pr
    review_file = f"clang_genai_review/reviews/pr_{pr_number}.md"

    if args.show:
        if os.path.exists(review_file):
            with open(review_file, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"[❌] No saved review found for PR #{pr_number}")
        return

    if not pr_number:
        print("[❌] Please provide a PR number with --pr")
        return

    print(f"[🔍] Fetching patch for PR #{pr_number}...")
    patch = fetch_patch_from_pr(pr_number)

    print("[🧠] Running GenAI review...")
    os.makedirs("clang_genai_review/reviews", exist_ok=True)
    run_review_from_patch(patch, save_markdown=True, output_path=review_file)

    print(f"[✅] Review saved to {review_file}")
