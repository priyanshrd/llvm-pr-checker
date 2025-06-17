# Combined LLVM Code Review

## `lldb/scripts/framework-header-fix.sh`

### 🧹 clang-format Output
```text
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:1:4: error: code should be clang-formatted [-Wclang-format-violations]
#!/bin/sh
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:1:7: error: code should be clang-formatted [-Wclang-format-violations]
#!/bin/sh
      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:1:8: error: code should be clang-formatted [-Wclang-format-violations]
#!/bin/sh
       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:2:2: error: code should be clang-formatted [-Wclang-format-violations]
# Usage: framework-header-fix.sh <source header dir> <LLDB Version>
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:2:8: error: code should be clang-formatted [-Wclang-format-violations]
# Usage: framework-header-fix.sh <source header dir> <LLDB Version>
       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:2:19: error: code should be clang-formatted [-Wclang-format-violations]
# Usage: framework-header-fix.sh <source header dir> <LLDB Version>
                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:2:20: error: code should be clang-formatted [-Wclang-format-violations]
# Usage: framework-header-fix.sh <source header dir> <LLDB Version>
                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:2:26: error: code should be clang-formatted [-Wclang-format-violations]
# Usage: framework-header-fix.sh <source header dir> <LLDB Version>
                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:2:27: error: code should be clang-formatted [-Wclang-format-violations]
# Usage: framework-header-fix.sh <source header dir> <LLDB Version>
                          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:2:35: error: code should be clang-formatted [-Wclang-format-violations]
# Usage: framework-header-fix.sh <source header dir> <LLDB Version>
                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh:2:55: error: code should be clang-formatted [-Wclang-format-violations]
# Usage: framework-header-fix.sh <source header dir> <LLDB Version>
                                                      ^
```
### 🧪 clang-tidy Output
```text
error: unable to handle compilation, expected exactly one compiler job in '' [clang-diagnostic-error]
warning: C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh: 'linker' input unused [clang-diagnostic-unused-command-line-argument]Error while processing C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\framework-header-fix.sh.
Found compiler error(s).
```
### 🤖 GenAI Review
```text
🤖 **GenAI Review for `lldb/scripts/framework-header-fix.sh`**

```diff
lldb/scripts/framework-header-fix.sh
```

🧠 **Feedback**:
The above changes appear structurally sound. Consider reviewing:
- Code readability and formatting
- Potential edge case handling
- Naming conventions and code reuse
```

---

## `lldb/scripts/version-header-fix.py`

