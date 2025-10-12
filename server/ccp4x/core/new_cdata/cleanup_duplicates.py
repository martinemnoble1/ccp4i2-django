#!/usr/bin/env python3.12

import os
import re


def remove_duplicate_decorators_from_file(file_path):
    """Remove duplicate @cdata_class decorators from a file"""
    with open(file_path, "r") as f:
        lines = f.readlines()

    cleaned_lines = []
    i = 0
    duplicates_removed = 0

    while i < len(lines):
        line = lines[i]
        cleaned_lines.append(line)

        # If this line starts a @cdata_class decorator
        if line.strip().startswith("@cdata_class"):
            decorator_start = i
            decorator_lines = [line]

            # Read the complete decorator (until the closing parenthesis)
            paren_count = line.count("(") - line.count(")")
            i += 1

            while i < len(lines) and paren_count > 0:
                decorator_lines.append(lines[i])
                paren_count += lines[i].count("(") - lines[i].count(")")
                i += 1

            # Now check if the next non-empty, non-comment lines are duplicate decorators
            while i < len(lines):
                # Skip empty lines and comments
                if lines[i].strip() == "" or lines[i].strip().startswith("#"):
                    cleaned_lines.append(lines[i])
                    i += 1
                    continue

                # If we find another @cdata_class decorator, check if it's a duplicate
                if lines[i].strip().startswith("@cdata_class"):
                    duplicate_start = i
                    duplicate_lines = [lines[i]]

                    # Read the complete duplicate decorator
                    paren_count = lines[i].count("(") - lines[i].count(")")
                    i += 1

                    while i < len(lines) and paren_count > 0:
                        duplicate_lines.append(lines[i])
                        paren_count += lines[i].count("(") - lines[i].count(")")
                        i += 1

                    # Compare decorators (ignoring whitespace differences)
                    original_content = (
                        "".join(decorator_lines)
                        .replace(" ", "")
                        .replace("\n", "")
                        .replace("\t", "")
                    )
                    duplicate_content = (
                        "".join(duplicate_lines)
                        .replace(" ", "")
                        .replace("\n", "")
                        .replace("\t", "")
                    )

                    if original_content == duplicate_content:
                        # It's a duplicate, skip it
                        duplicates_removed += 1
                        print(
                            f"  Removed duplicate decorator at line {duplicate_start + 1}"
                        )
                        continue
                    else:
                        # It's a different decorator, keep it
                        cleaned_lines.extend(duplicate_lines)
                        decorator_lines = duplicate_lines  # Update for next comparison
                        continue
                else:
                    # Not a decorator, we're done checking for duplicates
                    break
        else:
            i += 1

    return cleaned_lines, duplicates_removed


def main():
    """Main function to clean up duplicate decorators"""
    # Get all Python class files
    class_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    total_duplicates_removed = 0
    files_modified = []

    for file_path in class_files:
        print(f"Checking {file_path}...")

        # Process the file
        cleaned_lines, duplicates_removed = remove_duplicate_decorators_from_file(
            file_path
        )

        if duplicates_removed > 0:
            # Write the cleaned content back
            with open(file_path, "w") as f:
                f.writelines(cleaned_lines)

            files_modified.append(file_path)
            total_duplicates_removed += duplicates_removed
            print(
                f"  ✅ Removed {duplicates_removed} duplicate decorators from {file_path}"
            )
        else:
            print(f"  ✓ No duplicates found in {file_path}")

    print(f"\n🎯 Summary:")
    print(f"Files modified: {len(files_modified)}")
    print(f"Total duplicate decorators removed: {total_duplicates_removed}")

    if files_modified:
        print(f"\nModified files:")
        for file_path in files_modified:
            print(f"  - {file_path}")

    # Verify syntax of modified files
    if files_modified:
        print(f"\n🔍 Verifying syntax of modified files...")
        for file_path in files_modified:
            try:
                with open(file_path, "r") as f:
                    compile(f.read(), file_path, "exec")
                print(f"  ✅ {file_path} - syntax OK")
            except SyntaxError as e:
                print(f"  ❌ {file_path} - syntax error: {e}")


if __name__ == "__main__":
    main()
