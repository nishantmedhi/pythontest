import json
from datetime import datetime

class DataProcessor:
    def __init__(self, events=None):
        if events is None:
            # If no events are provided, use dummy values for two events
            self.events = {
                "Event1": [
                    {"datetime": str(datetime.now()), "severity": "High", "response": "Action taken", "message": "Critical issue"},
                    {"datetime": str(datetime.now()), "severity": "Medium", "response": "Investigating", "message": "Potential problem"}
                ],
                "Event2": [
                    {"datetime": str(datetime.now()), "severity": "Low", "response": "No action required", "message": "Informational message"},
                    {"datetime": str(datetime.now()), "severity": "High", "response": "Action taken", "message": "Another critical issue"}
                ]
            }
        else:
            # If events are provided, use them
            self.events = {}
            for event_name, event_data in events.items():
                self.events[event_name] = [json.loads(item) for item in event_data]

    def print_events(self):
        for event_name, event_data in self.events.items():
            print(f"\nEvent: {event_name}")
            for data in event_data:
                print(f"  Datetime: {data['datetime']}, Severity: {data['severity']}, Response: {data['response']}, Message: {data['message']}")

# Example usage:
# If no events are provided, dummy values will be used for two events
processor1 = DataProcessor()
processor1.print_events()

# If events are provided, they will be used
event_data = {
    "CustomEvent1": [
        '{"datetime": "2023-01-01 12:00:00", "severity": "Medium", "response": "Investigating", "message": "Custom issue"}',
        '{"datetime": "2023-01-02 15:30:00", "severity": "Low", "response": "No action required", "message": "Another custom message"}'
    ],
    "CustomEvent2": [
        '{"datetime": "2023-01-03 09:45:00", "severity": "High", "response": "Action taken", "message": "Critical custom issue"}'
    ]
}
processor2 = DataProcessor(event_data)
processor2.print_events()
