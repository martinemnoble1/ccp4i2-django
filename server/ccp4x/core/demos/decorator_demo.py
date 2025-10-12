"""
Demonstration of Qt-style @Slot and @Signal decorators for modern Python.

This shows how to use decorators equivalent to Qt's @QtCore.Slot and Signal
for creating type-safe, auto-connecting signal/slot systems.
"""

import sys
import os
import asyncio

# Add the server directory to Python path (4 levels up from this demo file)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from ..base_object.signal_system import (
    Signal,
    Slot,
    SignalDecorator,
    auto_connect_slots,
    get_slots,
    get_signals,
)
from ..base_object.hierarchy_system import HierarchicalObject


class ModernDataModel(HierarchicalObject):
    """
    Example data model class using signal decorators.
    Equivalent to Qt's QAbstractItemModel pattern.
    """

    # Signal declarations using decorators (like Qt signals)
    data_changed = SignalDecorator(dict, name="data_changed")
    rows_inserted = SignalDecorator(int, int, name="rows_inserted")  # start_row, count
    model_reset = SignalDecorator(name="model_reset")

    def __init__(self, parent=None):
        super().__init__(parent, "DataModel")

        # Initialize data
        self._data = []
        self._listeners = []

        # Create actual signals from decorators
        self.data_changed = self.create_signal("data_changed", dict)
        self.rows_inserted = self.create_signal("rows_inserted", dict)
        self.model_reset = self.create_signal("model_reset", type(None))

    def add_item(self, item: dict):
        """Add item to model and emit signals."""
        start_row = len(self._data)
        self._data.append(item)

        # Emit signals
        self.rows_inserted.emit({"start_row": start_row, "count": 1})
        self.data_changed.emit({"action": "insert", "item": item, "row": start_row})

    def update_item(self, row: int, item: dict):
        """Update item and emit change signal."""
        if 0 <= row < len(self._data):
            old_item = self._data[row]
            self._data[row] = item

            self.data_changed.emit(
                {"action": "update", "item": item, "old_item": old_item, "row": row}
            )

    def clear(self):
        """Clear all data."""
        self._data.clear()
        self.model_reset.emit()
        self.data_changed.emit({"action": "clear"})

    def get_item(self, row: int) -> dict:
        """Get item at row."""
        return self._data[row] if 0 <= row < len(self._data) else None

    def row_count(self) -> int:
        """Get number of rows."""
        return len(self._data)


class ModernTableView(HierarchicalObject):
    """
    Example view class using slot decorators.
    Equivalent to Qt's QTableView pattern.
    """

    def __init__(self, model: ModernDataModel = None, parent=None):
        super().__init__(parent, "TableView")

        self._model = None
        self._display_data = []

        # Connect to model if provided
        if model:
            self.set_model(model)

    def set_model(self, model: ModernDataModel):
        """Set the data model and connect signals to slots."""
        if self._model:
            # Disconnect from old model
            self._model.data_changed.disconnect()
            self._model.rows_inserted.disconnect()
            self._model.model_reset.disconnect()

        self._model = model

        # Auto-connect signals to slots
        if model:
            model.data_changed.connect(self.on_data_changed)
            model.rows_inserted.connect(self.on_rows_inserted)
            model.model_reset.connect(self.on_model_reset)

            # Initial refresh
            self.refresh_view()

    @Slot(dict, name="data_changed_handler")
    def on_data_changed(self, change_data: dict):
        """
        Slot for handling data changes.
        Equivalent to Qt's @QtCore.Slot(dict)
        """
        action = change_data.get("action")

        if action == "insert":
            row = change_data.get("row", 0)
            item = change_data.get("item", {})
            self._display_data.insert(row, self._format_item(item))
            print(f"📊 View: Inserted item at row {row}: {item}")

        elif action == "update":
            row = change_data.get("row", 0)
            item = change_data.get("item", {})
            if 0 <= row < len(self._display_data):
                self._display_data[row] = self._format_item(item)
                print(f"📊 View: Updated row {row}: {item}")

        elif action == "clear":
            self._display_data.clear()
            print("📊 View: Cleared all data")

    @Slot(dict, name="rows_inserted_handler")
    def on_rows_inserted(self, insert_data: dict):
        """
        Slot for handling row insertion.
        """
        start_row = insert_data.get("start_row", 0)
        count = insert_data.get("count", 1)
        print(f"📊 View: {count} row(s) inserted at position {start_row}")

    @Slot(name="model_reset_handler")
    def on_model_reset(self):
        """
        Slot for handling model reset.
        """
        print("📊 View: Model reset - refreshing view")
        self.refresh_view()

    @Slot(str, int, result=bool, name="custom_handler")
    def handle_custom_event(self, message: str, code: int) -> bool:
        """
        Example slot with type checking and return value.
        """
        print(f"📊 View: Custom event - {message} (code: {code})")
        return code == 0

    def refresh_view(self):
        """Refresh the entire view from model."""
        self._display_data.clear()

        if self._model:
            for i in range(self._model.row_count()):
                item = self._model.get_item(i)
                if item:
                    self._display_data.append(self._format_item(item))

    def _format_item(self, item: dict) -> str:
        """Format item for display."""
        name = item.get("name", "Unknown")
        value = item.get("value", "")
        return f"{name}: {value}"

    def show_data(self):
        """Display current view data."""
        print(f"📊 TableView Data ({len(self._display_data)} items):")
        for i, display_item in enumerate(self._display_data):
            print(f"   [{i}] {display_item}")


