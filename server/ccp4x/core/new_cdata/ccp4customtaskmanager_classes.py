"""Generated classes from CCP4CustomTaskManager.py"""

from typing import List, Any, Optional
from .base_classes import CData
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "text": attribute(AttributeType.STRING, tooltip="text attribute"),
        "name": attribute(AttributeType.STRING, default="./com.txt", tooltip="name attribute"),
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

class CCustomComFileList(CData):
    """Generated CCustomComFileList class from CData metadata."""
    pass

class CCustomTaskDefinition(CData):
    """Generated CCustomTaskDefinition class from CData metadata."""
    pass

class CCustomTaskFileFunction(CData):
    """Generated CCustomTaskFileFunction class from CData metadata."""
    pass


@cdata_class(
    attributes={
        "name": attribute(AttributeType.CUSTOM, custom_class="COneWord", tooltip="name attribute"),
        "dataType": attribute(AttributeType.CUSTOM, custom_class="CI2DataType", default="CPdbDataFile", tooltip="dataType attribute"),
        "label": attribute(AttributeType.STRING, tooltip="label attribute"),
        "obligatory": attribute(AttributeType.BOOLEAN, default=True, tooltip="obligatory attribute"),
        "saveDataToDb": attribute(AttributeType.BOOLEAN, default=False, tooltip="saveDataToDb attribute"),
        "function": attribute(AttributeType.CUSTOM, custom_class="CCustomTaskFileFunction", default="input", tooltip="function attribute"),
        "mergeTo": attribute(AttributeType.STRING, tooltip="mergeTo attribute"),
        "splitColumns": attribute(AttributeType.STRING, tooltip="splitColumns attribute"),
        "requiredContentType": attribute(AttributeType.CUSTOM, custom_class="CList", tooltip="requiredContentType attribute"),
        "outputFilePath": attribute(AttributeType.STRING, tooltip="outputFilePath attribute"),
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

class CCustomTaskParamList(CData):
    """Generated CCustomTaskParamList class from CData metadata."""
    pass
