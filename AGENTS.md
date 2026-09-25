# Session Documentation & README Generation Rule

This rule guides the creation and maintenance of `README.md` documentation files for learning/practice sessions within this repository (e.g., `session_*` folders).

## Objective

When requested to document, create, or update a `README.md` for any session folder, adhere to the guidelines and standard structure below to record the learning journey accurately, consistently, and constructively from the first-person perspective ("I") of someone who is learning the basics of Python programming.

---

## Generation Guidelines

### 1. Session Date Determination

- **Primary Source**: Identify the date when the session occurred primarily by inspecting the folder and file creation dates (birthtime timestamps) of the session directory or its earliest code files:
  - **macOS**:
    ```bash
    stat -f "%SB" -t "%Y-%m-%d" <session_folder>
    ```
  - **Linux**:
    ```bash
    stat -c "%w" <session_folder> | cut -d' ' -f1
    # Fallback to modification date if birthtime is unsupported:
    stat -c "%y" <session_folder> | cut -d' ' -f1
    ```
  - **Windows (PowerShell)**:
    ```powershell
    (Get-Item <session_folder>).CreationTime.ToString("yyyy-MM-dd")
    ```
  - **Cross-Platform (Python)**:
    ```bash
    python3 -c "import os, datetime; s=os.stat('<session_folder>'); t=getattr(s, 'st_birthtime', s.st_ctime); print(datetime.date.fromtimestamp(t))"
    ```
    _(Or inspect the earliest file creation timestamp in the folder)._
- **Fallback**: If creation timestamps are unavailable or inconclusive, fall back to git history:
  ```bash
  git log --format="%cd" --date=short --reverse -- <session_folder> | head -n 1
  ```
- Display the date prominently at the top of the `README.md` in `YYYY-MM-DD` format.

### 2. Files to Include & Exclude

- **Include**: All exercise scripts, practice problems, and code files created for that session.
- **Exclude**: Temporary and build/cache artifacts:
  - `tempCodeRunnerFile.py`
  - `__pycache__/`
  - `.DS_Store` and other editor/OS-generated files.

### 3. Required Sections for Each `README.md`

Each session's `README.md` must include:

1. **Title & Session Metadata**:
   - Session identifier (e.g., `Session 1: Python Basics & Input Handling`).
   - Session Date (`YYYY-MM-DD`).
   - Core topic / focus.
2. **Session Overview**:
   - A concise summary written in first-person ("I") of the key programming concepts learned or practiced during the session.
3. **File-by-File Breakdown**:
   For each script in the folder:
   - **File Name**: Formatted as a relative link or bold code name.
   - **Concept Covered**: The primary programming concept demonstrated (e.g., condition checks, recursion, loops).
   - **Code Explanation**: Clear, beginner-friendly explanation written in first person ("I") describing the script logic, how I wrote it, and how it works.
   - **Possible Improvements (Optional)**: Practical, constructive suggestions to help me write cleaner, more Pythonic code as I learn:
     - Pythonic idioms and style improvements.
     - Input validation and edge-case handling.
     - Code refactoring or alternative standard library approaches.
     - Readability or naming improvements.
4. **Key Takeaways / Summary**:
   - Bullet points summarizing what I learned or took away from that session.

---

## Standard Template

When creating a `README.md` inside a session folder, follow this template:

```markdown
# Session X: [Session Topic]

- **Date**: YYYY-MM-DD
- **Topic**: [Brief summary of main concepts]

## Overview

[Concise summary in first person ("In this session, I learned / practiced...") of what was covered during the session.]

---

## Files and Explanations

### `[filename.py]`

- **Concept**: [Concept demonstrated in this file]
- **Explanation**:
  [Detailed, beginner-friendly explanation in first person of how the code works and the logic behind it.]
- **Possible Improvements**:
  - [Constructive improvement 1 (e.g., style, validation, edge cases)]
  - [Constructive improvement 2 (e.g., alternative Pythonic approach)]

---

## Key Takeaways

- [What I learned / takeaway 1]
- [What I learned / takeaway 2]
```

---

## Tone and Style

- **First-Person POV ("I")**: Written from the learner's perspective (e.g., "In this session, I practiced...", "I created this script to..."), capturing a personal learning journal.
- **Beginner Mindset**: Grounded in basic Python programming. Explanations should be simple, intuitive, relatable, and accessible without assuming advanced software engineering concepts or using unnecessary jargon.
- **Educational & Encouraging**: Written to support learning and track programming growth over time.
- **Accurate & Clear**: Explain Python concepts simply and accurately.
- **Constructive**: Focus code improvements on practical best practices to help the learner level up.