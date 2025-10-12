"""Generated classes from CCP4WorkflowManager.py"""

from typing import List, Any, Optional
from .base_classes import CContainer, CData, CList
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "fromJob": attribute(AttributeType.STRING, tooltip="fromJob attribute"),
        "fromKey": attribute(AttributeType.STRING, tooltip="fromKey attribute"),
        "toKey": attribute(AttributeType.STRING, tooltip="toKey attribute"),
        "annotation": attribute(AttributeType.STRING, tooltip="annotation attribute"),
    },
    gui_label="CWorkflowDataFlow",
)
@cdata_class(
    attributes={
            "fromJob": attribute(AttributeType.STRING, tooltip="fromJob attribute"),
            "fromKey": attribute(AttributeType.STRING, tooltip="fromKey attribute"),
            "toKey": attribute(AttributeType.STRING, tooltip="toKey attribute"),
            "annotation": attribute(AttributeType.STRING, tooltip="annotation attribute"),
        },
    gui_label="CWorkflowDataFlow"
)
class CWorkflowDataFlow(CData):
    """Generated CWorkflowDataFlow class from CData metadata."""


@cdata_class(
    gui_label="CWorkflowDataFlowList"
)
class CWorkflowDataFlowList(CList):
    """Generated CWorkflowDataFlowList class from CData metadata."""
    pass

@cdata_class(
    gui_label="CWorkflowDefinition"
)
class CWorkflowDefinition(CContainer):
    """Generated CWorkflowDefinition class from CData metadata."""
    pass


@cdata_class(
    attributes={
        "key": attribute(AttributeType.STRING, tooltip="key attribute"),
        "className": attribute(AttributeType.STRING, tooltip="className attribute"),
    },
    gui_label="CWorkflowFileOut",
)
class CWorkflowFileOut(CData):
    """Generated CWorkflowFileOut class from CData metadata."""



@cdata_class(
    attributes={
        "taskName": attribute(AttributeType.STRING, tooltip="taskName attribute"),
        "input": attribute(AttributeType.CUSTOM, custom_class="CWorkflowDataFlowList", tooltip="input attribute"),
        "allOutputFiles": attribute(AttributeType.CUSTOM, custom_class="CList", tooltip="allOutputFiles attribute"),
        "output": attribute(AttributeType.CUSTOM, custom_class="CWorkflowDataFlowList", tooltip="output attribute"),
    },
    gui_label="CWorkflowJobDefinition",
)
@cdata_class(
    attributes={
            "taskName": attribute(AttributeType.STRING, tooltip="taskName attribute"),
            "input": attribute(AttributeType.STRING, tooltip="input attribute"),
            "allOutputFiles": attribute(AttributeType.STRING, tooltip="allOutputFiles attribute"),
            "output": attribute(AttributeType.STRING, tooltip="output attribute"),
        },
    gui_label="CWorkflowJobDefinition"
)
class CWorkflowJobDefinition(CData):
    """Generated CWorkflowJobDefinition class from CData metadata."""

