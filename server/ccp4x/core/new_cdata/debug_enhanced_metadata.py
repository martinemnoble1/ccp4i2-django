#!/usr/bin/env python3.12

import json
import os
import re
from typing import Dict, List, Tuple


def load_json_metadata() -> Dict:
    """Load the JSON metadata file"""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["classes"]


def debug_class_decorator(class_name: str):
    """Debug a specific class to see what's happening"""
    print(f"\n🔍 DEBUG: Analyzing {class_name}")

    # Find the class
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    for file_path in py_files:
        with open(file_path, "r") as f:
            content = f.read()

        # Find this specific class
        class_pattern = rf"class\s+{re.escape(class_name)}\s*\([^)]+\):"
        class_match = re.search(class_pattern, content)

        if class_match:
            print(f"Found {class_name} in {file_path}")

            # Get the position and look backwards for decorator
            class_start = class_match.start()
            before_class = content[:class_start]

            # Look for decorator pattern
            decorator_pattern = r"@cdata_class\s*\([^@]*?\)\s*$"
            decorator_match = re.search(decorator_pattern, before_class, re.DOTALL)

            if decorator_match:
                decorator_text = decorator_match.group(0)
                print(f"Current decorator:\n{decorator_text}")

                # Check what's in it
                has_contents_order = "contents_order=" in decorator_text
                has_qualifiers_order = "qualifiers_order=" in decorator_text
                has_qualifiers_definition = "qualifiers_definition=" in decorator_text

                print(f"Has contents_order: {has_contents_order}")
                print(f"Has qualifiers_order: {has_qualifiers_order}")
                print(f"Has qualifiers_definition: {has_qualifiers_definition}")

                # Check JSON metadata
                metadata = load_json_metadata()
                if class_name in metadata:
                    json_meta = metadata[class_name]
                    print(f"JSON has CONTENTS_ORDER: {'CONTENTS_ORDER' in json_meta}")
                    if "CONTENTS_ORDER" in json_meta:
                        print(f"CONTENTS_ORDER value: {json_meta['CONTENTS_ORDER']}")
                    print(
                        f"JSON has QUALIFIERS_ORDER: {'QUALIFIERS_ORDER' in json_meta}"
                    )
                    if "QUALIFIERS_ORDER" in json_meta:
                        print(
                            f"QUALIFIERS_ORDER value: {json_meta['QUALIFIERS_ORDER']}"
                        )
                    print(
                        f"JSON has QUALIFIERS_DEFINITION: {'QUALIFIERS_DEFINITION' in json_meta}"
                    )
                    if "QUALIFIERS_DEFINITION" in json_meta:
                        print(
                            f"QUALIFIERS_DEFINITION value: {json_meta['QUALIFIERS_DEFINITION']}"
                        )

            else:
                print(f"No decorator found for {class_name}")

            return

    print(f"Class {class_name} not found")


def main():
    """Debug specific cases"""
    debug_class_decorator("CSequence")
    debug_class_decorator("CMtzDataFile")


if __name__ == "__main__":
    main()
