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
        self.output_json = self.generate_output_json()

    def generate_output_json(self):
        output = []
        for event in self.events:
            event_data = {
                "name": event['name'],
                "data": [
                    {
                        "datetime": data['datetime'],
                        "severity": data['severity'],
                        "response": data['response'],
                        "message": data['message']
                    }
                    for data in event['data']
                ]
            }
            output.append(event_data)
        return output

# Example usage:
# If no events are provided, a default event will be used
processor1 = DataProcessor()
print(json.dumps(processor1.output_json, indent=2))
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
print(json.dumps(processor2.output_json, indent=2))
