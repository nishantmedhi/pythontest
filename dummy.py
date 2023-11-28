import json
from enum import Enum
from datetime import datetime
import inspect

class Severity(Enum):
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'

class Response(Enum):
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'

class EventLogger:
    def __init__(self, data=None):
        self.data = {
            "Event": []
        }
        if data is not None:
            # Update with provided data, filling missing values with defaults
            self.fill_defaults(data)

    def fill_defaults(self, data):
        for event in data.get("Event", []):
            existing_event = next(
                (e for e in self.data["Event"] if e["name"] == event["name"]),
                None
            )
            if existing_event:
                existing_event["data"].update(self.fill_default_values(event.get("data", {})))
            else:
                self.data["Event"].append({
                    "name": event["name"],
                    "data": self.fill_default_values(event.get("data", {}))
                })

    def fill_default_values(self, data):
        default_values = {
            "datetime": str(datetime.now()),
            "severity": Severity.INFO.value,
            "caller": self.get_caller_function(),
            "response": Response.SUCCESS.value,
            "message": "Default message"
        }
        data.update({key: data.get(key, value) for key, value in default_values.items()})
        return data

    def get_caller_function(self):
        # Get the name of the calling function using inspect
        frame = inspect.currentframe().f_back
        return inspect.getframeinfo(frame).function

    def to_json(self):
        return json.dumps(self.data, indent=2)

# Example usage:

# Case 1: No data provided, use default values
event_logger_1 = EventLogger()
print(event_logger_1.to_json())

# Case 2: Provide data with some fields missing
custom_data = {
    "Event": [
        {
            "name": "CustomEvent",
            "data": {
                "severity": Severity.WARNING.value,
                "message": "Custom message"
            }
        },
        {
            "name": "CustomEvent",
            "data": {
                "response": Response.FAILURE.value,
                "message": "Another message"
            }
        }
    ]
}
event_logger_2 = EventLogger(custom_data)
print(event_logger_2.to_json())
