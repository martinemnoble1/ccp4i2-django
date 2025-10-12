#!/usr/bin/env python3.12

import os


def fix_duplicate_decorators_in_file(file_path):
    """Fix duplicate @cdata_class decorators in a specific file"""
    with open(file_path, "r") as f:
        lines = f.readlines()

    issues_fixed = 0
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("@cdata_class"):
            # Found a decorator, find its end
            decorator_start = i
            paren_count = line.count("(") - line.count(")")
            j = i + 1

            # Find the end of this decorator
            while j < len(lines) and paren_count > 0:
                paren_count += lines[j].count("(") - lines[j].count(")")
                j += 1
            decorator_end = j

            # Now look for duplicate decorators
            k = decorator_end
            while k < len(lines):
                next_line = lines[k].strip()
                if next_line == "" or next_line.startswith("#"):
                    k += 1
                    continue
                elif next_line.startswith("@cdata_class"):
                    # Found a duplicate decorator! Remove it
                    duplicate_start = k
                    duplicate_paren_count = next_line.count("(") - next_line.count(")")
                    l = k + 1

                    # Find the end of the duplicate decorator
                    while l < len(lines) and duplicate_paren_count > 0:
                        duplicate_paren_count += lines[l].count("(") - lines[l].count(
                            ")"
                        )
                        l += 1
                    duplicate_end = l

                    # Remove the duplicate decorator lines
                    print(
                        f"  Removing duplicate decorator at lines {duplicate_start+1}-{duplicate_end}"
                    )
                    del lines[duplicate_start:duplicate_end]
                    issues_fixed += 1

                    # Adjust our position since we removed lines
                    # Continue checking from the same position
                    continue
                elif next_line.startswith("class "):
                    # Found the class, we're done
                    break
                else:
                    # Found something else, we're done
                    break

            i = decorator_end
        else:
            i += 1

    return lines, issues_fixed


def main():
    """Main function to fix duplicate decorators"""
    # Files that have duplicate decorator issues
    files_with_issues = [
        "ccp4modeldata_classes.py",
        "ccp4file_classes.py",
        "ccp4mathsdata_classes.py",
    ]

    total_issues_fixed = 0

    for file_path in files_with_issues:
        if os.path.exists(file_path):
            print(f"Fixing {file_path}...")

            # Fix the file
            fixed_lines, issues_fixed = fix_duplicate_decorators_in_file(file_path)

            if issues_fixed > 0:
                # Write the fixed content back
                with open(file_path, "w") as f:
                    f.writelines(fixed_lines)

                total_issues_fixed += issues_fixed
                print(f"  ✅ Fixed {issues_fixed} duplicate decorators in {file_path}")
            else:
                print(f"  ✓ No issues found in {file_path}")
        else:
            print(f"  ❌ File not found: {file_path}")

    print(f"\n🎯 Total duplicate decorators fixed: {total_issues_fixed}")

    # Verify syntax of modified files
    if total_issues_fixed > 0:
        print(f"\n🔍 Verifying syntax of modified files...")
        for file_path in files_with_issues:
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r") as f:
                        compile(f.read(), file_path, "exec")
                    print(f"  ✅ {file_path} - syntax OK")
                except SyntaxError as e:
                    print(f"  ❌ {file_path} - syntax error: {e}")


if __name__ == "__main__":
    main()