### 🧹 clang-format Output
```text
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:1:4: error: code should be clang-formatted [-Wclang-format-violations]
#!/usr/bin/env python3
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:1:7: error: code should be clang-formatted [-Wclang-format-violations]
#!/usr/bin/env python3
      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:1:8: error: code should be clang-formatted [-Wclang-format-violations]
#!/usr/bin/env python3
       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:1:11: error: code should be clang-formatted [-Wclang-format-violations]
#!/usr/bin/env python3
          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:1:12: error: code should be clang-formatted [-Wclang-format-violations]
#!/usr/bin/env python3
           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:2:3: error: code should be clang-formatted [-Wclang-format-violations]
"""
  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:2:4: error: code should be clang-formatted [-Wclang-format-violations]
"""
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:6: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:13: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
            ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:14: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:16: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:17: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:22: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:23: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:32: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:38: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:39: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:41: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:42: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:48: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:49: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:58: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                                                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:3:115: error: code should be clang-formatted [-Wclang-format-violations]
Usage: <path/to/input-header.h> <path/to/output-header.h> LLDB_MAJOR_VERSION LLDB_MINOR_VERSION LLDB_PATCH_VERSION
                                                                                                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:5:52: error: code should be clang-formatted [-Wclang-format-violations]
This script uncomments and populates the versioning information in lldb-defines.h
                                                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:5:72: error: code should be clang-formatted [-Wclang-format-violations]
This script uncomments and populates the versioning information in lldb-defines.h
                                                                       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:5:73: error: code should be clang-formatted [-Wclang-format-violations]
This script uncomments and populates the versioning information in lldb-defines.h
                                                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:5:82: error: code should be clang-formatted [-Wclang-format-violations]
This script uncomments and populates the versioning information in lldb-defines.h
                                                                                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:6:3: error: code should be clang-formatted [-Wclang-format-violations]
"""
  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:6:4: error: code should be clang-formatted [-Wclang-format-violations]
"""
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:8:16: error: code should be clang-formatted [-Wclang-format-violations]
import argparse
               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:9:10: error: code should be clang-formatted [-Wclang-format-violations]
import os
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:10:10: error: code should be clang-formatted [-Wclang-format-violations]
import re
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:12:21: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_VERSION_REGEX = re.compile(r"//\s*#define LLDB_VERSION\s*$", re.M)
                    ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:12:34: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_VERSION_REGEX = re.compile(r"//\s*#define LLDB_VERSION\s*$", re.M)
                                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:12:72: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_VERSION_REGEX = re.compile(r"//\s*#define LLDB_VERSION\s*$", re.M)
                                                                       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:13:22: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_REVISION_REGEX = re.compile(r"//\s*#define LLDB_REVISION\s*$", re.M)
                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:13:35: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_REVISION_REGEX = re.compile(r"//\s*#define LLDB_REVISION\s*$", re.M)
                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:13:74: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_REVISION_REGEX = re.compile(r"//\s*#define LLDB_REVISION\s*$", re.M)
                                                                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:14:28: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_VERSION_STRING_REGEX = re.compile(r"//\s*#define LLDB_VERSION_STRING\s*$", re.M)
                           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:14:41: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_VERSION_STRING_REGEX = re.compile(r"//\s*#define LLDB_VERSION_STRING\s*$", re.M)
                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:14:86: error: code should be clang-formatted [-Wclang-format-violations]
LLDB_VERSION_STRING_REGEX = re.compile(r"//\s*#define LLDB_VERSION_STRING\s*$", re.M)
                                                                                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:17:4: error: code should be clang-formatted [-Wclang-format-violations]
def main():
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:17:11: error: code should be clang-formatted [-Wclang-format-violations]
def main():
          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:17:12: error: code should be clang-formatted [-Wclang-format-violations]
def main():
           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:18:39: error: code should be clang-formatted [-Wclang-format-violations]
    parser = argparse.ArgumentParser()
                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:19:38: error: code should be clang-formatted [-Wclang-format-violations]
    parser.add_argument("input_path")
                                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:20:39: error: code should be clang-formatted [-Wclang-format-violations]
    parser.add_argument("output_path")
                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:21:46: error: code should be clang-formatted [-Wclang-format-violations]
    parser.add_argument("lldb_version_major")
                                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:22:46: error: code should be clang-formatted [-Wclang-format-violations]
    parser.add_argument("lldb_version_minor")
                                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:23:46: error: code should be clang-formatted [-Wclang-format-violations]
    parser.add_argument("lldb_version_patch")
                                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:24:31: error: code should be clang-formatted [-Wclang-format-violations]
    args = parser.parse_args()
                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:25:17: error: code should be clang-formatted [-Wclang-format-violations]
    input_path = str(args.input_path)
                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:25:38: error: code should be clang-formatted [-Wclang-format-violations]
    input_path = str(args.input_path)
                                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:26:18: error: code should be clang-formatted [-Wclang-format-violations]
    output_path = str(args.output_path)
                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:26:40: error: code should be clang-formatted [-Wclang-format-violations]
    output_path = str(args.output_path)
                                       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:27:25: error: code should be clang-formatted [-Wclang-format-violations]
    lldb_version_major = args.lldb_version_major
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:27:49: error: code should be clang-formatted [-Wclang-format-violations]
    lldb_version_major = args.lldb_version_major
                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:28:25: error: code should be clang-formatted [-Wclang-format-violations]
    lldb_version_minor = args.lldb_version_minor
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:28:49: error: code should be clang-formatted [-Wclang-format-violations]
    lldb_version_minor = args.lldb_version_minor
                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:29:25: error: code should be clang-formatted [-Wclang-format-violations]
    lldb_version_patch = args.lldb_version_patch
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:29:49: error: code should be clang-formatted [-Wclang-format-violations]
    lldb_version_patch = args.lldb_version_patch
                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:31:45: error: code should be clang-formatted [-Wclang-format-violations]
    with open(input_path, "r") as input_file:
                                            ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:31:46: error: code should be clang-formatted [-Wclang-format-violations]
    with open(input_path, "r") as input_file:
                                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:32:39: error: code should be clang-formatted [-Wclang-format-violations]
        lines = input_file.readlines()
                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:33:22: error: code should be clang-formatted [-Wclang-format-violations]
        file_buffer = "".join(lines)
                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:33:37: error: code should be clang-formatted [-Wclang-format-violations]
        file_buffer = "".join(lines)
                                    ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:35:32: error: code should be clang-formatted [-Wclang-format-violations]
    with open(output_path, "w") as output_file:
                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:35:47: error: code should be clang-formatted [-Wclang-format-violations]
    with open(output_path, "w") as output_file:
                                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:35:48: error: code should be clang-formatted [-Wclang-format-violations]
    with open(output_path, "w") as output_file:
                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:36:10: error: code should be clang-formatted [-Wclang-format-violations]
        # For the defines in lldb-defines.h that define the major, minor and version string
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:36:34: error: code should be clang-formatted [-Wclang-format-violations]
        # For the defines in lldb-defines.h that define the major, minor and version string
                                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:36:35: error: code should be clang-formatted [-Wclang-format-violations]
        # For the defines in lldb-defines.h that define the major, minor and version string
                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:36:67: error: code should be clang-formatted [-Wclang-format-violations]
        # For the defines in lldb-defines.h that define the major, minor and version string
                                                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:36:92: error: code should be clang-formatted [-Wclang-format-violations]
        # For the defines in lldb-defines.h that define the major, minor and version string
                                                                                           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:37:10: error: code should be clang-formatted [-Wclang-format-violations]
        # uncomment each define and populate its value using the arguments passed in.
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:37:86: error: code should be clang-formatted [-Wclang-format-violations]
        # uncomment each define and populate its value using the arguments passed in.
                                                                                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:38:10: error: code should be clang-formatted [-Wclang-format-violations]
        # e.g. //#define LLDB_VERSION -> #define LLDB_VERSION <LLDB_MAJOR_VERSION>
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:38:18: error: code should be clang-formatted [-Wclang-format-violations]
        # e.g. //#define LLDB_VERSION -> #define LLDB_VERSION <LLDB_MAJOR_VERSION>
                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:38:83: error: code should be clang-formatted [-Wclang-format-violations]
        # e.g. //#define LLDB_VERSION -> #define LLDB_VERSION <LLDB_MAJOR_VERSION>
                                                                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:39:30: error: code should be clang-formatted [-Wclang-format-violations]
        file_buffer = re.sub(
                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:40:32: error: code should be clang-formatted [-Wclang-format-violations]
            LLDB_VERSION_REGEX,
                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:41:14: error: code should be clang-formatted [-Wclang-format-violations]
            r"#define LLDB_VERSION " + lldb_version_major,
             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:41:39: error: code should be clang-formatted [-Wclang-format-violations]
            r"#define LLDB_VERSION " + lldb_version_major,
                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:41:59: error: code should be clang-formatted [-Wclang-format-violations]
            r"#define LLDB_VERSION " + lldb_version_major,
                                                          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:42:25: error: code should be clang-formatted [-Wclang-format-violations]
            file_buffer,
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:43:10: error: code should be clang-formatted [-Wclang-format-violations]
        )
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:45:30: error: code should be clang-formatted [-Wclang-format-violations]
        file_buffer = re.sub(
                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:46:33: error: code should be clang-formatted [-Wclang-format-violations]
            LLDB_REVISION_REGEX,
                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:47:14: error: code should be clang-formatted [-Wclang-format-violations]
            r"#define LLDB_REVISION " + lldb_version_patch,
             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:47:40: error: code should be clang-formatted [-Wclang-format-violations]
            r"#define LLDB_REVISION " + lldb_version_patch,
                                       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:47:60: error: code should be clang-formatted [-Wclang-format-violations]
            r"#define LLDB_REVISION " + lldb_version_patch,
                                                           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:48:25: error: code should be clang-formatted [-Wclang-format-violations]
            file_buffer,
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:49:10: error: code should be clang-formatted [-Wclang-format-violations]
        )
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:50:22: error: code should be clang-formatted [-Wclang-format-violations]
        file_buffer = re.sub(
                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:50:30: error: code should be clang-formatted [-Wclang-format-violations]
        file_buffer = re.sub(
                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:51:39: error: code should be clang-formatted [-Wclang-format-violations]
            LLDB_VERSION_STRING_REGEX,
                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:52:14: error: code should be clang-formatted [-Wclang-format-violations]
            r'#define LLDB_VERSION_STRING "{0}.{1}.{2}"'.format(
             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:52:57: error: code should be clang-formatted [-Wclang-format-violations]
            r'#define LLDB_VERSION_STRING "{0}.{1}.{2}"'.format(
                                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:52:65: error: code should be clang-formatted [-Wclang-format-violations]
            r'#define LLDB_VERSION_STRING "{0}.{1}.{2}"'.format(
                                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:53:36: error: code should be clang-formatted [-Wclang-format-violations]
                lldb_version_major, lldb_version_minor, lldb_version_patch
                                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:53:56: error: code should be clang-formatted [-Wclang-format-violations]
                lldb_version_major, lldb_version_minor, lldb_version_patch
                                                       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:53:75: error: code should be clang-formatted [-Wclang-format-violations]
                lldb_version_major, lldb_version_minor, lldb_version_patch
                                                                          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:54:15: error: code should be clang-formatted [-Wclang-format-violations]
            ),
              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:55:25: error: code should be clang-formatted [-Wclang-format-violations]
            file_buffer,
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:56:10: error: code should be clang-formatted [-Wclang-format-violations]
        )
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:57:39: error: code should be clang-formatted [-Wclang-format-violations]
        output_file.write(file_buffer)
                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:60:26: error: code should be clang-formatted [-Wclang-format-violations]
if __name__ == "__main__":
                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py:60:27: error: code should be clang-formatted [-Wclang-format-violations]
if __name__ == "__main__":
                          ^
```
### 🧪 clang-tidy Output
```text
error: unable to handle compilation, expected exactly one compiler job in '' [clang-diagnostic-error]
warning: C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py: 'linker' input unused [clang-diagnostic-unused-command-line-argument]Error while processing C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\scripts\version-header-fix.py.
Found compiler error(s).
```
### 🤖 GenAI Review
```text
🤖 **GenAI Review for `lldb/scripts/version-header-fix.py`**

```diff
lldb/scripts/version-header-fix.py
```

🧠 **Feedback**:
The above changes appear structurally sound. Consider reviewing:
- Code readability and formatting
- Potential edge case handling
- Naming conventions and code reuse
```

