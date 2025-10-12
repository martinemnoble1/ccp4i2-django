"""Generated classes from CCP4CootData.py"""

from typing import List, Any, Optional
from .base_classes import CDataFile

@cdata_class(
    qualifiers={
        "mimeTypeName": "application/coot-script",
        "mimeTypeDescription": "Coot history/script file",
        "fileExtensions": ['scm', 'py'],
        "fileContentClassName": None,
        "guiLabel": "Coot history",
        "fileLabel": "coot_history",
        "toolTip": "history.scm or 0-state.scm file from Coot",
    }
)
class CCootHistoryDataFile(CDataFile):
    """Generated CCootHistoryDataFile class from CData metadata."""
    pass
