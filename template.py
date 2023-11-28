from common import Logger, Severity, Response
import inspect

logger = Logger()

def pre_check_env_windows():
    eventName = "Validating environment pre-checks in Windows"
    caller = logger.get_caller()
    try:
        print(eventName)
        if "Windows" in eventName:
            record(eventName, caller, "SUCCESS")
        else:
            message = "eventName doesn't contain Windows"
            record(eventName, caller, "FAILURE", "ERROR", message)
            
        pre_check_ansible_windows()
            
    except Exception as e:
        record(eventName, caller, "FAILURE", "EXCEPTION", str(e))
        

def pre_check_ansible_windows():
    eventName = "Validating installation of Ansible in Windows"
    caller = logger.get_caller()
    try:
        print(eventName)
        if "Ansible" in eventName:
            record(eventName, caller, "SUCCESS")
        else:
            message = "eventName doesn't contain Ansible"
            record(eventName, caller, "FAILURE", "ERROR", message) 
            
    except Exception as e:
        record(eventName, caller, "FAILURE", "EXCEPTION", str(e))
       
        
def record(eventName, caller, response, severity=None, message=None):
    eventData = []
    if severity not in ["ERROR", "EXCEPTION"] and response == "SUCCESS":
        eventData = [
                        {
                            "name": eventName,
                            "data": {
                                "caller": caller,
                                "response": response,
                                "message": eventName + "executed successfully"
                            }
                        }
                    ]
    else:
        eventData = [
                        {
                            "name": eventName,
                            "data": {
                                "caller": caller,
                                "severity": Severity(severity).value,
                                "message": str(e)
                            }
                        }
                    ]

    logger_data = logger(eventData)
    logger_data.write_to_file('output.json')
    logger.read_and_print_file('output.json')
    

if __name__ == "__main__":
    pre_check_env_windows()
