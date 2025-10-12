#!/usr/bin/env python3
"""
Debug the hierarchical setup issue.
"""

from ccp4x.core.data_manager.new_cdata.base_classes import CData


def debug_hierarchy():
    """Debug why hierarchy setup isn't working."""

    print("🐛 DEBUGGING HIERARCHY SETUP")
    print("=" * 35)

    # Create objects
    parent = CData(name="parent")
    child = CData(name="child")

    print(f"Parent children before: {len(parent.children())}")
    print(f"Child parent before: {child.parent}")

    # Test direct assignment
    print("\n🔧 Testing direct assignment...")
    parent.test_child = child

    print(f"Parent children after: {len(parent.children())}")
    print(f"Child parent after: {child.parent}")
    print(f"Child name: {child.name}")

    # Test list assignment
    print("\n📋 Testing list assignment...")
    child1 = CData(name="child1")
    child2 = CData(name="child2")

    print(f"Before list assignment:")
    print(f"  Parent children: {len(parent.children())}")

    parent.children_list = [child1, child2]

    print(f"After list assignment:")
    print(f"  Parent children: {len(parent.children())}")
    print(f"  child1 parent: {child1.parent}")
    print(f"  child1 name: {child1.name}")
    print(f"  child2 parent: {child2.parent}")
    print(f"  child2 name: {child2.name}")


if __name__ == "__main__":
    debug_hierarchy()
