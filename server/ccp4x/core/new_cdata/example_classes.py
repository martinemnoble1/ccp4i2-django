"""Example CData classes using the new decorator-based metadata system.

This file demonstrates how easy it is to define new CData classes with embedded metadata,
making the system much more maintainable than external JSON files.
"""

from .base_classes import CData
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "fullName": attribute(AttributeType.STRING, tooltip="Person's full name"),
        "age": attribute(
            AttributeType.INT, min_value=0, max_value=150, tooltip="Age in years"
        ),
        "email": attribute(AttributeType.STRING, tooltip="Email address"),
        "active": attribute(
            AttributeType.BOOLEAN, default=True, tooltip="Is person active"
        ),
        "salary": attribute(
            AttributeType.FLOAT, min_value=0.0, tooltip="Annual salary"
        ),
    },
    gui_label="Person Record",
)
class CPerson(CData):
    """A person record with validation and metadata."""

    def __init__(self, parent=None, name=None, **kwargs):
        super().__init__(parent=parent, name=name, **kwargs)

    def get_display_name(self) -> str:
        """Get a display-friendly name."""
        return (
            str(self.fullName)
            if hasattr(self, "fullName") and self.fullName.isSet()
            else "Unknown Person"
        )


@cdata_class(
    attributes={
        "fileName": attribute(
            AttributeType.FILEPATH,
            file_extensions=["pdb", "cif", "mmcif"],
            tooltip="Coordinate file path",
        ),
        "resolution": attribute(
            AttributeType.FLOAT,
            min_value=0.5,
            max_value=10.0,
            tooltip="Resolution in Angstroms",
        ),
        "spaceGroup": attribute(AttributeType.STRING, tooltip="Space group symbol"),
        "rWork": attribute(
            AttributeType.FLOAT, min_value=0.0, max_value=1.0, tooltip="R-work value"
        ),
        "rFree": attribute(
            AttributeType.FLOAT, min_value=0.0, max_value=1.0, tooltip="R-free value"
        ),
        "validated": attribute(
            AttributeType.BOOLEAN, default=False, tooltip="Has structure been validated"
        ),
    },
    file_extensions=["pdb", "cif", "mmcif"],
    mime_type="chemical/x-pdb",
    gui_label="Coordinate File",
    error_codes={
        1001: "Invalid coordinate file format",
        1002: "Resolution out of expected range",
        1003: "R-factors are inconsistent",
    },
)
class CCoordinateFile(CData):
    """A crystallographic coordinate file with metadata and validation."""

    def __init__(self, parent=None, name=None, **kwargs):
        super().__init__(parent=parent, name=name, **kwargs)

    def validate_r_factors(self) -> bool:
        """Validate that R-free > R-work (crystallographic requirement)."""
        if (
            hasattr(self, "rWork")
            and hasattr(self, "rFree")
            and self.rWork.isSet()
            and self.rFree.isSet()
        ):
            return float(self.rFree.value) > float(self.rWork.value)
        return True  # Can't validate if values not set

    def get_quality_summary(self) -> str:
        """Get a summary of structure quality."""
        parts = []
        if hasattr(self, "resolution") and self.resolution.isSet():
            parts.append(f"{self.resolution.value}Å resolution")
        if hasattr(self, "rWork") and self.rWork.isSet():
            parts.append(f"R-work={self.rWork.value}")
        if hasattr(self, "rFree") and self.rFree.isSet():
            parts.append(f"R-free={self.rFree.value}")

        return ", ".join(parts) if parts else "No quality metrics available"


