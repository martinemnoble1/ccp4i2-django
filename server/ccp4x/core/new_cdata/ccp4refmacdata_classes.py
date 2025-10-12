"""Generated classes from CCP4RefmacData.py"""

from typing import List, Optional
from .base_classes import CData, CDataFile
from .fundamental_types import CList
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    gui_label="CRefmacAnomalousAtom"
)
class CRefmacAnomalousAtom(CData):
    """Generated CRefmacAnomalousAtom class from CData metadata."""

    # CONTENTS: <Unparseable: {'atomType': {'class': CCP4Data.CString, 'qualifiers': {'charWidth': 5, 'toolTip': 'Element name as in PDB file'}}, 'Fp': {'class': CCP4Data.CFloat, 'qualifiers': {'toolTip': "Form factor f' for element at given wavelength"}}, 'Fpp': {'class': CCP4Data.CFloat, 'qualifiers': {'toolTip': "Form factor f'' for element at given wavelength"}}}>


@cdata_class(
    qualifiers={
            "fileLabel": "restraints",
            "mimeTypeName": "application/refmac-external-restraints",
            "mimeTypeDescription": "Refmac external restraints",
            "guiLabel": "Additional restraints",
            "fileExtensions": ["txt"],
            "fileContentClassName": "NotImplemented",
        },
    gui_label="CRefmacRestraintsDataFile"
)
class CRefmacRestraintsDataFile(CDataFile):
    """Generated CRefmacRestraintsDataFile class from CData metadata."""

    pass


@cdata_class(
    attributes={
            "rigid_group_id": attribute(AttributeType.STRING, tooltip="rigid_group_id attribute"),
            "segmentList": attribute(AttributeType.STRING, tooltip="segmentList attribute"),
        },
    gui_label="CRefmacRigidGroupItem"
)
class CRefmacRigidGroupItem(CData):
    """Generated CRefmacRigidGroupItem class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    gui_label="CRefmacRigidGroupList"
)
class CRefmacRigidGroupList(CList):
    """Generated CRefmacRigidGroupList class from CData metadata."""

    pass


@cdata_class(
    attributes={
            "chain_id": attribute(AttributeType.STRING, tooltip="chain_id attribute"),
            "residue_1": attribute(AttributeType.INT, tooltip="residue_1 attribute"),
            "residue_2": attribute(AttributeType.INT, tooltip="residue_2 attribute"),
        },
    error_codes={
            "101": "No sequence identity or structure RMS to target set",
        },
    gui_label="CRefmacRigidGroupSegment",
    contents_order=["chain_id", "residue_1", "residue_2"]
)
class CRefmacRigidGroupSegment(CData):
    """Generated CRefmacRigidGroupSegment class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors
