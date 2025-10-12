#!/usr/bin/env python3.12

import re
import os


def fix_comma_syntax_errors():
    """Fix syntax errors caused by extra commas in decorators"""
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    for file_path in py_files:
        with open(file_path, "r") as f:
            content = f.read()

        original_content = content

        # Fix pattern: ,\n    <new_field>= where there's a comma before the new field
        # This happens when there's a trailing comma followed by a new field
        content = re.sub(r",\s*\n\s*,\s*\n\s*([a-z_]+\s*=)", r",\n    \1", content)

        # Fix pattern: gui_label="...",\n,\n    <new_field>=
        content = re.sub(
            r'(gui_label="[^"]*"),\s*\n\s*,\s*\n\s*([a-z_]+\s*=)',
            r"\1,\n    \2",
            content,
        )

        # Fix pattern: },\n,\n    <new_field>=
        content = re.sub(
            r"(\s*}),\s*\n\s*,\s*\n\s*([a-z_]+\s*=)", r"\1,\n    \2", content
        )

        # Fix standalone commas on their own lines in decorators
        # Look for @cdata_class blocks and fix commas within them
        def fix_decorator_commas(match):
            decorator_content = match.group(0)
            # Remove lines that are just commas
            fixed_content = re.sub(r"\n\s*,\s*\n", "\n", decorator_content)
            # Fix double commas
            fixed_content = re.sub(r",,+", ",", fixed_content)
            return fixed_content

        # Apply the fix to all @cdata_class decorators
        content = re.sub(
            r"@cdata_class\s*\([^@]*?\)\s*(?=class)",
            fix_decorator_commas,
            content,
            flags=re.DOTALL,
        )

        if content != original_content:
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Fixed syntax errors in {file_path}")

        # Validate syntax
        try:
            compile(content, file_path, "exec")
            print(f"✅ {file_path}: Syntax OK")
        except SyntaxError as e:
            print(f"❌ {file_path}: Still has syntax error - {e}")


if __name__ == "__main__":
    fix_comma_syntax_errors()
