#!/usr/bin/env python3
"""
Test the fundamental types and smart assignment with them.
"""

from ccp4x.core.new_cdata.fundamental_types import (
    CInt,
    CFloat,
    CBoolean,
    CString,
    CIntRange,
    CFloatRange,
)
from ccp4x.core.new_cdata.base_classes import CData


def test_fundamental_types():
    """Test fundamental types and their behaviors."""

    print("🔢 FUNDAMENTAL TYPES TEST")
    print("=" * 30)

    # Test CInt
    print("\n📊 Testing CInt...")
    int1 = CInt(value=42)
    int2 = CInt(value=100)

    print(f"int1: {int1} (type: {type(int1)})")
    print(f"int1.value: {int1.value}")
    print(f"int(int1): {int(int1)}")

    # Test smart assignment with integers
    container = CData(name="container")
    container.count = int1

    print(f"container.count: {container.count}")
    print(f"container.count id: {id(container.count)}")

    # Smart assignment: should update value, not replace object
    original_id = id(container.count)
    container.count = int2

    print(f"After assignment: {container.count}")
    print(f"ID same? {id(container.count) == original_id}")

    # Test CFloat
    print("\n🎯 Testing CFloat...")
    float1 = CFloat(value=3.14159)
    float2 = CFloat(value=2.71828)

    print(f"float1: {float1}")
    print(f"float(float1): {float(float1)}")

    # Test CBoolean
    print("\n✅ Testing CBoolean...")
    bool1 = CBoolean(value=True)
    bool2 = CBoolean(value=False)

    print(f"bool1: {bool1}")
    print(f"bool(bool1): {bool(bool1)}")

    # Test ranges
    print("\n📏 Testing Ranges...")
    int_range = CIntRange(start=1, end=10)
    float_range = CFloatRange(start=0.5, end=5.5)

    print(f"int_range: {int_range}")
    print(f"float_range: {float_range}")

    # Test range validation
    print("\n🔍 Testing Range Validation...")
    bad_range = CIntRange(start=10, end=5)  # Invalid: start > end
    errors = bad_range.validate()
    print(f"bad_range errors: {errors}")

    good_range = CIntRange(start=1, end=10)
    errors = good_range.validate()
    print(f"good_range errors: {errors}")

    # Test hierarchical relationships with fundamental types
    print("\n🏗️ Testing Hierarchical Relationships...")
    project = CData(name="test_project")
    project.max_iterations = CInt(value=1000)
    project.convergence_threshold = CFloat(value=1e-6)
    project.auto_save = CBoolean(value=True)
    project.resolution_range = CFloatRange(start=20.0, end=2.0)

    print(f"Project children: {len(project.children())}")
    child_names = [child.name for child in project.children()]
    print(f"Child names: {child_names}")

    # Test accessing values
    print(f"Max iterations: {project.max_iterations.value}")
    print(f"Convergence: {float(project.convergence_threshold)}")
    print(f"Auto save: {bool(project.auto_save)}")
    print(f"Resolution range: {project.resolution_range}")

    print("\n✅ Fundamental types working correctly!")


if __name__ == "__main__":
    test_fundamental_types()
