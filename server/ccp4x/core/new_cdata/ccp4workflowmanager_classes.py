"""Generated classes from CCP4WorkflowManager.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CWorkflowDataFlow(CData):
    """Generated CWorkflowDataFlow class from CData metadata."""

    fromJob: Any = None
    fromKey: Any = None
    toKey: Any = None
    annotation: Any = None

class CWorkflowDataFlowList(CData):
    """Generated CWorkflowDataFlowList class from CData metadata."""
    pass

class CWorkflowDefinition(CData):
    """Generated CWorkflowDefinition class from CData metadata."""
    pass

class CWorkflowFileOut(CData):
    """Generated CWorkflowFileOut class from CData metadata."""

    key: Any = None
    className: Any = None

class CWorkflowJobDefinition(CData):
    """Generated CWorkflowJobDefinition class from CData metadata."""

    taskName: Any = None
    input: Any = None
    allOutputFiles: Any = None
    output: Any = None
