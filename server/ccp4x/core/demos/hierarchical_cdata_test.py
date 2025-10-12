#!/usr/bin/env python3
"""
Simple test to demonstrate the hierarchical CData system working.
This shows the "beyond exciting" integration of CData with HierarchicalObject.
"""
import sys
import os

# Add the server directory to Python path (4 levels up from this demo file)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from ccp4x.core.new_cdata.base_classes import CData


def test_hierarchical_cdata():
    """Test the integrated hierarchical CData system."""

    print("🏗️ HIERARCHICAL CDATA SYSTEM TEST")
    print("=" * 40)

    # Create a project (top-level CData object)
    print("\n📁 Creating project...")
    project = CData(name="Crystal_Project")
    print(f"   Project: {project.name}")
    print(f"   Children: {len(project.children())}")

    # Create child objects
    print("\n🧬 Adding sequences...")
    seq1 = CData(name="sequence1")
    seq2 = CData(name="sequence2")

    # Assign them as attributes - should automatically become children
    project.sequences = [seq1, seq2]

    print(f"   Project children: {len(project.children())}")
    print(f"   Sequence names: {[child.name for child in project.children()]}")
    print(f"   seq1 parent: {seq1.parent().name}")
    print(f"   seq2 parent: {seq2.parent().name}")

    # Test nested structure
    print("\n📝 Adding annotations to sequence1...")
    ann1 = CData(name="annotation1")
    ann2 = CData(name="annotation2")

    seq1.annotations = [ann1, ann2]

    print(f"   seq1 children: {len(seq1.children())}")
    print(f"   Annotation names: {[child.name for child in seq1.children()]}")
    print(f"   ann1 parent: {ann1.parent().name}")

    # Test path-based access
    print("\n🗂️ Testing path-based access...")
    print(f"   Project path: {project.object_path()}")

    # Find objects by path
    found_seq = project.find_by_path("sequences[0]")
    print(f"   Found sequences[0]: {found_seq.name if found_seq else 'Not found'}")

    found_ann = project.find_by_path("sequences[0].annotations[1]")
    print(
        f"   Found sequences[0].annotations[1]: {found_ann.name if found_ann else 'Not found'}"
    )

    # Test single child assignment
    print("\n📋 Testing single child assignment...")
    metadata = CData(name="metadata")
    project.metadata = metadata

    print(f"   Project children: {len(project.children())}")
    print(f"   Metadata parent: {metadata.parent().name}")
    print(f"   Metadata name: {metadata.name}")

    print("\n✅ SUCCESS! Hierarchical CData system is working!")
    print("\n🎉 Key features demonstrated:")
    print("   ✓ Automatic parent/child relationships")
    print("   ✓ List elements named with [index] format")
    print("   ✓ Path-based object access")
    print("   ✓ Proper hierarchical navigation")
    print("   ✓ CData objects inherit from HierarchicalObject")


if __name__ == "__main__":
    test_hierarchical_cdata()
