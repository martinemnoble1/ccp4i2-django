"""Generated classes from CCP4CustomTaskManager.py"""

from typing import List, Any, Optional
from .base_classes import CContainer, CData, CString
from .fundamental_types import CList
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "text": attribute(AttributeType.STRING, tooltip="text attribute"),
        "name": attribute(
            AttributeType.STRING, default="./com.txt", tooltip="name attribute"
        ),
    },
    gui_label="CCustomComFile",
)
class CCustomComFile(CData):
    """Generated CCustomComFile class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(gui_label="CCustomComFileList")
class CCustomComFileList(CList):
    """Generated CCustomComFileList class from CData metadata."""

    pass


@cdata_class(gui_label="CCustomTaskDefinition")
class CCustomTaskDefinition(CContainer):
    """Generated CCustomTaskDefinition class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "enumerators": ["unknown", "input", "output", "control parameter", "log"],
    }
)
class CCustomTaskFileFunction(CString):
    """Generated CCustomTaskFileFunction class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "dataType": attribute(AttributeType.STRING, tooltip="dataType attribute"),
        "label": attribute(AttributeType.STRING, tooltip="label attribute"),
        "obligatory": attribute(AttributeType.BOOLEAN, tooltip="obligatory attribute"),
        "saveDataToDb": attribute(AttributeType.BOOLEAN, tooltip="saveDataToDb attribute"),
        "function": attribute(AttributeType.STRING, tooltip="function attribute"),
        "mergeTo": attribute(AttributeType.STRING, tooltip="mergeTo attribute"),
        "splitColumns": attribute(
            AttributeType.STRING, tooltip="splitColumns attribute"
        ),
        "requiredContentType": attribute(
            AttributeType.STRING, tooltip="requiredContentType attribute"
        ),
        "outputFilePath": attribute(
            AttributeType.STRING, tooltip="outputFilePath attribute"
        ),
    },
    gui_label="CCustomTaskParam",
)
class CCustomTaskParam(CData):
    """Generated CCustomTaskParam class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(gui_label="CCustomTaskParamList")
class CCustomTaskParamList(CList):
    """Generated CCustomTaskParamList class from CData metadata."""

    pass
