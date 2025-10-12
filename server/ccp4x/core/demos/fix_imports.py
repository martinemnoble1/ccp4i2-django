#!/usr/bin/env python3
"""Fix import issues in CData classes files."""

import os
import re
from pathlib import Path

# Define the correct locations for each class
CLASS_LOCATIONS = {
    "CInt": "fundamental_types",
    "CFloat": "fundamental_types",
    "CList": "fundamental_types",
    "CString": "base_classes",
    "CData": "base_classes",
    "CDataFile": "base_classes",
    "CContainer": "base_classes",
    "CDataFileContent": "base_classes",
}


def fix_imports_in_file(filepath):
    """Fix imports in a single file."""
    with open(filepath, "r") as f:
        content = f.read()

    # Find the import line that imports from base_classes
    import_pattern = r"from \.base_classes import (.+)"
    match = re.search(import_pattern, content)

    if not match:
        return False

    imported_classes = [cls.strip() for cls in match.group(1).split(",")]

    # Separate classes by their correct modules
    base_classes = []
    fundamental_classes = []

    for cls in imported_classes:
        if cls in CLASS_LOCATIONS:
            if CLASS_LOCATIONS[cls] == "base_classes":
                base_classes.append(cls)
            elif CLASS_LOCATIONS[cls] == "fundamental_types":
                fundamental_classes.append(cls)

    # Create new import lines
    new_imports = []
    if base_classes:
        new_imports.append(f"from .base_classes import {', '.join(base_classes)}")
    if fundamental_classes:
        new_imports.append(
            f"from .fundamental_types import {', '.join(fundamental_classes)}"
        )

    # Replace the old import
    new_content = re.sub(import_pattern, "\n".join(new_imports), content)

    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Fixed imports in {filepath}")
        return True

    return False


def main():
    # Process all *_classes.py files
    classes_dir = Path(__file__).parent.parent / "new_cdata"

    for filepath in classes_dir.glob("*_classes.py"):
        if filepath.name != "analyze_missing_classes.py":
            fix_imports_in_file(str(filepath))


if __name__ == "__main__":
    main()
