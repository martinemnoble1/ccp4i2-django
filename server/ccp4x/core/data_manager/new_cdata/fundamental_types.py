"""Fundamental CCP4i2 data types that form the base of the type system."""

from typing import List, Any, Optional, Union
from .base_classes import CData


class CInt(CData):
    """Integer value type."""

    def __init__(self, value: int = 0, parent=None, name=None, **kwargs):
        super().__init__(parent=parent, name=name, **kwargs)
        # Set the value after initialization to properly track set state
        self.value = value

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def _is_value_type(self) -> bool:
        return True


class CFloat(CData):
    """Float value type."""

    def __init__(self, value: float = 0.0, parent=None, name=None, **kwargs):
        super().__init__(parent=parent, name=name, **kwargs)
        # Set the value after initialization to properly track set state
        self.value = value

    def __str__(self):
        return str(self.value)

    def __float__(self):
        return float(self.value)

    def _is_value_type(self) -> bool:
        return True


class CBoolean(CData):
    """Boolean value type."""

    def __init__(self, value: bool = False, parent=None, name=None, **kwargs):
        super().__init__(parent=parent, name=name, **kwargs)
        # Set the value after initialization to properly track set state
        self.value = value

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        return bool(self.value)

    def _is_value_type(self) -> bool:
        return True


class CRange(CData):
    """Base class for range types."""

    def __init__(self, parent=None, name=None, **kwargs):
        super().__init__(parent=parent, name=name, **kwargs)


class CIntRange(CRange):
    """Integer range type."""

    def __init__(self, start: int = 0, end: int = 0, parent=None, name=None, **kwargs):
        self.start = start
        self.end = end
        super().__init__(parent=parent, name=name, **kwargs)

    def __str__(self):
        return f"{self.start}-{self.end}"

    def validate(self) -> List[str]:
        """Validate the range."""
        errors = []
        if self.start > self.end:
            errors.append("Start value cannot be greater than end value")
        return errors


class CFloatRange(CRange):
    """Float range type."""

    def __init__(
        self, start: float = 0.0, end: float = 0.0, parent=None, name=None, **kwargs
    ):
        self.start = start
        self.end = end
        super().__init__(parent=parent, name=name, **kwargs)

    def __str__(self):
        return f"{self.start}-{self.end}"

    def validate(self) -> List[str]:
        """Validate the range."""
        errors = []
        if self.start > self.end:
            errors.append("Start value cannot be greater than end value")
        return errors


# Import CString from base_classes
from .base_classes import CString

# Type aliases for commonly used types
CCellLength = CFloat
CCellAngle = CFloat
CWavelength = CFloat
CAngle = CFloat
CTime = CInt
CSpaceGroup = CString
CUUID = CString
CProjectId = CUUID
CUserId = CString
CVersion = CString
CProjectName = CString
CDatasetName = CString
CFilePath = CString
CHostName = CString
CJobStatus = CInt


class CList(CData):
    """List container type for collections of CData objects."""

    def __init__(
        self, items: Optional[List[Any]] = None, parent=None, name=None, **kwargs
    ):
        super().__init__(parent=parent, name=name, **kwargs)
        self._items = items or []
        self._item_type = None
        self._item_qualifiers = {}

        # Register existing items as children
        for i, item in enumerate(self._items):
            if isinstance(item, CData):
                item.set_parent(self)
                item.name = f"{self.name}[{i}]"

    def append(self, item: Any) -> None:
        """Add an item to the list."""
        index = len(self._items)

        # If item is CData, register as child
        if isinstance(item, CData):
            item.set_parent(self)
            item.name = f"{self.name}[{index}]"

        self._items.append(item)

        # Mark as explicitly set
        self._value_states["_items"] = self.ValueState.EXPLICITLY_SET

    def insert(self, index: int, item: Any) -> None:
        """Insert an item at specified index."""
        if isinstance(item, CData):
            item.set_parent(self)
            item.name = f"{self.name}[{index}]"

        self._items.insert(index, item)

        # Update names of subsequent items
        for i in range(index + 1, len(self._items)):
            if isinstance(self._items[i], CData):
                self._items[i].name = f"{self.name}[{i}]"

        # Mark as explicitly set
        self._value_states["_items"] = self.ValueState.EXPLICITLY_SET

    def remove(self, item: Any) -> None:
        """Remove an item from the list."""
        index = self._items.index(item)
        self._items.remove(item)

        # Update names of subsequent items
        for i in range(index, len(self._items)):
            if isinstance(self._items[i], CData):
                self._items[i].name = f"{self.name}[{i}]"

        # Mark as explicitly set
        self._value_states["_items"] = self.ValueState.EXPLICITLY_SET

    def pop(self, index: int = -1) -> Any:
        """Remove and return item at index."""
        item = self._items.pop(index)

        # Update names of subsequent items if needed
        if index >= 0:
            for i in range(index, len(self._items)):
                if isinstance(self._items[i], CData):
                    self._items[i].name = f"{self.name}[{i}]"

        # Mark as explicitly set
        self._value_states["_items"] = self.ValueState.EXPLICITLY_SET
        return item

    def clear(self) -> None:
        """Remove all items from the list."""
        self._items.clear()
        self._value_states["_items"] = self.ValueState.EXPLICITLY_SET

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if isinstance(value, CData):
            value.set_parent(self)
            value.name = f"{self.name}[{index}]"

        self._items[index] = value
        self._value_states["_items"] = self.ValueState.EXPLICITLY_SET

    def __iter__(self):
        return iter(self._items)

    def __contains__(self, item: Any) -> bool:
        return item in self._items

    def __str__(self) -> str:
        return f"CList({len(self._items)} items)"

    def __repr__(self) -> str:
        return f"CList({self._items!r})"


# String type aliases
CJobTitle = CString
CRangeSelection = CString
CExperimentalDataType = CString
CFileFunction = CString
CI2DataType = CString
CCustomTaskFileFunction = CString
CCrystalName = CString
CShelxLabel = CString
CSequenceString = CString
