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

class EventProcessor:
    def __init__(self, events=None):
        if events is None:
            events = [
                {
                    "name": "default_event",
                    "data": {
                        "datetime": datetime.now().isoformat(),
                        "severity": Severity.INFO.value,
                        "caller": inspect.stack()[1][3],
                        "response": Response.SUCCESS.value,
                        "message": "Default message"
                    }
                }
            ]
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
                    "message": event["data"].get("message", "Default message")
                }
            }
            processed_data.append(processed_event)

        return {"Event": processed_data}

    def write_to_file(self, filename='output.json'):
        processed_data = self.process_data()
        print(f"Processed data :")
        print(json.dumps(processed_data, indent=2))
        #with open(filename, 'w') as json_file:
            #json.dump(processed_data, json_file, indent=2)
        #print(f"Processed data written to {filename}")


# If data is provided, it updates the fields accordingly
custom_data = [
    {
        "name": "custom_event",
        "data": {
            "severity": Severity.ERROR.value,
            "message": "Custom error message"
        }
    }
]
processor_with_data = EventProcessor(custom_data)
processor_with_data.write_to_file('output.json')
