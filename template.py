from common import Logger
from record import EventRecorder

logger = Logger()
eventRecorder = EventRecorder()

def pre_check_env_windows():
    eventName = "Validating environment pre-checks in Windows"
    eventData = []
    caller = logger.get_caller()
    try:
        print(eventName)
        if "Windows" in eventName:
            eventData = eventRecorder.record(eventName, caller, "SUCCESS")
            update_logs(eventData)
        else:
            message = "eventName doesn't contain Windows"
            eventData = eventRecorder.record(eventName, caller, "FAILURE", "ERROR", message)
            update_logs(eventData)
            
        pre_check_ansible_windows()
            
    except Exception as e:
        eventData = eventRecorder.record(eventName, caller, "FAILURE", "EXCEPTION", str(e))
        update_logs(eventData)

def pre_check_ansible_windows():
    eventName = "Validating installation of Ansible in Windows"
    eventData = []
    caller = logger.get_caller()
    try:
        print(eventName)
        if "Ansible" in eventName:
            eventData = eventRecorder.record(eventName, caller, "SUCCESS")
            update_logs(eventData)
        else:
            message = "eventName doesn't contain Ansible"
            eventData = eventRecorder.record(eventName, caller, "FAILURE", "ERROR", message)
            update_logs(eventData)
            
    except Exception as e:
        eventData = eventRecorder.record(eventName, caller, "FAILURE", "EXCEPTION", str(e))
        update_logs(eventData)
       
def update_logs(eventData):
    logger_data = Logger(eventData)
    logger_data.write_to_file('output.json')
    logger.read_and_print_file('output.json')


"""def record(eventName, caller, response, severity=None, message=None):
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
                                "message": str(e)
                            }
                        }
                    ]

    logger_data = Logger(eventData)
    logger_data.write_to_file('output.json')
    # Optional read file function to see the updated json file with every insertion of incoming event data
    logger.read_and_print_file('output.json')"""
    

if __name__ == "__main__":
    pre_check_env_windows()
