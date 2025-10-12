"""Generated classes from CCP4CustomTaskManager.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CCustomComFile(CData):
    """Generated CCustomComFile class from CData metadata."""

    text: Any = None
    name: Any = "./com.txt"

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

class CCustomTaskParam(CData):
    """Generated CCustomTaskParam class from CData metadata."""

    name: Any = None
    dataType: Any = "CPdbDataFile"
    label: Any = None
    obligatory: Any = True
    saveDataToDb: Any = False
    function: Any = "input"
    mergeTo: Any = None
    splitColumns: Any = None
    requiredContentType: Any = None
    outputFilePath: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CCustomTaskParamList(CData):
    """Generated CCustomTaskParamList class from CData metadata."""
    pass
