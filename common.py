import json
from enum import Enum
import os
from datetime import datetime
import inspect


class Severity(Enum):
    INFO = 0
    WARNING = 1
    ERROR = 2
    EXCEPTION = 3

class Logger:
    def __init__(self, events=None):
        default_values = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "severity": Severity.INFO.name,
	    "caller": self.get_caller(),
            "response": "FAILURE",
            "message": ""
        }
        
        if events is None:
            # If no events are provided, use a default event
            self.events = [
                {
                    "name": "Default Event",
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

    @staticmethod
    def log_to_file(json_data, file_path='logger.json'):
        log_entry = json_data
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump([log_entry], file, indent=2)
        else:
            with open(file_path, 'r') as file:
                data = json.load(file)
                data.append(log_entry)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
                

    def get_caller(self):
        stack = inspect.stack()
        if len(stack) > 2:
            calling_module = inspect.getmodulename(stack[2].filename)
            calling_function = stack[2].function
            return f"{calling_module}.{calling_function}"
        return "Function caller could not be determined"
