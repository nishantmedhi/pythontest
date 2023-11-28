from logdata import Logger, Severity
import inspect

logger = Logger()

def pre_check_env_windows():
    try:
        caller = Logger.get_caller()
        eventName = "Validating environment pre-checks in Windows"
        print(eventName)
        
        if "Windows" in eventName:
            record(eventName, caller, "SUCCESS")
        else:
            message = "eventName doesn't contain Windows"
            record(eventName, caller, "FAILURE", ERROR, message)
            
        pre_check_ansible_windows()
            
    except Exception as e:
        record(eventName, caller, "FAILURE", EXCEPTION, str(e))
        

def pre_check_ansible_windows():
    try:
        caller = Logger.get_caller()
        eventName = "Validating installation of Ansible in Windows"
        print(eventName)
        
        if "Ansible" in eventName:
            record(eventName, caller, "SUCCESS")
        else:
            message = "eventName doesn't contain Ansible"
            record(eventName, caller, "FAILURE", ERROR, message) 
            
    except Exception as e:
        record(eventName, caller, "FAILURE", EXCEPTION, str(e))
       
        
def record(eventName, caller, response, severity = null, message = null):
    logger.event.name = eventName
    logger.event.data.caller = caller
    if (severity != "ERROR" or severity != "EXCEPTION") and response == "SUCCESS":
        logger.event.data = {
                        "response": response
                    }
    else:
        logger.event.data = {
                        "severity": Severity.$severity.value,
                        "message": str(e)
                    }
        
    logger.log_to_file(logger.__dict__)
    

if __name__ == "__main__":
    pre_check_env_windows()