---

## `lldb/source/API/CMakeLists.txt`

### 🧹 clang-format Output
```text
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:9:56: error: code should be clang-formatted [-Wclang-format-violations]
  if (APPLE AND LLVM_ENABLE_LOCAL_SUBMODULE_VISIBILITY)
                                                       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:10:6: error: code should be clang-formatted [-Wclang-format-violations]
    # Work around an issue with the Python headers, which have a modular include
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:10:81: error: code should be clang-formatted [-Wclang-format-violations]
    # Work around an issue with the Python headers, which have a modular include
                                                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:11:6: error: code should be clang-formatted [-Wclang-format-violations]
    # inside an extern "C" block.
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:23:2: error: code should be clang-formatted [-Wclang-format-violations]
# Generate SBLanguages.h from Dwarf.def.
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:2: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:6: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:7: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:16: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:17: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:21: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                    ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:22: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:30: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:31: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:35: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:36: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:64: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:151:65: error: code should be clang-formatted [-Wclang-format-violations]
# lib/pythonX.Y/dist-packages/lldb/_lldb.so is a symlink to lib/liblldb.so,
                                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:2: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:23: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:24: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:31: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:35: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:58: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                                                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:62: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                                                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:63: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                                                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:70: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                                                                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:152:71: error: code should be clang-formatted [-Wclang-format-violations]
# which depends on lib/libLLVM*.so (BUILD_SHARED_LIBS) or lib/libLLVM-10git.so
                                                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:153:2: error: code should be clang-formatted [-Wclang-format-violations]
# (LLVM_LINK_LLVM_DYLIB). Add an additional rpath $ORIGIN/../../../../lib so
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:153:26: error: code should be clang-formatted [-Wclang-format-violations]
# (LLVM_LINK_LLVM_DYLIB). Add an additional rpath $ORIGIN/../../../../lib so
                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:153:58: error: code should be clang-formatted [-Wclang-format-violations]
# (LLVM_LINK_LLVM_DYLIB). Add an additional rpath $ORIGIN/../../../../lib so
                                                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:153:71: error: code should be clang-formatted [-Wclang-format-violations]
# (LLVM_LINK_LLVM_DYLIB). Add an additional rpath $ORIGIN/../../../../lib so
                                                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:154:2: error: code should be clang-formatted [-Wclang-format-violations]
# that _lldb.so can be loaded from Python.
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:206:35: error: code should be clang-formatted [-Wclang-format-violations]
  if (NOT LLDB_EXPORT_ALL_SYMBOLS)
                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:207:6: error: code should be clang-formatted [-Wclang-format-violations]
    # If we're not exporting all symbols, we'll want to explicitly set
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:207:12: error: code should be clang-formatted [-Wclang-format-violations]
    # If we're not exporting all symbols, we'll want to explicitly set
           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:207:46: error: code should be clang-formatted [-Wclang-format-violations]
    # If we're not exporting all symbols, we'll want to explicitly set
                                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:207:71: error: code should be clang-formatted [-Wclang-format-violations]
    # If we're not exporting all symbols, we'll want to explicitly set
                                                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:208:6: error: code should be clang-formatted [-Wclang-format-violations]
    # the exported symbols here.  This prevents 'log enable --stack ...'
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:208:33: error: code should be clang-formatted [-Wclang-format-violations]
    # the exported symbols here.  This prevents 'log enable --stack ...'
                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:208:73: error: code should be clang-formatted [-Wclang-format-violations]
    # the exported symbols here.  This prevents 'log enable --stack ...'
                                                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:209:6: error: code should be clang-formatted [-Wclang-format-violations]
    # from working on some systems but limits the liblldb size.
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:212:52: error: code should be clang-formatted [-Wclang-format-violations]
  elseif (NOT LLDB_EXPORT_ALL_SYMBOLS_EXPORTS_FILE)
                                                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:213:6: error: code should be clang-formatted [-Wclang-format-violations]
    # Don't use an explicit export. Instead, tell the linker to export all symbols.
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:226:103: error: code should be clang-formatted [-Wclang-format-violations]
  message(STATUS "Symbols (liblldb): exporting all symbols from the lldb and lldb_private namespaces")
                                                                                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:228:4: error: code should be clang-formatted [-Wclang-format-violations]
  # Pull out the various lldb libraries linked into liblldb, these will be used
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:228:80: error: code should be clang-formatted [-Wclang-format-violations]
  # Pull out the various lldb libraries linked into liblldb, these will be used
                                                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:229:4: error: code should be clang-formatted [-Wclang-format-violations]
  # when looking for symbols to extract. We ignore most plugin libraries here,
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:229:41: error: code should be clang-formatted [-Wclang-format-violations]
  # when looking for symbols to extract. We ignore most plugin libraries here,
                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:229:79: error: code should be clang-formatted [-Wclang-format-violations]
  # when looking for symbols to extract. We ignore most plugin libraries here,
                                                                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:230:4: error: code should be clang-formatted [-Wclang-format-violations]
  # because we may expose more symbols than the DLL limit and these symbols
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:230:76: error: code should be clang-formatted [-Wclang-format-violations]
  # because we may expose more symbols than the DLL limit and these symbols
                                                                           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:231:4: error: code should be clang-formatted [-Wclang-format-violations]
  # aren't useful to expose.
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:244:36: error: code should be clang-formatted [-Wclang-format-violations]
  list(REMOVE_DUPLICATES lldb_libs)
                                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:246:4: error: code should be clang-formatted [-Wclang-format-violations]
  # Extract all of the private symbols and produce a single file we can use for
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:246:80: error: code should be clang-formatted [-Wclang-format-violations]
  # Extract all of the private symbols and produce a single file we can use for
                                                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:247:4: error: code should be clang-formatted [-Wclang-format-violations]
  # the exports.
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:254:25: error: code should be clang-formatted [-Wclang-format-violations]
      ${lldb_libs} -o ${exported_symbol_file} --nm=${llvm_nm_exe}
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:272:2: error: code should be clang-formatted [-Wclang-format-violations]
# The Clang expression parser in LLDB requires the Clang resource directory to function.
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:272:79: error: code should be clang-formatted [-Wclang-format-violations]
# The Clang expression parser in LLDB requires the Clang resource directory to function.
                                                                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:273:35: error: code should be clang-formatted [-Wclang-format-violations]
if (TARGET clang-resource-headers)
                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:274:4: error: code should be clang-formatted [-Wclang-format-violations]
  # If building alongside Clang, just add a dependency to ensure it is build together with liblldb.
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:274:33: error: code should be clang-formatted [-Wclang-format-violations]
  # If building alongside Clang, just add a dependency to ensure it is build together with liblldb.
                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:276:7: error: code should be clang-formatted [-Wclang-format-violations]
else()
      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:277:4: error: code should be clang-formatted [-Wclang-format-violations]
  # In a standalone build create a symlink from the LLDB library directory that points to the
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:277:80: error: code should be clang-formatted [-Wclang-format-violations]
  # In a standalone build create a symlink from the LLDB library directory that points to the
                                                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:277:94: error: code should be clang-formatted [-Wclang-format-violations]
  # In a standalone build create a symlink from the LLDB library directory that points to the
                                                                                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:278:4: error: code should be clang-formatted [-Wclang-format-violations]
  # resource directory in the Clang library directory. LLDB searches relative to its install path,
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:278:55: error: code should be clang-formatted [-Wclang-format-violations]
  # resource directory in the Clang library directory. LLDB searches relative to its install path,
                                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:278:81: error: code should be clang-formatted [-Wclang-format-violations]
  # resource directory in the Clang library directory. LLDB searches relative to its install path,
                                                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:278:99: error: code should be clang-formatted [-Wclang-format-violations]
  # resource directory in the Clang library directory. LLDB searches relative to its install path,
                                                                                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:279:4: error: code should be clang-formatted [-Wclang-format-violations]
  # and the symlink is created in the same relative path as the resource directory of Clang when
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:279:73: error: code should be clang-formatted [-Wclang-format-violations]
  # and the symlink is created in the same relative path as the resource directory of Clang when
                                                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:279:97: error: code should be clang-formatted [-Wclang-format-violations]
  # and the symlink is created in the same relative path as the resource directory of Clang when
                                                                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:280:4: error: code should be clang-formatted [-Wclang-format-violations]
  # building alongside Clang.
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:280:30: error: code should be clang-formatted [-Wclang-format-violations]
  # building alongside Clang.
                             ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:281:4: error: code should be clang-formatted [-Wclang-format-violations]
  # When building the LLDB framework, this isn't necessary as there we copy everything we need into
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:281:100: error: code should be clang-formatted [-Wclang-format-violations]
  # When building the LLDB framework, this isn't necessary as there we copy everything we need into
                                                                                                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:282:4: error: code should be clang-formatted [-Wclang-format-violations]
  # the framework (including the Clang resourece directory).
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:282:18: error: code should be clang-formatted [-Wclang-format-violations]
  # the framework (including the Clang resourece directory).
                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt:293:2: error: code should be clang-formatted [-Wclang-format-violations]
# Stage all headers in the include directory in the build dir.
 ^
```
### 🧪 clang-tidy Output
```text
error: unable to handle compilation, expected exactly one compiler job in '' [clang-diagnostic-error]
warning: C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt: 'linker' input unused [clang-diagnostic-unused-command-line-argument]Error while processing C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\source\API\CMakeLists.txt.
Found compiler error(s).
```
### 🤖 GenAI Review
```text
🤖 **GenAI Review for `lldb/source/API/CMakeLists.txt`**

```diff
lldb/source/API/CMakeLists.txt
```

🧠 **Feedback**:
The above changes appear structurally sound. Consider reviewing:
- Code readability and formatting
- Potential edge case handling
- Naming conventions and code reuse
```

