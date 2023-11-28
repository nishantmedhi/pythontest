import json
from enum import Enum
from datetime import datetime
import inspect
import os

class Severity(Enum):
    INFO = 0
    WARNING = 1
    ERROR = 2
    EXCEPTION = 3

class Response(Enum):
    SUCCESS = 200
    FAILURE = 400

class Logger:
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
                    "caller": event["data"].get("caller", self.get_caller()),
                    "response": event["data"].get("response", Response.FAILURE.value),
                    "message": event["data"].get("message", "")
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
        if os.path.exists(filename):
            # If the file already exists, load existing data and append new data
            with open(filename, 'r') as json_file:
                existing_data = json.load(json_file)
                existing_data["Event"].extend(processed_data["Event"])
        else:
            existing_data = processed_data
        
        with open(filename, 'w') as json_file:
            json.dump(existing_data, json_file, indent=2)
                

    def get_caller(self):
        stack = inspect.stack()
        if len(stack) > 2:
            calling_module = stack[1][1]
            calling_function = stack[1][3]
            # if the calling function is empty, return only the calling module
            if calling_function in "<module>":
                return f"{calling_module}"
            return f"{calling_module}.{calling_function}"
        return "Function caller could not be determined"
