from enum import Enum
from common import Severity, Response
import json

class EventRecorder:
    def record(eventName, caller, response, severity=None, message=None):
        eventData = []
        if severity not in [Severity.ERROR.name, Severity.EXCEPTION.name] and response == Response.SUCCESS.name:
            eventData = [
                {
                    "name": eventName,
                    "data": {
                        "caller": caller,
                        "response": getattr(Response, response).value,
                        "message": eventName + " executed successfully"
                    }
                }
            ]
        else:
            eventData = [
                {
                    "name": eventName,
                    "data": {
                        "caller": caller,
                        "severity": getattr(Severity, severity).value,
                        "message": message
                    }
                }
            ]
        return eventData
