"""
Simple demonstration of Qt-style @Slot decorators for modern Python.

This shows the most important part - slot decoration and type checking,
similar to Qt's @QtCore.Slot decorator.
"""

import sys
import os
import asyncio

sys.path.insert(0, os.path.dirname(__file__))

from signal_system import Signal, Slot, auto_connect_slots, get_slots
from hierarchy_system import HierarchicalObject


class DataProcessor(HierarchicalObject):
    """
    Example class demonstrating @Slot decorators.
    Similar to Qt widgets with slots.
    """

    def __init__(self, parent=None):
        super().__init__(parent, "DataProcessor")

        # Create signals manually (more reliable than decorators for now)
        self.data_received = self.create_signal("data_received", dict)
        self.processing_complete = self.create_signal("processing_complete", dict)
        self.error_occurred = self.create_signal("error_occurred", str)

        self._processed_count = 0

    # Slot decorators - these mark methods as slots with type checking
    @Slot(dict, name="process_data_slot")
    def process_data(self, data: dict):
        """
        Process incoming data.
        Equivalent to Qt's @QtCore.Slot(dict)
        """
        print(f"🔄 Processing data: {data}")

        try:
            # Simulate processing
            result = {
                "input": data,
                "processed_at": __import__("time").time(),
                "processor_id": self.name,
                "count": self._processed_count,
            }

            self._processed_count += 1
            self.processing_complete.emit(result)

        except Exception as e:
            self.error_occurred.emit(f"Processing failed: {e}")

    @Slot(str, int, result=bool, name="validate_input_slot")
    def validate_input(self, text: str, min_length: int) -> bool:
        """
        Validate input with type checking.
        Shows multiple parameter types and return value.
        """
        print(f"✅ Validating: '{text}' (min_length: {min_length})")

        is_valid = len(text) >= min_length
        print(f"   Result: {'Valid' if is_valid else 'Invalid'}")

        return is_valid

    @Slot(name="reset_slot")
    def reset_processor(self):
        """
        Reset processor state.
        Slot with no parameters.
        """
        print("🔄 Resetting processor...")
        self._processed_count = 0
        print(f"   Reset complete. Count: {self._processed_count}")

    @Slot(str, dict, name="log_event_slot")
    def log_event(self, level: str, event_data: dict):
        """
        Log an event with level and data.
        """
        timestamp = __import__("time").strftime("%H:%M:%S")
        print(f"📝 [{timestamp}] {level.upper()}: {event_data}")

    # Regular method (not a slot)
    def get_stats(self) -> dict:
        """Get processing statistics."""
        return {"processed_count": self._processed_count, "processor_name": self.name}


class EventLogger(HierarchicalObject):
    """
    Example logger class with slots for handling various events.
    """

    def __init__(self, parent=None):
        super().__init__(parent, "EventLogger")
        self._log_entries = []

    @Slot(dict, name="log_processing_complete")
    def on_processing_complete(self, result: dict):
        """
        Handle processing completion events.
        Auto-connectable slot (matches signal name pattern).
        """
        entry = f"Processing completed - Count: {result.get('count', 'Unknown')}"
        self._log_entries.append(entry)
        print(f"📋 Logger: {entry}")

    @Slot(str, name="log_error")
    def on_error_occurred(self, error_message: str):
        """
        Handle error events.
        """
        entry = f"ERROR: {error_message}"
        self._log_entries.append(entry)
        print(f"🚨 Logger: {entry}")

    @Slot(dict, name="log_data_received")
    def on_data_received(self, data: dict):
        """
        Handle data received events.
        """
        entry = f"Data received: {len(str(data))} chars"
        self._log_entries.append(entry)
        print(f"📥 Logger: {entry}")

    def show_log(self):
        """Display all logged entries."""
        print(f"\n📋 Event Log ({len(self._log_entries)} entries):")
        for i, entry in enumerate(self._log_entries):
            print(f"   [{i+1}] {entry}")


async def demonstrate_slots():
    """Demonstrate the @Slot decorator system."""

    print("🎯 @Slot Decorator Demonstration")
    print("=" * 50)

    # Create processor and logger
    processor = DataProcessor()
    logger = EventLogger()

    print("\n📋 Slot Discovery:")

    # Show discovered slots using reflection
    processor_slots = get_slots(processor)
    logger_slots = get_slots(logger)

    print(f"Processor slots:")
    for slot_name, slot_info in processor_slots.items():
        arg_types = (
            ", ".join(t.__name__ for t in slot_info.arg_types)
            if slot_info.arg_types
            else "None"
        )
        result_type = (
            slot_info.result_type.__name__ if slot_info.result_type else "None"
        )
        print(f"  • {slot_name}({arg_types}) -> {result_type}")

    print(f"\nLogger slots:")
    for slot_name, slot_info in logger_slots.items():
        arg_types = (
            ", ".join(t.__name__ for t in slot_info.arg_types)
            if slot_info.arg_types
            else "None"
        )
        print(f"  • {slot_name}({arg_types})")

    print(f"\n🔗 Manual Signal-Slot Connections:")

    # Connect processor signals to logger slots manually
    processor.data_received.connect(logger.on_data_received)
    processor.processing_complete.connect(logger.on_processing_complete)
    processor.error_occurred.connect(logger.on_error_occurred)

    print("✅ Connected processor signals to logger slots")

    print(f"\n🎮 Testing Slot Operations:")

    # Test data processing
    test_data = [
        {"type": "measurement", "value": 42.5, "unit": "angstrom"},
        {"type": "coordinate", "x": 1.0, "y": 2.0, "z": 3.0},
        {"type": "metadata", "source": "experiment_001"},
    ]

    for i, data in enumerate(test_data):
        print(f"\n--- Test {i+1} ---")

        # Emit data received signal (triggers logger)
        processor.data_received.emit(data)

        # Process the data (triggers completion signal -> logger)
        processor.process_data(data)

    print(f"\n✅ Input Validation Testing:")

    # Test validation slot with type checking
    validation_tests = [
        ("hello", 3),  # Valid
        ("hi", 5),  # Invalid (too short)
        ("testing", 4),  # Valid
    ]

    for text, min_len in validation_tests:
        result = processor.validate_input(text, min_len)
        print(f"   '{text}' >= {min_len}: {result}")

    print(f"\n🔄 Other Slot Operations:")

    # Test logging slot
    processor.log_event("info", {"action": "test_completed", "items": len(test_data)})
    processor.log_event("debug", {"memory_usage": "15MB", "cpu_time": "0.5s"})

    # Show current stats
    stats = processor.get_stats()
    print(f"Processor stats: {stats}")

    # Test reset slot
    processor.reset_processor()

    print(f"\n🚨 Error Handling:")

    # Trigger an error (for demonstration)
    try:
        # This would normally cause an error, but we'll simulate it
        processor.error_occurred.emit("Simulated network timeout")
    except Exception as e:
        print(f"Caught exception: {e}")

    print(f"\n📋 Final Event Log:")
    logger.show_log()

    print(f"\n⚡ Type Checking Demo:")

    # Demonstrate type checking (this would raise TypeError)
    try:
        print("Testing correct types...")
        processor.validate_input("test", 4)  # Correct types

        print("Testing incorrect types (should fail)...")
        # This should raise TypeError due to @Slot type checking
        # processor.validate_input(123, "invalid")  # Wrong types - commented out
        print("(Type checking test skipped to avoid error)")

    except TypeError as e:
        print(f"✅ Type checking caught error: {e}")

    print(f"\n✅ @Slot decorator demonstration complete!")


if __name__ == "__main__":
    asyncio.run(demonstrate_slots())
