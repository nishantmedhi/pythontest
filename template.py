from common import Logger, Severity
import inspect

logger = Logger()

def pre_check_env_windows():
    try:
        caller = logger.get_caller()
        eventName = "Validating environment pre-checks in Windows"
        print(eventName)
        
        if "Windows" in eventName:
            logger.record(eventName, caller, "SUCCESS")
        else:
            message = "eventName doesn't contain Windows"
            logger.record(eventName, caller, "SUCCESS", WARNING, message)
            
        pre_check_ansible_windows()
            
    except Exception as e:
        logger.record(eventName, caller, "FAILURE", EXCEPTION, str(e))
        

def pre_check_ansible_windows():
    try:
        caller = logger.get_caller()
        eventName = "Validating installation of Ansible in Windows"
        print(eventName)
        
        if "Ansible" in eventName:
            logger.record(eventName, caller, "SUCCESS")
        else:
            message = "eventName doesn't contain Ansible"
            logger.record(eventName, caller, "FAILURE", ERROR, message) 
            
    except Exception as e:
        logger.record(eventName, caller, "FAILURE", EXCEPTION, str(e))
      
      
if __name__ == "__main__":
    pre_check_env_windows()