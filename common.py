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
    def __init__(self, json_data=None):
        if json_data is None:
	        json_data = {
				    "event": [
				        {
				            "name": "Default event",
			                    "data": {
			                        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			                        "severity": Severity.INFO.name,
			                        "caller": self.get_caller(),
			                        "response": "FAILURE",
			                        "message": ""
			                    }
				        }
				    ]
		}
        else:
            self.event = []
	    self.event.name = json_data["name"]
            self.event.data = json_data["data"]	

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