---

## `lldb/test/Shell/Scripts/Inputs/lldb-defines.h`

### 🧹 clang-format Output
```text
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\Inputs\lldb-defines.h:4:71: error: code should be clang-formatted [-Wclang-format-violations]
// The script needs to uncomment these lines and populate the info for versioning.
                                                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\Inputs\lldb-defines.h:4:83: error: code should be clang-formatted [-Wclang-format-violations]
// The script needs to uncomment these lines and populate the info for versioning.
                                                                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\Inputs\lldb-defines.h:5:1: error: code should be clang-formatted [-Wclang-format-violations]
// #define LLDB_VERSION
^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\Inputs\lldb-defines.h:5:24: error: code should be clang-formatted [-Wclang-format-violations]
// #define LLDB_VERSION
                       ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\Inputs\lldb-defines.h:6:1: error: code should be clang-formatted [-Wclang-format-violations]
// #define LLDB_REVISION
^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\Inputs\lldb-defines.h:6:25: error: code should be clang-formatted [-Wclang-format-violations]
// #define LLDB_REVISION
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\Inputs\lldb-defines.h:7:1: error: code should be clang-formatted [-Wclang-format-violations]
// #define LLDB_VERSION_STRING
^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\Inputs\lldb-defines.h:7:11: error: code should be clang-formatted [-Wclang-format-violations]
// #define LLDB_VERSION_STRING
          ^
```
### 🧪 clang-tidy Output
```text

```
### 🤖 GenAI Review
```text
🤖 **GenAI Review for `lldb/test/Shell/Scripts/Inputs/lldb-defines.h`**

```diff
lldb/test/Shell/Scripts/Inputs/lldb-defines.h
```

🧠 **Feedback**:
The above changes appear structurally sound. Consider reviewing:
- Code readability and formatting
- Potential edge case handling
- Naming conventions and code reuse
```

