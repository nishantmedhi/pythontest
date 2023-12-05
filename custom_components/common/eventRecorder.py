from custom_components.common.logger import Severity, Response

class EventRecorder:
    def record(self, eventName, caller, response, severity=None, message=None):
        eventData = []
        if severity not in ["ERROR", "EXCEPTION"] and response == "SUCCESS":
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
                        "message": str(message)
                    }
                }
            ]
        return eventData
