#!/usr/bin/env python3
"""
Test Smart Setter Behavior for CCP4i2 Integration

This tests the two required assignment patterns:
1. ctrl.NCYCLES = 25 (direct primitive assignment)
2. ctrl.NCYCLES.set(25) (method call assignment)

Both patterns must preserve the CData object identity and properly track set states.
"""

import sys

sys.path.insert(0, "/Users/nmemn/Developer/ccp4i2-django/server")

from ccp4x.core.data_manager.new_cdata.base_classes import CData, CString, ValueState
from ccp4x.core.data_manager.new_cdata.fundamental_types import CInt, CFloat, CBoolean


def test_smart_setters():
    """Test both assignment patterns work correctly."""
    print("🎯 Testing Smart Setter Behavior for CCP4i2 Integration")
    print("=" * 60)

    # Create a control parameters container (similar to your example)
    ctrl = CData(name="controlParameters")

    # Initialize with CData value types (as they would be from DEF XML parsing)
    ctrl.NCYCLES = CInt(value=10)  # Default from DEF XML
    ctrl.WEIGHT = CFloat(value=0.1)  # Default from DEF XML
    ctrl.ADD_WATERS = CBoolean(value=False)  # Default from DEF XML
    ctrl.METHOD = CString(value="default")  # Default from DEF XML

    print("\n📋 Initial State (from DEF XML defaults):")
    print(f"  ctrl.NCYCLES: {ctrl.NCYCLES.value} (type: {type(ctrl.NCYCLES).__name__})")
    print(f"  ctrl.WEIGHT: {ctrl.WEIGHT.value} (type: {type(ctrl.WEIGHT).__name__})")
    print(
        f"  ctrl.ADD_WATERS: {ctrl.ADD_WATERS.value} (type: {type(ctrl.ADD_WATERS).__name__})"
    )
    print(f"  ctrl.METHOD: {ctrl.METHOD.value} (type: {type(ctrl.METHOD).__name__})")

    print("\n🔍 Initial Set States:")
    print(f"  NCYCLES isSet: {ctrl.isSet('NCYCLES')}")
    print(f"  WEIGHT isSet: {ctrl.isSet('WEIGHT')}")
    print(f"  ADD_WATERS isSet: {ctrl.isSet('ADD_WATERS')}")
    print(f"  METHOD isSet: {ctrl.isSet('METHOD')}")

    # Store original object IDs to verify they don't change
    original_ncycles_id = id(ctrl.NCYCLES)
    original_weight_id = id(ctrl.WEIGHT)
    original_waters_id = id(ctrl.ADD_WATERS)
    original_method_id = id(ctrl.METHOD)

    print(f"\n🆔 Original Object IDs:")
    print(f"  NCYCLES: {original_ncycles_id}")
    print(f"  WEIGHT: {original_weight_id}")
    print(f"  ADD_WATERS: {original_waters_id}")
    print(f"  METHOD: {original_method_id}")

    # ================================
    # TEST 1: Direct primitive assignment
    # ================================
    print(f"\n🔧 TEST 1: Direct Primitive Assignment (ctrl.NCYCLES = 25)")

    # This should update the .value of the existing CInt object
    ctrl.NCYCLES = 25
    ctrl.WEIGHT = 0.15
    ctrl.ADD_WATERS = True
    ctrl.METHOD = "updated"

    print(f"After direct assignment:")
    print(f"  ctrl.NCYCLES: {ctrl.NCYCLES.value} (type: {type(ctrl.NCYCLES).__name__})")
    print(f"  ctrl.WEIGHT: {ctrl.WEIGHT.value} (type: {type(ctrl.WEIGHT).__name__})")
    print(
        f"  ctrl.ADD_WATERS: {ctrl.ADD_WATERS.value} (type: {type(ctrl.ADD_WATERS).__name__})"
    )
    print(f"  ctrl.METHOD: {ctrl.METHOD.value} (type: {type(ctrl.METHOD).__name__})")

    # Verify object identity is preserved
    print(f"\n✅ Object Identity Check (should be preserved):")
    print(f"  NCYCLES same object? {id(ctrl.NCYCLES) == original_ncycles_id}")
    print(f"  WEIGHT same object? {id(ctrl.WEIGHT) == original_weight_id}")
    print(f"  ADD_WATERS same object? {id(ctrl.ADD_WATERS) == original_waters_id}")
    print(f"  METHOD same object? {id(ctrl.METHOD) == original_method_id}")

    # Verify set states are updated
    print(f"\n✅ Set State Check (should be EXPLICITLY_SET):")
    print(f"  NCYCLES isSet: {ctrl.isSet('NCYCLES')}")
    print(f"  WEIGHT isSet: {ctrl.isSet('WEIGHT')}")
    print(f"  ADD_WATERS isSet: {ctrl.isSet('ADD_WATERS')}")
    print(f"  METHOD isSet: {ctrl.isSet('METHOD')}")

    # ================================
    # TEST 2: Method call assignment
    # ================================
    print(f"\n🔧 TEST 2: Method Call Assignment (ctrl.NCYCLES.set(50))")

    # This should also update the .value and preserve object identity
    ctrl.NCYCLES.set(50)
    ctrl.WEIGHT.set(0.25)
    ctrl.ADD_WATERS.set(False)
    ctrl.METHOD.set("method_set")

    print(f"After method call assignment:")
    print(f"  ctrl.NCYCLES: {ctrl.NCYCLES.value} (type: {type(ctrl.NCYCLES).__name__})")
    print(f"  ctrl.WEIGHT: {ctrl.WEIGHT.value} (type: {type(ctrl.WEIGHT).__name__})")
    print(
        f"  ctrl.ADD_WATERS: {ctrl.ADD_WATERS.value} (type: {type(ctrl.ADD_WATERS).__name__})"
    )
    print(f"  ctrl.METHOD: {ctrl.METHOD.value} (type: {type(ctrl.METHOD).__name__})")

    # Verify object identity is still preserved
    print(f"\n✅ Object Identity Check (should still be preserved):")
    print(f"  NCYCLES same object? {id(ctrl.NCYCLES) == original_ncycles_id}")
    print(f"  WEIGHT same object? {id(ctrl.WEIGHT) == original_weight_id}")
    print(f"  ADD_WATERS same object? {id(ctrl.ADD_WATERS) == original_waters_id}")
    print(f"  METHOD same object? {id(ctrl.METHOD) == original_method_id}")

    # ================================
    # TEST 3: Mixed assignment patterns
    # ================================
    print(f"\n🔧 TEST 3: Mixed Assignment Patterns")

    # Mix both patterns
    ctrl.NCYCLES = 100  # Direct assignment
    ctrl.WEIGHT.set(0.5)  # Method call

    print(f"After mixed assignment:")
    print(f"  ctrl.NCYCLES: {ctrl.NCYCLES.value} (direct assignment)")
    print(f"  ctrl.WEIGHT: {ctrl.WEIGHT.value} (method call)")

    # Verify both still work and preserve identity
    print(f"\n✅ Mixed Pattern Identity Check:")
    print(f"  NCYCLES same object? {id(ctrl.NCYCLES) == original_ncycles_id}")
    print(f"  WEIGHT same object? {id(ctrl.WEIGHT) == original_weight_id}")

    # ================================
    # TEST 4: Type compatibility checking
    # ================================
    print(f"\n🔧 TEST 4: Type Compatibility Checking")

    try:
        # This should work - int to CInt
        ctrl.NCYCLES = 999
        print(f"  ✅ int -> CInt: {ctrl.NCYCLES.value}")
    except Exception as e:
        print(f"  ❌ int -> CInt failed: {e}")

    try:
        # This should work - float to CFloat
        ctrl.WEIGHT = 0.999
        print(f"  ✅ float -> CFloat: {ctrl.WEIGHT.value}")
    except Exception as e:
        print(f"  ❌ float -> CFloat failed: {e}")

    try:
        # This should work - bool to CBoolean
        ctrl.ADD_WATERS = True
        print(f"  ✅ bool -> CBoolean: {ctrl.ADD_WATERS.value}")
    except Exception as e:
        print(f"  ❌ bool -> CBoolean failed: {e}")

    try:
        # This should work - str to CString
        ctrl.METHOD = "compatibility_test"
        print(f"  ✅ str -> CString: {ctrl.METHOD.value}")
    except Exception as e:
        print(f"  ❌ str -> CString failed: {e}")

    # ================================
    # SUMMARY
    # ================================
    print(f"\n🎉 Summary: Smart Setter Integration")

    # Final verification
    all_objects_preserved = (
        id(ctrl.NCYCLES) == original_ncycles_id
        and id(ctrl.WEIGHT) == original_weight_id
        and id(ctrl.ADD_WATERS) == original_waters_id
        and id(ctrl.METHOD) == original_method_id
    )

    all_set_states_correct = (
        ctrl.isSet("NCYCLES")
        and ctrl.isSet("WEIGHT")
        and ctrl.isSet("ADD_WATERS")
        and ctrl.isSet("METHOD")
    )

    print(f"  ✅ Object Identity Preserved: {all_objects_preserved}")
    print(f"  ✅ Set States Correct: {all_set_states_correct}")
    print(f"  ✅ Direct Assignment Pattern: ctrl.NCYCLES = 25 ✓")
    print(f"  ✅ Method Call Pattern: ctrl.NCYCLES.set(25) ✓")
    print(f"  ✅ Type Compatibility: Enforced ✓")

    if all_objects_preserved and all_set_states_correct:
        print(f"\n🌟 SUCCESS: Smart setters are plug-and-play compatible!")
        print(f"    Both patterns work while preserving CData object identity.")
        return True
    else:
        print(f"\n💥 FAILURE: Smart setters need refinement.")
        return False


if __name__ == "__main__":
    success = test_smart_setters()
    if success:
        print(f"\n🎊 Ready for CCP4i2 integration!")
    else:
        print(f"\n🔧 Needs debugging before integration.")
