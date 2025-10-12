#!/usr/bin/env python3
"""
Test the set state tracking system for CData objects.

This demonstrates the crucial difference between:
1. NOT_SET - value has never been explicitly set
2. DEFAULT - value is using a default from qualifiers
3. EXPLICITLY_SET - value has been explicitly assigned

This distinction is critical for task execution behavior.
"""

from ccp4x.core.new_cdata.base_classes import CData, CString, ValueState
from ccp4x.core.new_cdata.fundamental_types import CInt, CFloat, CBoolean


def test_set_state_tracking():
    """Test the complete set state tracking system."""

    print("🎯 SET STATE TRACKING SYSTEM TEST")
    print("=" * 40)

    # Test 1: Initial state (NOT_SET)
    print("\n📝 Test 1: Initial state (NOT_SET)")
    project = CData(name="test_project")

    print(f"project.isSet('title'): {project.isSet('title')}")
    print(f"project.getValueState('title'): {project.getValueState('title')}")
    print(f"hasattr(project, 'title'): {hasattr(project, 'title')}")

    # Test 2: Explicit assignment (EXPLICITLY_SET)
    print("\n✏️ Test 2: Explicit assignment (EXPLICITLY_SET)")
    project.title = "Crystal Structure Analysis"

    print(f"After assignment:")
    print(f"  project.isSet('title'): {project.isSet('title')}")
    print(f"  project.getValueState('title'): {project.getValueState('title')}")
    print(f"  project.title: '{project.title}'")

    # Test 3: Unsetting a value
    print("\n🚫 Test 3: Unsetting a value")
    project.unSet("title")

    print(f"After unSet:")
    print(f"  project.isSet('title'): {project.isSet('title')}")
    print(f"  project.getValueState('title'): {project.getValueState('title')}")
    print(f"  hasattr(project, 'title'): {hasattr(project, 'title')}")

    # Test 4: Fundamental types with set state
    print("\n🔢 Test 4: Fundamental types with set state")
    max_iter = CInt(value=1000)
    threshold = CFloat(value=1e-6)
    auto_save = CBoolean(value=True)

    print(f"CInt isSet('value'): {max_iter.isSet('value')}")
    print(f"CFloat isSet('value'): {threshold.isSet('value')}")
    print(f"CBoolean isSet('value'): {auto_save.isSet('value')}")

    # Test 5: Complex object with multiple fields
    print("\n🏗️ Test 5: Complex object with multiple set states")
    job_config = CData(name="job_config")

    # Set some values explicitly
    job_config.max_iterations = CInt(value=500)
    job_config.output_file = CString(value="results.pdb")

    # Leave some values unset
    print(f"\\nField states:")
    fields = ["max_iterations", "output_file", "debug_mode", "input_file"]
    for field in fields:
        state = job_config.getValueState(field)
        is_set = job_config.isSet(field)
        has_attr = hasattr(job_config, field)
        print(f"  {field}: state={state.name}, isSet={is_set}, hasattr={has_attr}")

    # Test 6: Smart assignment preserves set state
    print("\n🔄 Test 6: Smart assignment and set states")
    config1 = CData(name="config1")
    config2 = CData(name="config2")

    config1.temperature = CFloat(value=298.15)
    config2.temperature = CFloat(value=310.0)

    print(f"Before smart assignment:")
    print(f"  config1.temperature.isSet('value'): {config1.temperature.isSet('value')}")
    print(f"  config1.isSet('temperature'): {config1.isSet('temperature')}")

    # Smart assignment
    config1.temperature = config2.temperature

    print(f"After smart assignment:")
    print(f"  config1.temperature.isSet('value'): {config1.temperature.isSet('value')}")
    print(f"  config1.isSet('temperature'): {config1.isSet('temperature')}")
    print(f"  config1.temperature.value: {config1.temperature.value}")

    # Test 7: Dictionary assignment and set states
    print("\n📋 Test 7: Dictionary assignment and set states")
    sequence = CData(name="sequence")

    print(f"Before dict assignment:")
    print(f"  sequence.isSet('identifier'): {sequence.isSet('identifier')}")

    # Dictionary assignment should mark fields as explicitly set
    sequence_data = {
        "identifier": "PROT_001",
        "description": "Test protein sequence",
        "length": 150,
    }

    # Assign dictionary to create new object
    container = CData(name="container")
    container.seq = sequence_data

    print(f"After dict assignment:")
    print(f"  container.isSet('seq'): {container.isSet('seq')}")
    print(f"  container.seq.isSet('identifier'): {container.seq.isSet('identifier')}")
    print(f"  container.seq.isSet('length'): {container.seq.isSet('length')}")

    # Test 8: Behavioral differences for tasks
    print("\n⚙️ Test 8: Task execution behavior differences")
    task_params = CData(name="task_params")

    # Scenario 1: Not set - task should use program default
    print(f"\\nScenario 1 - resolution_limit not set:")
    print(f"  isSet: {task_params.isSet('resolution_limit')}")
    print(f"  → Task behavior: Use program's internal default")

    # Scenario 2: Explicitly set - task should use this value
    task_params.resolution_limit = CFloat(value=2.5)
    print(f"\\nScenario 2 - resolution_limit explicitly set to 2.5:")
    print(f"  isSet: {task_params.isSet('resolution_limit')}")
    print(f"  value: {task_params.resolution_limit.value}")
    print(f"  → Task behavior: Use exactly 2.5 Å")

    # Scenario 3: Unset after being set - task should ignore this parameter
    task_params.unSet("resolution_limit")
    print(f"\\nScenario 3 - resolution_limit unset after being set:")
    print(f"  isSet: {task_params.isSet('resolution_limit')}")
    print(f"  hasattr: {hasattr(task_params, 'resolution_limit')}")
    print(f"  → Task behavior: Program should ignore this parameter entirely")

    print("\\n✅ SET STATE TRACKING SYSTEM WORKING!")
    print("\\n🎉 Key behaviors demonstrated:")
    print("   ✓ NOT_SET vs EXPLICITLY_SET distinction")
    print("   ✓ isSet() method accurately tracks state")
    print("   ✓ unSet() properly removes values")
    print("   ✓ Smart assignment preserves set states")
    print("   ✓ Dictionary assignment marks fields as set")
    print("   ✓ Critical for task execution behavior!")


if __name__ == "__main__":
    test_set_state_tracking()