class JobController(HierarchicalObject):
    """
    Example controller that coordinates between model and view.
    Shows automatic signal/slot connection.
    """

    # Controller signals
    job_started = SignalDecorator(str, name="job_started")
    job_finished = SignalDecorator(dict, name="job_finished")

    def __init__(self, parent=None):
        super().__init__(parent, "JobController")

        # Create actual signals
        self.job_started = self.create_signal("job_started", str)
        self.job_finished = self.create_signal("job_finished", dict)

    def start_job(self, job_name: str, parameters: dict):
        """Start a job and emit signal."""
        print(f"🚀 Controller: Starting job '{job_name}'")
        self.job_started.emit(job_name)

        # Simulate job completion
        result = {"job_name": job_name, "status": "completed", "result": parameters}
        self.job_finished.emit(result)

    @Slot(str, name="job_started_handler")
    def on_job_started(self, job_name: str):
        """Handle job start (could be connected from external signal)."""
        print(f"🎯 Controller: Acknowledged job start: {job_name}")

    @Slot(dict, name="job_finished_handler")
    def on_job_finished(self, result: dict):
        """Handle job completion."""
        job_name = result.get("job_name", "Unknown")
        status = result.get("status", "Unknown")
        print(f"✅ Controller: Job '{job_name}' finished with status: {status}")


async def demonstrate_decorators():
    """Demonstrate the signal/slot decorator system."""

    print("🎭 Signal/Slot Decorator Demonstration")
    print("=" * 50)

    # Create MVC components
    model = ModernDataModel()
    view = ModernTableView(model)
    controller = JobController()

    print("\n📋 Slot Discovery:")

    # Show discovered slots
    view_slots = get_slots(view)
    print(f"View slots: {list(view_slots.keys())}")

    controller_slots = get_slots(controller)
    print(f"Controller slots: {list(controller_slots.keys())}")

    print(f"\n📡 Signal Discovery:")

    # Show discovered signals
    model_signals = get_signals(model)
    print(f"Model signals: {list(model_signals.keys())}")

    controller_signals = get_signals(controller)
    print(f"Controller signals: {list(controller_signals.keys())}")

    print(f"\n🔗 Automatic Connection Example:")

    # Auto-connect controller to itself (demo)
    auto_connections = auto_connect_slots(controller, controller)
    print(f"Auto-connected {len(auto_connections)} signal-slot pairs")

    print(f"\n📊 Data Operations:")

    # Add some data to model
    model.add_item({"name": "Refmac Job", "value": "R=0.185", "status": "completed"})
    model.add_item({"name": "Phenix Job", "value": "R=0.192", "status": "running"})
    model.add_item({"name": "Shelx Job", "value": "R=0.201", "status": "queued"})

    # Show current view
    view.show_data()

    print(f"\n🔄 Update Operations:")

    # Update an item
    model.update_item(
        1, {"name": "Phenix Job", "value": "R=0.189", "status": "completed"}
    )

    # Test custom slot with type checking
    try:
        success = view.handle_custom_event("Test message", 0)
        print(f"Custom slot returned: {success}")

        # This should raise TypeError due to type checking
        # view.handle_custom_event(123, "invalid")  # Would fail

    except TypeError as e:
        print(f"Type checking caught error: {e}")

    print(f"\n🚀 Job Controller Demo:")

    # Start some jobs
    controller.start_job("refinement_001", {"cycles": 10, "input": "test.pdb"})
    controller.start_job("validation_001", {"input": "refined.pdb"})

    print(f"\n🧹 Cleanup:")

    # Clear model (triggers reset)
    model.clear()
    view.show_data()

    print(f"\n✅ Decorator demonstration complete!")


if __name__ == "__main__":
    asyncio.run(demonstrate_decorators())
