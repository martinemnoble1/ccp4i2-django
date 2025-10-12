#!/usr/bin/env python3
"""
Simple Usage Guide: Complete CCP4i2 XML Workflow

This shows the essential code patterns for working with DEF and Params XML files.
"""

import sys

sys.path.insert(0, "/Users/nmemn/Developer/ccp4i2-django/server")

from ccp4x.core.data_manager.def_xml_parser import parse_def_xml_file
from ccp4x.core.data_manager.params_xml_handler import (
    export_task_params,
    import_task_params,
)


def simple_usage_example():
    """Show the essential usage patterns."""

    print("🎯 Simple CCP4i2 XML Workflow Usage")
    print("=" * 40)

    # ================================
    # SCENARIO 1: Create a new task
    # ================================
    print("\n📋 Scenario 1: Create a new task")

    # Load task definition
    task = parse_def_xml_file("/path/to/servalcat_pipe.def.xml")

    # Configure parameters (user input)
    task.controlParameters.NCYCLES.value = 50
    task.controlParameters.ADD_WATERS.value = True
    task.controlParameters.DATA_METHOD.value = "xtal"

    # Set input files
    # task.inputData.XYZIN.set_file_info(project="proj1", baseName="input.pdb", ...)

    # Export user settings to params file
    export_task_params(task, "/path/to/job_123.params.xml", user_id="scientist")

    print("✅ New task configured and params exported")

    # ================================
    # SCENARIO 2: Resume existing task
    # ================================
    print("\n🔄 Scenario 2: Resume existing task")

    # Load fresh task definition
    fresh_task = parse_def_xml_file("/path/to/servalcat_pipe.def.xml")

    # Import previous user settings
    import_task_params(fresh_task, "/path/to/job_123.params.xml")

    # Task is now ready with user's previous configuration
    # fresh_task.controlParameters.NCYCLES.value == 50
    # fresh_task.controlParameters.ADD_WATERS.value == True

    print("✅ Task restored from params file")

    # ================================
    # SCENARIO 3: Modify existing task
    # ================================
    print("\n🔧 Scenario 3: Modify existing task")

    # Load and restore task
    task = parse_def_xml_file("/path/to/servalcat_pipe.def.xml")
    import_task_params(task, "/path/to/job_123.params.xml")

    # Make additional changes
    task.controlParameters.WEIGHT.value = 0.2
    task.metalCoordPipeline.RUN_METALCOORD.value = True

    # Export updated settings
    export_task_params(task, "/path/to/job_123_modified.params.xml")

    print("✅ Task modified and new params exported")


def show_key_features():
    """Demonstrate key features of the system."""

    print("\n🌟 Key Features Demonstrated:")
    print("  • Complete task structure from .def.xml")
    print("  • User parameter tracking with set states")
    print("  • Export only modified parameters to .params.xml")
    print("  • Perfect round-trip fidelity")
    print("  • Hierarchical container support")
    print("  • Multiple data types (CInt, CFloat, CBoolean, CString)")
    print("  • Path-based parameter access")
    print("  • Smart assignment semantics")


if __name__ == "__main__":
    simple_usage_example()
    show_key_features()

    print("\n📚 API Summary:")
    print("  parse_def_xml_file(path) -> task hierarchy")
    print("  export_task_params(task, path, user_id) -> bool")
    print("  import_task_params(task, path) -> bool")

    print("\n🎊 System ready for CCP4i2 production use!")
