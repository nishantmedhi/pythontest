import json
from datetime import datetime

class DataProcessor:
    def __init__(self, events=None):
        default_values = {
            "datetime": str(datetime.now()),
            "severity": "High",
            "response": "Action taken",
            "message": "Critical issue"
        }
        
        if events is None:
            # If no events are provided, use a default event
            self.events = [
                {
                    "name": "Default",
                    "data": default_values
                }
            ]
        else:
            # If events are provided, use them
            self.events = []
            for event_name, event_data in events.items():
                custom_event_data = []
                for item in event_data:
                    # Fill missing fields with default values
                    filled_data = {**default_values, **json.loads(item)}
                    custom_event_data.append(filled_data)
                self.events.append({
                    "name": event_name,
                    "data": custom_event_data
                })

    def print_events(self):
        for event in self.events:
            for data in event['data']:
                print(data)
                #print(f"  Datetime: {data['datetime']}, Severity: {data['severity']}, Response: {data['response']}, Message: {data['message']}")

# Example usage:
# If no events are provided, a default event will be used
processor1 = DataProcessor()

# If events are provided, they will be used with dynamic names
event_data = {
    "CustomEvent1": [
        '{"datetime": "2023-01-01 12:00:00", "message": "Custom issue"}',
        '{"datetime": "2023-01-02 15:30:00", "severity": "Low", "response": "No action required", "message": "Another custom message"}'
    ],
    "CustomEvent2": [
        '{"datetime": "2023-01-03 09:45:00", "severity": "High", "response": "Action taken", "message": "Critical custom issue"}'
    ]
}
processor2 = DataProcessor(event_data)
processor2.print_events()
