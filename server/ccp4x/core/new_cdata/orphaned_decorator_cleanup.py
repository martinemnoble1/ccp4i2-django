#!/usr/bin/env python3.12

import re
import os


def find_and_remove_orphaned_decorators(file_path):
    """Find and remove orphaned @cdata_class decorators"""
    with open(file_path, "r") as f:
        content = f.read()
        original_content = content

    # Find all @cdata_class positions
    all_matches = list(re.finditer(r"@cdata_class", content))

    # Find complete decorator-class pairs
    valid_matches = list(
        re.finditer(r"@cdata_class\s*\([^@]*?\)\s*class", content, re.DOTALL)
    )

    valid_starts = {match.start() for match in valid_matches}

    orphaned_count = 0

    # Process from end to beginning to maintain positions
    for match in reversed(all_matches):
        if match.start() not in valid_starts:
            # This is an orphaned @cdata_class
            # Find the complete orphaned decorator
            start_pos = match.start()

            # Find the matching closing parenthesis
            pos = start_pos
            paren_count = 0
            in_decorator = False

            while pos < len(content):
                char = content[pos]

                if char == "(" and not in_decorator:
                    in_decorator = True
                    paren_count = 1
                elif in_decorator:
                    if char == "(":
                        paren_count += 1
                    elif char == ")":
                        paren_count -= 1
                        if paren_count == 0:
                            # Found the end of the decorator
                            end_pos = pos + 1
                            break
                pos += 1
            else:
                # Couldn't find matching parenthesis - skip this one
                continue

            # Extract the orphaned decorator
            orphaned_decorator = content[start_pos:end_pos]

            # Find the preceding newline to remove the whole line(s)
            line_start = content.rfind("\n", 0, start_pos) + 1

            # Find the following newline to remove cleanly
            line_end = content.find("\n", end_pos)
            if line_end == -1:
                line_end = end_pos
            else:
                line_end += 1  # Include the newline

            # Remove the orphaned decorator
            content = content[:line_start] + content[line_end:]
            orphaned_count += 1

            line_num = original_content[:start_pos].count("\n") + 1
            print(f"    Removed orphaned decorator at line {line_num}")

    if orphaned_count > 0:
        with open(file_path, "w") as f:
            f.write(content)

    return orphaned_count


def validate_syntax(file_path):
    """Validate Python syntax"""
    try:
        with open(file_path, "r") as f:
            compile(f.read(), file_path, "exec")
        return True
    except SyntaxError as e:
        print(f"  ❌ Syntax error: {e}")
        return False


def main():
    """Remove orphaned @cdata_class decorators"""
    print("🧹 ORPHANED DECORATOR CLEANUP")
    print("=" * 32)

    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    total_removed = 0
    files_modified = []

    for file_path in py_files:
        print(f"\n📄 Processing {file_path}...")

        removed = find_and_remove_orphaned_decorators(file_path)

        if removed > 0:
            # Validate syntax
            if validate_syntax(file_path):
                files_modified.append(file_path)
                total_removed += removed
                print(f"  ✅ Removed {removed} orphaned decorators, syntax OK")
            else:
                print(f"  ❌ Syntax error after cleanup - reverting")
                os.system(f"git checkout -- {file_path}")
        else:
            print(f"  ✓ No orphaned decorators found")

    print(f"\n🎯 Summary:")
    print(f"Total orphaned decorators removed: {total_removed}")
    print(f"Files modified: {len(files_modified)}")

    if files_modified:
        print(f"\nModified files:")
        for file_path in files_modified:
            print(f"  - {file_path}")

    # Final verification
    print(f"\n🔍 Final verification:")
    for file_path in py_files:
        with open(file_path, "r") as f:
            content = f.read()

        simple_count = content.count("@cdata_class")
        pattern_count = len(
            re.findall(r"@cdata_class\s*\([^@]*?\)\s*class", content, re.DOTALL)
        )

        if simple_count != pattern_count:
            print(
                f"  ⚠️  {file_path}: Still has {simple_count - pattern_count} orphaned decorators"
            )
        else:
            print(f"  ✅ {file_path}: Clean ({simple_count} decorators)")


if __name__ == "__main__":
    main()
