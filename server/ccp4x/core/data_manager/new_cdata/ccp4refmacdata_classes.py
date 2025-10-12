"""Generated classes from CCP4RefmacData.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CRefmacAnomalousAtom(CData):
    """Generated CRefmacAnomalousAtom class from CData metadata."""

    # CONTENTS: <Unparseable: {'atomType': {'class': CCP4Data.CString, 'qualifiers': {'charWidth': 5, 'toolTip': 'Element name as in PDB file'}}, 'Fp': {'class': CCP4Data.CFloat, 'qualifiers': {'toolTip': "Form factor f' for element at given wavelength"}}, 'Fpp': {'class': CCP4Data.CFloat, 'qualifiers': {'toolTip': "Form factor f'' for element at given wavelength"}}}>

class CRefmacRestraintsDataFile(CData):
    """Generated CRefmacRestraintsDataFile class from CData metadata."""
    pass

class CRefmacRigidGroupItem(CData):
    """Generated CRefmacRigidGroupItem class from CData metadata."""

    rigid_group_id: Any = None
    segmentList: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CRefmacRigidGroupList(CData):
    """Generated CRefmacRigidGroupList class from CData metadata."""
    pass

class CRefmacRigidGroupSegment(CData):
    """Generated CRefmacRigidGroupSegment class from CData metadata."""

    chain_id: Any = None
    residue_1: Any = None
    residue_2: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors
