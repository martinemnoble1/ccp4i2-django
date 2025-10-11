"""
Demonstration of hierarchical path-based object access.

This shows how the modern HierarchicalObject class supports Qt-style
dot-separated paths with array indexing, similar to:
- Qt's findChild() with object names
- Configuration file hierarchies 
- Database-like object paths
- File system paths
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from hierarchy_system import HierarchicalObject, DataContainer


def demonstrate_path_system():
    """Demonstrate the hierarchical path system."""
    
    print("🔗 Hierarchical Path System Demonstration")
    print("=" * 50)
    
    # Create a CCP4i2-like object hierarchy
    ccp4_app = DataContainer(name="CCP4i2")
    
    # Project level
    project = DataContainer(parent=ccp4_app, name="MyProject")
    project.set_property("description", "Protein structure refinement")
    project.set_property("created_date", "2025-10-11")
    
    # Jobs container
    jobs = DataContainer(parent=project, name="Jobs") 
    
    # Individual jobs
    refmac_job = DataContainer(parent=jobs, name="Refmac_001")
    refmac_job.set_property("status", "completed")
    refmac_job.set_property("r_factor", 0.185)
    refmac_job.set_property("input_pdb", "input.pdb")
    
    phenix_job = DataContainer(parent=jobs, name="Phenix_001") 
    phenix_job.set_property("status", "running")
    phenix_job.set_property("progress", 0.75)
    
    # Data files
    data_files = DataContainer(parent=project, name="DataFiles")
    
    pdb_file = DataContainer(parent=data_files, name="structure.pdb")
    pdb_file.set_property("size", "2.5MB")
    pdb_file.set_property("atoms", 3456)
    
    mtz_file = DataContainer(parent=data_files, name="reflections.mtz")
    mtz_file.set_property("size", "1.2MB") 
    mtz_file.set_property("resolution", 1.8)
    
    print("📊 Object Hierarchy Created:")
    print_hierarchy(ccp4_app, indent=0)
    
    print("\n🔍 Path-Based Access Examples:")
    
    # 1. Simple path access
    print("\n1. Simple Object Paths:")
    project_found = ccp4_app.find_by_path("MyProject")
    print(f"   Found project: {project_found.name if project_found else 'None'}")
    
    refmac_found = ccp4_app.find_by_path("MyProject.Jobs.Refmac_001")
    print(f"   Found Refmac job: {refmac_found.name if refmac_found else 'None'}")
    
    # 2. Array indexing
    print("\n2. Array Indexing:")
    first_job = ccp4_app.find_by_path("MyProject.Jobs[0]")
    print(f"   First job: {first_job.name if first_job else 'None'}")
    
    second_job = ccp4_app.find_by_path("MyProject.Jobs[1]") 
    print(f"   Second job: {second_job.name if second_job else 'None'}")
    
    first_file = ccp4_app.find_by_path("MyProject.DataFiles[0]")
    print(f"   First data file: {first_file.name if first_file else 'None'}")
    
    # 3. Property access via paths
    print("\n3. Property Access via Paths:")
    r_factor = ccp4_app.get_by_path("MyProject.Jobs.Refmac_001.r_factor")
    print(f"   Refmac R-factor: {r_factor}")
    
    resolution = ccp4_app.get_by_path("MyProject.DataFiles.reflections.mtz.resolution")
    print(f"   MTZ resolution: {resolution}")
    
    progress = ccp4_app.get_by_path("MyProject.Jobs[1].progress")
    print(f"   Second job progress: {progress}")
    
    # 4. Setting values via paths
    print("\n4. Setting Values via Paths:")
    ccp4_app.set_by_path("MyProject.Jobs.Phenix_001.progress", 0.95)
    new_progress = ccp4_app.get_by_path("MyProject.Jobs.Phenix_001.progress")
    print(f"   Updated Phenix progress: {new_progress}")
    
    ccp4_app.set_by_path("MyProject.version", "2.1.0")
    version = ccp4_app.get_by_path("MyProject.version")
    print(f"   Set project version: {version}")
    
    # 5. Object paths
    print("\n5. Object Path Strings:")
    print(f"   CCP4 app path: '{ccp4_app.object_path()}'")
    print(f"   Refmac job path: '{refmac_job.object_path()}'")
    print(f"   PDB file path: '{pdb_file.object_path()}'")
    
    # 6. List all available paths
    print("\n6. Available Paths (depth 3):")
    all_paths = ccp4_app.list_paths(max_depth=3)
    for path in sorted(all_paths)[:15]:  # Show first 15
        value = ccp4_app.get_by_path(path)
        if isinstance(value, HierarchicalObject):
            print(f"   {path} -> {value.__class__.__name__}({value.name})")
        else:
            print(f"   {path} -> {value}")
    
    if len(all_paths) > 15:
        print(f"   ... and {len(all_paths) - 15} more paths")
    
    # 7. Practical CCP4i2 use cases
    print("\n🎯 Practical CCP4i2 Use Cases:")
    
    # Job status monitoring
    def get_job_status(job_path: str) -> str:
        return ccp4_app.get_by_path(f"{job_path}.status", "unknown")
    
    print(f"   Refmac status: {get_job_status('MyProject.Jobs.Refmac_001')}")
    print(f"   Phenix status: {get_job_status('MyProject.Jobs.Phenix_001')}")
    
    # File size reporting
    def get_file_info(file_path: str) -> dict:
        return {
            'size': ccp4_app.get_by_path(f"{file_path}.size"),
            'name': ccp4_app.find_by_path(file_path).name if ccp4_app.find_by_path(file_path) else None
        }
    
    pdb_info = get_file_info("MyProject.DataFiles.structure.pdb")
    print(f"   PDB info: {pdb_info}")
    
    # Batch operations
    print(f"\n   All job statuses:")
    jobs_obj = ccp4_app.find_by_path("MyProject.Jobs")
    if jobs_obj:
        for i, job in enumerate(jobs_obj.children()):
            status = job.get_property("status", "unknown")
            print(f"     Job[{i}] {job.name}: {status}")
    
    print("\n✅ Path system demonstration complete!")


def print_hierarchy(obj: HierarchicalObject, indent: int = 0):
    """Print the object hierarchy tree."""
    prefix = "  " * indent
    properties = []
    
    for prop_name in obj.property_names():
        prop_value = obj.get_property(prop_name)
        if isinstance(prop_value, (str, int, float)):
            properties.append(f"{prop_name}={prop_value}")
    
    prop_str = f" ({', '.join(properties)})" if properties else ""
    print(f"{prefix}├─ {obj.name}{prop_str}")
    
    for child in obj.children():
        print_hierarchy(child, indent + 1)


if __name__ == "__main__":
    demonstrate_path_system()