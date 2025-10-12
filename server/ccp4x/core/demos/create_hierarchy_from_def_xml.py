#!/usr/bin/env python3
"""
Example: Create CData hierarchy from .def.xml file

This script demonstrates how to load a .def.xml file and create
a complete CData object hierarchy that you can use in your application.
"""

import sys
from pathlib import Path
from typing import Optional
import os

# Add the server directory to Python path (4 levels up from this demo file)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from ccp4x.core.task_manager.def_xml_parser import parse_def_xml_file


def create_task_from_def_xml(xml_file_path: str):
    """
    Create a complete CData task hierarchy from a .def.xml file.

    Args:
        xml_file_path: Path to the .def.xml file

    Returns:
        CContainer: Root task object with complete hierarchy
    """
    try:
        # Parse the XML file into a CData hierarchy
        task = parse_def_xml_file(xml_file_path)

        print(f"✅ Successfully loaded task: {task.name}")
        print(f"   Type: {type(task).__name__}")

        return task

    except FileNotFoundError:
        print(f"❌ File not found: {xml_file_path}")
        return None
    except Exception as e:
        print(f"❌ Error parsing {xml_file_path}: {e}")
        import traceback

        traceback.print_exc()
        return None


def explore_task_structure(task, max_depth: int = 3):
    """
    Explore and display the structure of a task hierarchy.

    Args:
        task: The root task object
        max_depth: Maximum depth to explore
    """
    print(f"\n🏗️ Task Structure for '{task.name}':")

    def explore_object(obj, indent="", depth=0):
        if depth >= max_depth:
            return

        for attr_name in sorted(dir(obj)):
            if (
                not attr_name.startswith("_")
                and not callable(getattr(obj, attr_name))
                and attr_name
                not in [
                    "child_added",
                    "child_removed",
                    "destroyed",
                    "object_info",
                    "parent_changed",
                    "state",
                ]
            ):

                try:
                    attr = getattr(obj, attr_name)
                    if hasattr(attr, "name"):  # It's a CData object
                        type_name = type(attr).__name__
                        print(f"{indent}{attr_name}: {type_name}")

                        # Show value and state for data types
                        if hasattr(attr, "value"):
                            try:
                                state = (
                                    attr.getValueState("value")
                                    if hasattr(attr, "getValueState")
                                    else "unknown"
                                )
                                print(
                                    f"{indent}  └─ value: {attr.value} (state: {state})"
                                )
                            except:
                                print(f"{indent}  └─ value: {attr.value}")

                        # Show metadata if available
                        if hasattr(attr, "_metadata") and attr._metadata:
                            meta = attr._metadata
                            if hasattr(meta, "help_text") and meta.help_text:
                                print(f"{indent}  └─ help: {meta.help_text[:50]}...")
                            if hasattr(meta, "enumerators") and meta.enumerators:
                                print(
                                    f"{indent}  └─ options: {', '.join(meta.enumerators)}"
                                )

                        # Recurse into containers
                        if type_name == "CContainer":
                            explore_object(attr, indent + "    ", depth + 1)

                except Exception:
                    pass  # Skip problematic attributes

    explore_object(task)


def demonstrate_hierarchy_usage(task):
    """
    Demonstrate how to use the created hierarchy.

    Args:
        task: The task hierarchy
    """
    print(f"\n🔧 Using Task '{task.name}':")

    # 1. Direct attribute access
    print("\n1. Direct attribute access:")
    if hasattr(task, "controlParameters"):
        params = task.controlParameters

        # Access parameters by name
        for param_name in ["NCYCLES", "ADD_WATERS", "DATA_METHOD", "WEIGHT"]:
            if hasattr(params, param_name):
                param = getattr(params, param_name)
                if hasattr(param, "value"):
                    print(f"   {param_name}: {param.value} ({type(param).__name__})")

    # 2. Path-based access
    print("\n2. Path-based access:")
    paths_to_try = [
        "controlParameters.NCYCLES",
        "controlParameters.ADD_WATERS",
        "inputData.XYZIN",
        "outputData.XYZOUT",
    ]

    for path in paths_to_try:
        try:
            obj = task.find_by_path(path)
            if obj and hasattr(obj, "value"):
                print(f"   {path}: {obj.value}")
            elif obj:
                print(f"   {path}: <{type(obj).__name__}>")
            else:
                print(f"   {path}: <not found>")
        except Exception as e:
            print(f"   {path}: <error: {e}>")

    # 3. Modify parameters and track state
    print("\n3. Parameter modification and state tracking:")
    if hasattr(task, "controlParameters") and hasattr(
        task.controlParameters, "NCYCLES"
    ):
        cycles = task.controlParameters.NCYCLES

        print(f"   Original: {cycles.value} (state: {cycles.getValueState('value')})")

        # Modify the value
        cycles.value = 50
        print(f"   Modified: {cycles.value} (state: {cycles.getValueState('value')})")

        # Reset to not set
        cycles.unSet("value")
        try:
            print(
                f"   After unSet: {cycles.value} (state: {cycles.getValueState('value')})"
            )
        except AttributeError:
            print(f"   After unSet: <unset> (state: {cycles.getValueState('value')})")


def main():
    """Main demonstration function."""
    print("🎯 DEF XML to CData Hierarchy Example")
    print("=" * 40)

    # Example XML file path (you would replace this with your actual path)
    xml_file_path = None

    # For demonstration, let's create a sample XML file
    sample_xml = """<?xml version="1.0" encoding="UTF-8"?>
<ns0:ccp4i2 xmlns:ns0="http://www.ccp4.ac.uk/ccp4ns">
  <ccp4i2_header>
    <pluginName>example_task</pluginName>
  </ccp4i2_header>
  <ccp4i2_body id="example_task">
    <ccp4i2_body>
      <container id="inputData">
        <content id="XYZIN">
          <className>CPdbDataFile</className>
          <qualifiers>
            <mustExist>True</mustExist>
            <toolTip>Input coordinate file</toolTip>
          </qualifiers>
        </content>
      </container>
      <container id="controlParameters">
        <content id="NCYCLES">
          <className>CInt</className>
          <qualifiers>
            <default>10</default>
            <min>1</min>
            <max>100</max>
            <toolTip>Number of refinement cycles</toolTip>
          </qualifiers>
        </content>
        <content id="ADD_WATERS">
          <className>CBoolean</className>
          <qualifiers>
            <default>False</default>
            <toolTip>Add water molecules</toolTip>
          </qualifiers>
        </content>
      </container>
      <container id="outputData">
        <content id="XYZOUT">
          <className>CPdbDataFile</className>
          <qualifiers>
            <toolTip>Output coordinate file</toolTip>
          </qualifiers>
        </content>
      </container>
    </ccp4i2_body>
  </ccp4i2_body>
</ns0:ccp4i2>"""

    # Create a temporary file for demonstration
    import tempfile

    with tempfile.NamedTemporaryFile(mode="w", suffix=".def.xml", delete=False) as f:
        f.write(sample_xml)
        xml_file_path = f.name

    try:
        # 1. Create the hierarchy from XML
        task = create_task_from_def_xml(xml_file_path)

        if task is not None:
            # 2. Explore the structure
            explore_task_structure(task)

            # 3. Demonstrate usage
            demonstrate_hierarchy_usage(task)

            print("\n✅ Hierarchy creation and usage completed successfully!")
            return task
        else:
            print("❌ Failed to create task hierarchy")
            return None

    finally:
        # Clean up temporary file
        Path(xml_file_path).unlink(missing_ok=True)


if __name__ == "__main__":
    task_hierarchy = main()
