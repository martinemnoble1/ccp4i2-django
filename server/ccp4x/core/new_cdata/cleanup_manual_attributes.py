"""Script to clean up manual attribute declarations from decorated classes.

This script removes manual attribute declarations (like 'attr: Any = None')
from classes that already have @cdata_class decorators, since the metadata
system will create these attributes automatically.
"""

import re
import os
from pathlib import Path


def clean_decorated_class_file(file_path: str) -> bool:
    """Clean up a single file by removing manual attributes from decorated classes."""

    try:
        with open(file_path, "r") as f:
            content = f.read()

        lines = content.split("\n")
        new_lines = []
        i = 0
        modified = False

        while i < len(lines):
            line = lines[i]

            # Look for @cdata_class decorator
            if line.strip().startswith("@cdata_class("):
                # Add the decorator and its content
                new_lines.append(line)
                i += 1

                # Continue adding lines until we find the class definition
                while i < len(lines) and not lines[i].strip().startswith("class "):
                    new_lines.append(lines[i])
                    i += 1

                # Add the class definition line
                if i < len(lines):
                    new_lines.append(lines[i])  # class line
                    i += 1

                    # Add docstring if present
                    if i < len(lines) and '"""' in lines[i]:
                        new_lines.append(lines[i])
                        i += 1
                        # Continue until closing docstring
                        while i < len(lines) and not (
                            lines[i].strip().endswith('"""')
                            and lines[i].strip() != '"""'
                        ):
                            new_lines.append(lines[i])
                            i += 1
                        if i < len(lines):
                            new_lines.append(lines[i])  # closing docstring
                            i += 1

                    # Skip manual attribute declarations and replace with pass
                    found_attributes = False
                    while i < len(lines):
                        current_line = lines[i].strip()

                        # Check if this is a manual attribute declaration
                        if (
                            current_line
                            and ": Any = None" in current_line
                            and not current_line.startswith("class ")
                            and not current_line.startswith("def ")
                            and not current_line.startswith("@")
                        ):
                            found_attributes = True
                            i += 1  # Skip this line
                            modified = True
                        elif (
                            current_line.startswith("class ")
                            or current_line.startswith("def ")
                            or current_line.startswith("@")
                        ):
                            # Start of next class/method/decorator
                            break
                        elif current_line == "" or current_line.startswith("#"):
                            # Empty line or comment, keep it
                            new_lines.append(lines[i])
                            i += 1
                        else:
                            # Other content, keep it and stop looking for attributes
                            new_lines.append(lines[i])
                            i += 1
                            break

                    # Add pass statement if we removed attributes
                    if found_attributes:
                        new_lines.append("    pass")
                        new_lines.append("")  # Add blank line

            else:
                # Regular line, just add it
                new_lines.append(line)
                i += 1

        if modified:
            # Write back the cleaned content
            new_content = "\n".join(new_lines)
            with open(file_path, "w") as f:
                f.write(new_content)
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main function to clean up all decorated class files."""

    # Files that have been decorated
    base_dir = Path("/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/new_cdata")
    files_to_clean = [
        "ccp4mathsdata_classes.py",  # Already done manually
        "ccp4modeldata_classes.py",  # Partially done
        "ccp4file_classes.py",
        # Add more as we go
    ]

    print("Cleaning up manual attribute declarations from decorated classes...")
    print()

    for file_name in files_to_clean:
        file_path = base_dir / file_name
        if file_path.exists():
            print(f"Processing {file_name}...")
            cleaned = clean_decorated_class_file(str(file_path))
            if cleaned:
                print(f"  ✓ Cleaned up manual attributes")
            else:
                print(f"  - No manual attributes found")
        else:
            print(f"  ✗ File not found: {file_path}")

    print("\nDone cleaning up decorated class files!")


if __name__ == "__main__":
    main()
