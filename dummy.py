import json
from datetime import datetime

class DataProcessor:
    def __init__(self, events=None):
        # Default values for event data fields
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
            # If events are provided, use them with default values for missing fields
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
            print(f"\nEvent: {event['name']}")
            for data in event['data']:
                # Check if data is a dictionary; if not, convert it to a dictionary
                data_dict = json.loads(data) if isinstance(data, str) else data
                print(f"  Datetime: {data_dict['datetime']}, Severity: {data_dict['severity']}, Response: {data_dict['response']}, Message: {data_dict['message']}")

# Example usage:
# If no events are provided, a default event will be used
processor1 = DataProcessor()
processor1.print_events()

# If events are provided, missing data fields will be filled with default values
event_data = {
    "CustomEvent1": [
        '{"datetime": "2023-01-01 12:00:00", "severity": "Medium"}',  # Missing response and message fields
        '{"datetime": "2023-01-02 15:30:00"}'  # Missing severity, response, and message fields
    ],
    "CustomEvent2": [
        '{"datetime": "2023-01-03 09:45:00", "severity": "High", "response": "Action taken", "message": "Critical custom issue"}'
    ]
}
processor2 = DataProcessor(event_data)
processor2.print_events()
