#!/usr/bin/env python3.12

import re


def find_detailed_duplicates(file_path):
    """Find detailed duplicate patterns in a file"""
    with open(file_path, "r") as f:
        content = f.read()

    # Find all decorator-class combinations
    pattern = (
        r"(@cdata_class\s*\([^@]*?\))\s*(class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):)"
    )
    matches = list(re.finditer(pattern, content, re.DOTALL))

    print(f"\n📄 Analyzing {file_path}")
    print(f"Found {len(matches)} decorator-class combinations")

    # Group by class name
    class_groups = {}
    for match in matches:
        class_name = match.group(3)
        if class_name not in class_groups:
            class_groups[class_name] = []
        class_groups[class_name].append(
            {
                "decorator": match.group(1),
                "class_line": match.group(2),
                "start": match.start(),
                "line_num": content[: match.start()].count("\n") + 1,
            }
        )

    # Find duplicates
    duplicates = []
    for class_name, occurrences in class_groups.items():
        if len(occurrences) > 1:
            print(f"  🔍 Class {class_name} has {len(occurrences)} decorators:")
            for i, occ in enumerate(occurrences):
                print(f"    #{i+1}: Line {occ['line_num']}")
                # Show first few lines of decorator
                decorator_lines = occ["decorator"].split("\n")[:3]
                print(
                    f"         {' '.join(line.strip() for line in decorator_lines if line.strip())}"
                )
            duplicates.extend(occurrences[:-1])  # All but last are duplicates

    return duplicates


def main():
    """Check for detailed duplicates in problem files"""
    problem_files = [
        "ccp4xtaldata_classes.py",
        "ccp4modeldata_classes.py",
        "ccp4file_classes.py",
    ]

    total_duplicates = 0
    for file_path in problem_files:
        duplicates = find_detailed_duplicates(file_path)
        total_duplicates += len(duplicates)

    print(f"\n🎯 Total duplicates found: {total_duplicates}")


if __name__ == "__main__":
    main()
