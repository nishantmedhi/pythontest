from datetime import datetime
from enum import Enum
import inspect

class Severity(Enum):
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'

class EventLogger:
    def __init__(self, events=None):
        if events is None:
            events = [self.create_default_event(), self.create_default_event()]

        self.events = events

    def create_default_event(self):
        return {
            "name": "Default event",
            "data": {
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "severity": Severity.INFO.name,
                "caller": self.get_caller(),
                "response": "FAILURE",
                "message": ""
            }
        }

    def get_caller(self):
        # Use inspect to get the name of the calling function
        frame = inspect.currentframe()
        caller = inspect.getouterframes(frame)[2].function
        return caller

    def display_events(self):
        for event in self.events:
            print(event)

# Example usage:

# Create an EventLogger with default events
logger1 = EventLogger()
logger1.display_events()

# Create an EventLogger with provided events
custom_events = [
    {
        "name": "Custom Event 1",
        "data": {
            "datetime": "2023-01-01 12:00:00",
            "severity": Severity.WARNING.name,
        }
    },
    {
        "name": "Custom Event 2",
        "data": {
            "datetime": "2023-02-02 14:30:00",
            "response": "FAILURE",
            "message": "Custom message 2"
        }
    }
]

logger2 = EventLogger(custom_events)
logger2.display_events()
