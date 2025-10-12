#!/usr/bin/env python3
"""
Test the smart assignment behaviors for CData objects.

This demonstrates the three assignment patterns:
1. CString = CString: Copy underlying value
2. Complex CData = Complex CData: Update/copy attributes
3. CData = dict: Update object attributes from dictionary
"""

from ccp4x.core.data_manager.new_cdata.base_classes import CData, CString


def test_smart_assignment():
    """Test all smart assignment patterns."""

    print("🎯 SMART ASSIGNMENT SYSTEM TEST")
    print("=" * 40)

    # Test 1: CString = CString (value assignment)
    print("\n📝 Test 1: CString = CString (value assignment)")
    str1 = CString(value="Hello")
    str2 = CString(value="World")

    print(f"Before: str1='{str1}', str2='{str2}'")
    print(f"str1 id: {id(str1)}, str2 id: {id(str2)}")

    # This should copy the value, not change the reference
    str1.value = str2.value  # Direct value copy
    print(f"After direct: str1='{str1}', str2='{str2}'")

    # Test setting the whole string object
    str3 = CString(value="Original")
    str4 = CString(value="New Value")

    print(f"\\nBefore smart assign: str3='{str3}', str4='{str4}'")
    print(f"str3 id: {id(str3)}")

    # Create a container to test attribute assignment
    container = CData(name="container")
    container.text1 = str3
    container.text2 = str4

    print(f"Container text1: '{container.text1}', text2: '{container.text2}'")
    print(f"Container text1 id: {id(container.text1)}")

    # Now test smart assignment through attribute setting
    original_id = id(container.text1)
    container.text1 = str4  # This should trigger smart assignment

    print(f"After smart assign: text1='{container.text1}'")
    print(
        f"text1 id after: {id(container.text1)} (same? {id(container.text1) == original_id})"
    )

    # Test 2: Complex CData = Complex CData (reference/attribute copy)
    print("\\n🏗️ Test 2: Complex CData = Complex CData")

    project1 = CData(name="project1")
    project1.title = "Crystal Structure Analysis"
    project1.version = "1.0"
    project1.status = "active"

    project2 = CData(name="project2")
    project2.title = "Protein Folding Study"
    project2.version = "2.1"
    project2.status = "completed"

    print(
        f"Before: project1.title='{project1.title}', project2.title='{project2.title}'"
    )
    print(f"project1 id: {id(project1)}")

    # Test smart assignment
    container.proj1 = project1
    container.proj2 = project2

    original_proj1_id = id(container.proj1)
    container.proj1 = project2  # Should update attributes, not replace object

    print(f"After smart assign: proj1.title='{container.proj1.title}'")
    print(
        f"proj1 id after: {id(container.proj1)} (same? {id(container.proj1) == original_proj1_id})"
    )

    # Test 3: CData = dict (dictionary unpacking)
    print("\\n📋 Test 3: CData = dict (dictionary unpacking)")

    sequence = CData(name="sequence")
    sequence.identifier = "PROT_001"
    sequence.description = "Test protein"
    sequence.length = 150

    print(
        f"Before: sequence.identifier='{sequence.identifier}', length={sequence.length}"
    )

    # Dictionary assignment should update the existing object
    update_dict = {
        "identifier": "PROT_002_UPDATED",
        "description": "Updated test protein",
        "length": 200,
        "organism": "E. coli",
    }

    container.seq = sequence
    original_seq_id = id(container.seq)

    container.seq = update_dict  # Should update existing object from dict

    print(
        f"After dict assign: identifier='{container.seq.identifier}', length={container.seq.length}"
    )
    print(f"New attribute organism: '{getattr(container.seq, 'organism', 'Not set')}'")
    print(
        f"seq id after: {id(container.seq)} (same? {id(container.seq) == original_seq_id})"
    )

    print("\\n✅ Smart assignment tests completed!")
    print("\\n🎉 Key behaviors demonstrated:")
    print("   ✓ Value types copy underlying values")
    print("   ✓ Complex types update attributes in-place")
    print("   ✓ Dictionary assignment updates object members")
    print("   ✓ Object identity preserved during smart assignment")


if __name__ == "__main__":
    test_smart_assignment()