---

## `lldb/test/Shell/Scripts/TestVersionFixScript.test`

### 🧹 clang-format Output
```text
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:1:2: error: code should be clang-formatted [-Wclang-format-violations]
# Create a temp dir for output and run the version fix script on the truncated version of lldb-defines.h in the inputs dir.
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:1:79: error: code should be clang-formatted [-Wclang-format-violations]
# Create a temp dir for output and run the version fix script on the truncated version of lldb-defines.h in the inputs dir.
                                                                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:1:95: error: code should be clang-formatted [-Wclang-format-violations]
# Create a temp dir for output and run the version fix script on the truncated version of lldb-defines.h in the inputs dir.
                                                                                              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:1:96: error: code should be clang-formatted [-Wclang-format-violations]
# Create a temp dir for output and run the version fix script on the truncated version of lldb-defines.h in the inputs dir.
                                                                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:2:4: error: code should be clang-formatted [-Wclang-format-violations]
RUN: mkdir -p %t/Outputs
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:2:13: error: code should be clang-formatted [-Wclang-format-violations]
RUN: mkdir -p %t/Outputs
            ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:2:16: error: code should be clang-formatted [-Wclang-format-violations]
RUN: mkdir -p %t/Outputs
               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:2:17: error: code should be clang-formatted [-Wclang-format-violations]
RUN: mkdir -p %t/Outputs
                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:2:18: error: code should be clang-formatted [-Wclang-format-violations]
RUN: mkdir -p %t/Outputs
                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:2:25: error: code should be clang-formatted [-Wclang-format-violations]
RUN: mkdir -p %t/Outputs
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:4: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:7: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:15: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
              ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:16: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:26: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:33: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:34: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:41: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:42: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:48: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:49: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:57: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:58: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:59: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:65: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:66: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:70: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:71: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                      ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:82: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                                 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:83: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:84: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:91: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                                          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:92: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                                           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:96: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                                               ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:3:97: error: code should be clang-formatted [-Wclang-format-violations]
RUN: %python %p/../../../scripts/version-header-fix.py %p/Inputs/lldb-defines.h %t/Outputs/lldb-defines.h 21 0 12
                                                                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:5:2: error: code should be clang-formatted [-Wclang-format-violations]
# Check the output
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:5:19: error: code should be clang-formatted [-Wclang-format-violations]
# Check the output
                  ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:4: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:11: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:12: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:13: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
            ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:20: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:21: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
                    ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:25: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
                        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:26: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
                         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:37: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
                                    ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:6:49: error: code should be clang-formatted [-Wclang-format-violations]
RUN: cat %t/Outputs/lldb-defines.h | FileCheck %s
                                                ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:8:2: error: code should be clang-formatted [-Wclang-format-violations]
# The LLDB version defines must be uncommented and filled in with the values passed into the script.
 ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:8:77: error: code should be clang-formatted [-Wclang-format-violations]
# The LLDB version defines must be uncommented and filled in with the values passed into the script.
                                                                            ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:8:101: error: code should be clang-formatted [-Wclang-format-violations]
# The LLDB version defines must be uncommented and filled in with the values passed into the script.
                                                                                                    ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:9:6: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION 21
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:9:9: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION 21
        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:9:10: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION 21
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:9:11: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION 21
          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:9:12: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION 21
           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:9:13: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION 21
            ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:9:36: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION 21
                                   ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:10:6: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_REVISION 12
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:10:9: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_REVISION 12
        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:10:10: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_REVISION 12
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:10:11: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_REVISION 12
          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:10:12: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_REVISION 12
           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:10:13: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_REVISION 12
            ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:10:37: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_REVISION 12
                                    ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:11:6: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION_STRING "21.0.12"
     ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:11:9: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION_STRING "21.0.12"
        ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:11:10: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION_STRING "21.0.12"
         ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:11:11: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION_STRING "21.0.12"
          ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:11:12: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION_STRING "21.0.12"
           ^
C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test:11:13: error: code should be clang-formatted [-Wclang-format-violations]
CHECK: {{^}}#define LLDB_VERSION_STRING "21.0.12"
            ^
```
### 🧪 clang-tidy Output
```text
error: unable to handle compilation, expected exactly one compiler job in '' [clang-diagnostic-error]
warning: C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test: 'linker' input unused [clang-diagnostic-unused-command-line-argument]Error while processing C:\Users\Fries\AppData\Local\Temp\tmphus7v5a2\lldb\test\Shell\Scripts\TestVersionFixScript.test.
Found compiler error(s).
```
### 🤖 GenAI Review
```text
🤖 **GenAI Review for `lldb/test/Shell/Scripts/TestVersionFixScript.test`**

```diff
lldb/test/Shell/Scripts/TestVersionFixScript.test
```

🧠 **Feedback**:
The above changes appear structurally sound. Consider reviewing:
- Code readability and formatting
- Potential edge case handling
- Naming conventions and code reuse
```

---

