from common import Logger, Severity, Response

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
                                #"response": "SUCCESS",
                                "response": str(Response(response).value),
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
                                "severity": str(Severity(severity).value),
                                "message": str(e)
                            }
                        }
                    ]

    logger_data = Logger(eventData)
    logger_data.write_to_file('output.json')
    # Optional read file function to see the updated json file with every insertion of incoming event data
    logger.read_and_print_file('output.json')
    

if __name__ == "__main__":
    pre_check_env_windows()
