import json
from enum import Enum
from datetime import datetime
import inspect
import os

class Severity(Enum):
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    EXCEPTION = 'EXCEPTION'

class Response(Enum):
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'

class EventProcessor:
    def __init__(self, events=None):
        if events is None:
            events = []
        self.events = events

    def process_data(self):
        processed_data = []
        for event in self.events:
            processed_event = {
                "name": event.get("name", "default_event"),
                "data": {
                    "datetime": event["data"].get("datetime", datetime.now().isoformat()),
                    "severity": event["data"].get("severity", Severity.INFO.value),
                    "caller": event["data"].get("caller", inspect.stack()[1][3]),
                    "response": event["data"].get("response", Response.SUCCESS.value),
                    "message": event["data"].get("message", "Default message from process_data")
                }
            }
            processed_data.append(processed_event)

        return {"Event": processed_data}

    def read_and_print_file(self, filename='output.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as json_file:
                file_content = json.load(json_file)
                print("File Content:")
                print(json.dumps(file_content, indent=2))
        else:
            print(f"The file {filename} does not exist.")
            
    def write_to_file(self, filename='output.json'):
        processed_data = self.process_data()
        print(f"Processed data :")
        print(json.dumps(processed_data, indent=2))

        if os.path.exists(filename):
            # If the file already exists, load existing data and append new data
            with open(filename, 'r') as json_file:
                existing_data = json.load(json_file)
                existing_data["Event"].extend(processed_data["Event"])
        else:
            existing_data = processed_data

        with open(filename, 'w') as json_file:
            json.dump(existing_data, json_file, indent=2)
        print(f"Processed data written to {filename}")

# If data is provided, it updates the fields accordingly
processor = EventProcessor()
processor.write_to_file('output.json')  # Create a file with default data


# If data is provided, it updates the fields accordingly
custom_data_1 = [
    {
        "name": "custom_event_1",
        "data": {
            "severity": Severity.ERROR.value
            #"message": "Custom error message 1"
        }
    }
]
processor_with_data_1 = EventProcessor(custom_data_1)
processor_with_data_1.write_to_file('output.json')  # Append data to existing file

# Add another set of custom data
custom_data_2 = [
    {
        "name": "custom_event_2",
        "data": {
            "severity": Severity.WARNING.value
            #"message": "Custom warning message 2"
        }
    }
]
processor_with_data_2 = EventProcessor(custom_data_2)
processor_with_data_2.write_to_file('output.json')

EventProcessor.read_and_print_file('output.json')
