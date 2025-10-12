"""Generated classes from CCP4PerformanceData.py"""

from typing import List, Any, Optional
from .base_classes import CData
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
            "value": attribute(AttributeType.FLOAT, tooltip="value attribute"),
            "annotation": attribute(AttributeType.STRING, tooltip="annotation attribute"),
        },
    gui_label="CPerformanceIndicator",
    contents_order=["value", "annotation"]
)
class CPerformanceIndicator(CData):
    """Generated CPerformanceIndicator class from CData metadata."""


    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors
