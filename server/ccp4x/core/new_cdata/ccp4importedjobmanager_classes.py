"""Generated classes from CCP4ImportedJobManager.py"""

from typing import List, Any, Optional
from .base_classes import CContainer, CData, CList
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "name": attribute(AttributeType.CUSTOM, custom_class="COneWord", tooltip="name attribute"),
        "dataType": attribute(AttributeType.CUSTOM, custom_class="CI2DataType", default="CPdbDataFile", tooltip="dataType attribute"),
        "label": attribute(AttributeType.STRING, tooltip="label attribute"),
        "fileName": attribute(AttributeType.CUSTOM, custom_class="CDataFile", tooltip="fileName attribute"),
    },
    gui_label="CImportedJobData",
)
class CImportedJobData(CData):
    """Generated CImportedJobData class from CData metadata."""


    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CImportedJobDataList(CList):
    """Generated CImportedJobDataList class from CData metadata."""
    pass

class CImportedJobDefinition(CContainer):
    """Generated CImportedJobDefinition class from CData metadata."""
    pass
