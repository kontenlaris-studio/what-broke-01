#!/usr/bin/env python3
"""what-broke-01: say what actually broke."""
import os

ENTRY = "Nothing broke. Someone deployed on a Friday at 4:58 p.m., skipped the tests because they were 'flaky', and went home. The tests were right."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")

if __name__ == "__main__":
    main()
