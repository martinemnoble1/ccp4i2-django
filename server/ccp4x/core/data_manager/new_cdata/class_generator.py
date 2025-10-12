"""
Generate modern Pythonic CData classes from the enhanced lookup metadata.

This module creates a new class hierarchy where:
- Each CData class becomes a proper Python class
- Instance attributes are created from CONTENTS definitions
- Proper inheritance is used based on immediate_parent relationships
- Type hints and validation are included from QUALIFIERS metadata
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field
import textwrap


@dataclass
class ClassDefinition:
    """Represents a class to be generated."""

    name: str
    immediate_parent: Optional[str]
    base_classes: List[str]
    file_path: str
    docstring: str
    contents: Dict[str, Any] = field(default_factory=dict)
    contents_order: List[str] = field(default_factory=list)
    qualifiers: Dict[str, Any] = field(default_factory=dict)
    qualifiers_order: List[str] = field(default_factory=list)
    qualifiers_definition: Dict[str, Any] = field(default_factory=dict)
    error_codes: Dict[str, Any] = field(default_factory=dict)
    parse_method: str = "AST"


class CDataClassGenerator:
    """Generate modern Python classes from CData metadata."""

    def __init__(self, lookup_file: str, output_dir: str):
        self.lookup_file = lookup_file
        self.output_dir = Path(output_dir)
        self.classes: Dict[str, ClassDefinition] = {}
        self.inheritance_tree: Dict[str, List[str]] = {}  # parent -> children
        self.type_mapping = {
            "CCP4Data.CString": "str",
            "CCP4Data.CInt": "int",
            "CCP4Data.CFloat": "float",
            "CCP4Data.CBoolean": "bool",
            "CCP4Data.CList": "List",
            "CCP4Data.CData": "CData",
            "CCP4File.CDataFile": "CDataFile",
            "CCP4Container.CContainer": "CContainer",
        }

        # Classes that conflict with base classes - skip or rename them
        self.conflicting_classes = {
            "CData",
            "CDataFile",
            "CContainer",
            "CList",
            "CString",
            "CInt",
            "CFloat",
            "CBool",
        }

    def load_metadata(self):
        """Load the enhanced CData class metadata."""
        with open(self.lookup_file, "r") as f:
            data = json.load(f)

        self.classes = {}
        for class_name, class_data in data["classes"].items():
            self.classes[class_name] = ClassDefinition(
                name=class_name,
                immediate_parent=class_data.get("immediate_parent"),
                base_classes=class_data.get("base_classes", []),
                file_path=class_data.get("file_path", ""),
                docstring=class_data.get("docstring", ""),
                contents=class_data.get("CONTENTS", {}),
                contents_order=class_data.get("CONTENTS_ORDER", []),
                qualifiers=class_data.get("QUALIFIERS", {}),
                qualifiers_order=class_data.get("QUALIFIERS_ORDER", []),
                qualifiers_definition=class_data.get("QUALIFIERS_DEFINITION", {}),
                error_codes=class_data.get("ERROR_CODES", {}),
                parse_method=class_data.get("parse_method", "AST"),
            )

        print(f"Loaded {len(self.classes)} class definitions")

    def build_inheritance_tree(self):
        """Build the inheritance hierarchy tree."""
        self.inheritance_tree = {}

        for class_name, class_def in self.classes.items():
            parent = class_def.immediate_parent
            if parent:
                if parent not in self.inheritance_tree:
                    self.inheritance_tree[parent] = []
                self.inheritance_tree[parent].append(class_name)

        print(f"Built inheritance tree with {len(self.inheritance_tree)} parent nodes")

    def get_python_type(self, cdata_type: str) -> str:
        """Convert CData type to Python type annotation."""
        type_mapping = {
            "CString": "str",
            "CInt": "int",
            "CFloat": "float",
            "CBool": "bool",
            "CList": "List[Any]",
            "CDict": "dict",
            "CDataFile": "Any",  # Forward reference
            "CData": "Any",  # Forward reference
        }

        # If it's a CData type we don't recognize, use Any for now
        # This avoids import issues with forward references
        if cdata_type.startswith("C") and cdata_type not in type_mapping:
            return "Any"

        return type_mapping.get(cdata_type, "Any")

    def generate_class_attributes(self, class_def: ClassDefinition) -> List[str]:
        """Generate class attribute definitions from CONTENTS."""
        attributes = []

        if not class_def.contents:
            return attributes

        # Handle case where contents is a string (unparseable)
        if isinstance(class_def.contents, str):
            attributes.append(f"    # CONTENTS: {class_def.contents}")
            return attributes

        # Use CONTENTS_ORDER if available, otherwise use dict order
        field_order = (
            class_def.contents_order
            if class_def.contents_order
            else list(class_def.contents.keys())
        )

        for field_name in field_order:
            if field_name not in class_def.contents:
                continue

            field_info = class_def.contents[field_name]

            # Extract type information
            field_class = field_info.get("class", "Any")
            subitem_class = field_info.get("subItem", {}).get("class", None)
            qualifiers = field_info.get("qualifiers", {})

            # Convert to Python type
            python_type = self.get_python_type(field_class)

            # Generate attribute with type hint and default
            default_value = qualifiers.get("default", "None")
            if isinstance(default_value, str) and default_value != "None":
                default_value = f'"{default_value}"'

            # Add docstring from qualifiers if available
            tooltip = qualifiers.get("toolTip", "")
            if tooltip:
                attributes.append(f"    # {tooltip}")

            attributes.append(f"    {field_name}: {python_type} = {default_value}")

        return attributes

    def generate_class_methods(self, class_def: ClassDefinition) -> List[str]:
        """Generate class methods including validation and error handling."""
        methods = []

        # Add validation method if qualifiers exist
        has_field_qualifiers = False
        if isinstance(class_def.contents, dict):
            has_field_qualifiers = any(
                isinstance(v, dict) and "qualifiers" in v
                for v in class_def.contents.values()
            )

        if class_def.qualifiers or has_field_qualifiers:
            methods.append(
                """
    def validate(self) -> List[str]:
        \"\"\"Validate instance data according to class qualifiers.\"\"\"
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors"""
            )

        # Add error handling if error codes exist
        if class_def.error_codes:
            methods.append(
                f"""
    @classmethod 
    def get_error_message(cls, error_code: int) -> str:
        \"\"\"Get error message for given error code.\"\"\"
        error_codes = {class_def.error_codes}
        return error_codes.get(str(error_code), {{}}).get('description', 'Unknown error')"""
            )

        return methods

    def generate_class_code(self, class_def: ClassDefinition) -> str:
        """Generate complete Python class code."""
        lines = []

        # Determine parent class
        parent_class = "CData"  # Default to CData for all classes
        if class_def.immediate_parent:
            parent_name = (
                class_def.immediate_parent.split(".")[-1]
                if "." in class_def.immediate_parent
                else class_def.immediate_parent
            )
            # Use the immediate parent if it's a known CData type
            if parent_name.startswith("C") and parent_name in [
                "CData",
                "CDataFile",
                "CContainer",
                "CList",
                "CString",
                "CInt",
                "CFloat",
                "CBool",
            ]:
                parent_class = parent_name

        # Class definition
        lines.append(f"class {class_def.name}({parent_class}):")

        # Docstring
        if class_def.docstring:
            docstring = class_def.docstring.replace('"""', r"\"\"\"")
            lines.append(f'    """{docstring}"""')
        else:
            lines.append(
                f'    """Generated {class_def.name} class from CData metadata."""'
            )

        # Class attributes
        attributes = self.generate_class_attributes(class_def)
        if attributes:
            lines.append("")
            lines.extend(attributes)
        else:
            lines.append("    pass")

        # Class methods
        methods = self.generate_class_methods(class_def)
        if methods:
            lines.extend(methods)

        # Add metadata registration
        metadata_init = self.generate_metadata_registration(class_def)
        if metadata_init:
            lines.extend(metadata_init)

        return "\n".join(lines)

    def generate_metadata_registration(self, class_def: ClassDefinition) -> List[str]:
        """Generate metadata registration code for a class."""
        if not isinstance(class_def.contents, dict) or not class_def.contents:
            return []

        lines = []
        lines.append("")
        lines.append("# Register metadata for this class")
        lines.append(
            "from .metadata_system import MetadataRegistry, ClassMetadata, FieldMetadata"
        )
        lines.append("")
        lines.append(f"# Metadata for {class_def.name}")
        lines.append(f"_fields_{class_def.name.lower()} = {{")

        # Generate field metadata
        for field_name, field_info in class_def.contents.items():
            if isinstance(field_info, dict):
                qualifiers = field_info.get("qualifiers", {})

                # Extract metadata properties
                tooltip = qualifiers.get("toolTip", "").replace("'", "\\'")
                default = qualifiers.get("default", "None")
                minlength = qualifiers.get("minlength")
                maxlength = qualifiers.get("maxlength")
                minimum = qualifiers.get("minimum")
                maximum = qualifiers.get("maximum")
                enumerators = qualifiers.get("enumerators")
                menu_text = qualifiers.get("menuText")
                only_enumerators = qualifiers.get("onlyEnumerators", False)

                lines.append(f"    '{field_name}': FieldMetadata(")
                lines.append(f"        name='{field_name}',")
                if tooltip:
                    lines.append(f"        tooltip='{tooltip}',")
                if default != "None":
                    if isinstance(default, str):
                        lines.append(f"        default='{default}',")
                    else:
                        lines.append(f"        default={default},")
                if minlength is not None:
                    lines.append(f"        minlength={minlength},")
                if maxlength is not None:
                    lines.append(f"        maxlength={maxlength},")
                if minimum is not None:
                    lines.append(f"        minimum={minimum},")
                if maximum is not None:
                    lines.append(f"        maximum={maximum},")
                if enumerators:
                    lines.append(f"        enumerators={enumerators},")
                if menu_text:
                    lines.append(f"        menu_text={menu_text},")
                if only_enumerators:
                    lines.append(f"        only_enumerators={only_enumerators},")
                lines.append("    ),")

        lines.append("}")
        lines.append("")
        lines.append(f"_metadata_{class_def.name.lower()} = ClassMetadata(")
        lines.append(f"    name='{class_def.name}',")
        if class_def.docstring:
            docstring = class_def.docstring.replace("'", "\\'").replace("\n", "\\n")
            lines.append(f"    docstring='{docstring}',")
        lines.append(f"    fields=_fields_{class_def.name.lower()},")
        if class_def.immediate_parent:
            lines.append(f"    immediate_parent='{class_def.immediate_parent}',")
        lines.append(")")
        lines.append("")
        lines.append(
            f"MetadataRegistry.register('{class_def.name}', _metadata_{class_def.name.lower()})"
        )

        return lines

    def generate_base_classes(self):
        """Generate the base classes that others will inherit from."""
        base_classes = {
            "CData": '''class CData:
    """Base class for all CData-derived classes."""
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __str__(self):
        return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items())})"
        
    def __repr__(self):
        return self.__str__()''',
            "CDataFile": '''class CDataFile(CData):
    """Base class for file-related CData classes."""
    
    def __init__(self, file_path: str = None, **kwargs):
        super().__init__(**kwargs)
        self.file_path = file_path
        
    def load_from_file(self, file_path: str):
        """Load data from file."""
        self.file_path = file_path
        # TODO: Implement file loading logic
        
    def save_to_file(self, file_path: str = None):
        """Save data to file."""
        path = file_path or self.file_path
        if not path:
            raise ValueError("No file path specified")
        # TODO: Implement file saving logic''',
            "CContainer": '''class CContainer(CData):
    """Base class for container CData classes."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._children = []
        
    def add_child(self, child):
        """Add a child object."""
        self._children.append(child)
        
    def get_children(self):
        """Get all child objects."""
        return self._children[:]''',
        }

        # Write base classes
        base_file = self.output_dir / "base_classes.py"
        with open(base_file, "w") as f:
            f.write('"""Base classes for the new CData hierarchy."""\n\n')
            f.write("from typing import List, Any, Optional\n\n")
            for class_code in base_classes.values():
                f.write(class_code + "\n\n")

        print(f"Generated base classes in {base_file}")

    def generate_all_classes(self):
        """Generate all CData classes organized by hierarchy."""
        self.output_dir.mkdir(exist_ok=True)

        # Generate base classes first
        self.generate_base_classes()

        # Group classes by their source module
        modules = {}
        for class_def in self.classes.values():
            module_name = (
                Path(class_def.file_path).stem if class_def.file_path else "unknown"
            )
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append(class_def)

        # Generate files for each module
        for module_name, class_defs in modules.items():
            output_file = self.output_dir / f"{module_name.lower()}_classes.py"

            with open(output_file, "w") as f:
                # File header
                f.write(f'"""Generated classes from {module_name}.py"""\n\n')
                f.write("from typing import List, Any, Optional\n")
                f.write("from .base_classes import CData, CDataFile, CContainer\n\n")

                # Generate each class (skip conflicts with base classes)
                class_count = 0
                for class_def in sorted(class_defs, key=lambda x: x.name):
                    if class_def.name in self.conflicting_classes:
                        print(f"Skipping {class_def.name} - conflicts with base class")
                        continue

                    # Add proper spacing between classes
                    if class_count > 0:
                        f.write("\n")

                    class_code = self.generate_class_code(class_def)
                    f.write(class_code + "\n")
                    class_count += 1

            print(f"Generated {len(class_defs)} classes in {output_file}")

    def generate_init_file(self):
        """Generate __init__.py file for the package."""
        init_file = self.output_dir / "__init__.py"

        with open(init_file, "w") as f:
            f.write('"""New CData class hierarchy generated from metadata."""\n\n')
            f.write("from .base_classes import CData, CDataFile, CContainer\n\n")

            # Import all generated classes
            py_files = [f for f in self.output_dir.glob("*_classes.py")]
            for py_file in sorted(py_files):
                module_name = py_file.stem
                f.write(f"from .{module_name} import *\n")

            f.write("\n__all__ = [\n")
            f.write('    "CData", "CDataFile", "CContainer",\n')

            # Add all class names
            for class_name in sorted(self.classes.keys()):
                f.write(f'    "{class_name}",\n')

            f.write("]\n")

        print(f"Generated package init file: {init_file}")

    def run(self):
        """Run the complete class generation process."""
        print("Starting CData class generation...")

        # Load and process metadata
        self.load_metadata()
        self.build_inheritance_tree()

        # Generate classes
        self.generate_all_classes()
        self.generate_init_file()

        print(f"\nClass generation complete!")
        print(f"Generated {len(self.classes)} classes in {self.output_dir}")
        print(f"Files created: {list(self.output_dir.glob('*.py'))}")


def main():
    """Main entry point."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python class_generator.py <lookup_json_file> [output_dir]")
        sys.exit(1)

    lookup_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "generated_classes"

    generator = CDataClassGenerator(lookup_file, output_dir)
    generator.run()


if __name__ == "__main__":
    main()