@cdata_class(
    attributes={
        "taskName": attribute(AttributeType.STRING, tooltip="Name of the task"),
        "inputFiles": attribute(
            AttributeType.STRING, tooltip="Input file list"
        ),  # Would be a list in real implementation
        "outputFiles": attribute(
            AttributeType.STRING, tooltip="Output file list"
        ),  # Would be a list in real implementation
        "status": attribute(
            AttributeType.STRING,
            default="pending",
            enumerators=["pending", "running", "completed", "failed"],
            tooltip="Current task status",
        ),
        "priority": attribute(
            AttributeType.INT,
            default=5,
            min_value=1,
            max_value=10,
            tooltip="Task priority (1=highest, 10=lowest)",
        ),
        "timeLimit": attribute(
            AttributeType.FLOAT,
            default=3600.0,
            min_value=1.0,
            tooltip="Time limit in seconds",
        ),
        "memoryLimit": attribute(
            AttributeType.INT, default=1024, min_value=64, tooltip="Memory limit in MB"
        ),
    },
    gui_label="Computation Task",
    error_codes={
        2001: "Task configuration is invalid",
        2002: "Input files are missing",
        2003: "Insufficient resources for task",
        2004: "Task execution timeout",
    },
)
class CComputationTask(CData):
    """A computational task with resource limits and status tracking."""

    def __init__(self, parent=None, name=None, **kwargs):
        super().__init__(parent=parent, name=name, **kwargs)

    def is_ready_to_run(self) -> bool:
        """Check if task is ready to execute."""
        # In a real implementation, this would check input files exist, etc.
        return (
            hasattr(self, "taskName")
            and self.taskName.isSet()
            and hasattr(self, "status")
            and str(self.status) == "pending"
        )

    def get_resource_summary(self) -> str:
        """Get summary of resource requirements."""
        time_hrs = (
            float(self.timeLimit.value) / 3600.0
            if hasattr(self, "timeLimit") and self.timeLimit.isSet()
            else 1.0
        )
        mem_gb = (
            float(self.memoryLimit.value) / 1024.0
            if hasattr(self, "memoryLimit") and self.memoryLimit.isSet()
            else 1.0
        )
        priority = (
            int(self.priority.value)
            if hasattr(self, "priority") and self.priority.isSet()
            else 5
        )

        return f"Priority {priority}, {time_hrs:.1f}h limit, {mem_gb:.1f}GB memory"


# Example usage function
def demonstrate_metadata_system():
    """Demonstrate the new metadata system with examples."""
    print("=== Decorator-Based Metadata System Demo ===")
    print()

    # Create a person
    person = CPerson()
    person.fullName.set("Dr. Jane Smith")
    person.age.set(35)
    person.email.set("jane.smith@example.com")
    person.salary.set(95000.50)

    print(f"Person: {person.get_display_name()}")
    print(f"  Age: {person.age} (isSet: {person.age.isSet()})")
    print(f"  Email: {person.email} (isSet: {person.email.isSet()})")
    print(f"  Active: {person.active} (isSet: {person.active.isSet()}) [default value]")
    print()

    # Create a coordinate file
    coord_file = CCoordinateFile()
    coord_file.fileName.set("1abc.pdb")
    coord_file.resolution.set(2.1)
    coord_file.spaceGroup.set("P212121")
    coord_file.rWork.set(0.178)
    coord_file.rFree.set(0.203)

    print(f"Coordinate File: {coord_file.fileName}")
    print(f"  Quality: {coord_file.get_quality_summary()}")
    print(f"  R-factors valid: {coord_file.validate_r_factors()}")
    print()

    # Create a computation task
    task = CComputationTask()
    task.taskName.set("Molecular Replacement")
    task.priority.set(3)
    task.timeLimit.set(7200.0)  # 2 hours
    task.memoryLimit.set(2048)  # 2GB

    print(f"Task: {task.taskName}")
    print(f"  Status: {task.status} (default)")
    print(f"  Resources: {task.get_resource_summary()}")
    print(f"  Ready to run: {task.is_ready_to_run()}")
    print()

    # Show metadata access
    from .class_metadata import get_class_metadata_by_type

    task_metadata = get_class_metadata_by_type(CComputationTask)
    if task_metadata:
        print("Task metadata:")
        print(f"  Attributes: {list(task_metadata.attributes.keys())}")
        print(f"  Error codes: {list(task_metadata.error_codes.keys())}")

    return person, coord_file, task


if __name__ == "__main__":
    demonstrate_metadata_system()
