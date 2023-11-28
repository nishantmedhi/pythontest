from common import Logger
from record import EventRecorder
import os, sys

logger = Logger()
eventRecorder = EventRecorder()
update_java_version = os.environ['TO_VERSION']

def verify_java_upgrade_install_windows():
    eventName = "Verify java upgrade version in Windows"
    caller = logger.get_caller()
    try:
        print(eventName)
        if "11.0.11" in update_java_version:
            update_logs(eventRecorder.record(eventName, caller, "SUCCESS"))
        else:
            message = "to_version in workflow input is below the prescribed version for update"
            update_logs(eventRecorder.record(eventName, caller, "FAILURE", "ERROR", message))
            sys.exit(1)
            
        upgrage_java_install_windows()
            
    except Exception as e:
        update_logs(eventRecorder.record(eventName, caller, "FAILURE", "EXCEPTION", str(e)))

def upgrage_java_install_windows():
    eventName = "Installing java version " + update_java_version + " in Windows"
    caller = logger.get_caller()
    try:
        print(eventName)
        if "11.0.11" in eventName:
            update_logs(eventRecorder.record(eventName, caller, "SUCCESS"))
        else:
            message = "Installation of java version " + update_java_version + " failed in Windows"
            update_logs(eventRecorder.record(eventName, caller, "FAILURE", "ERROR", message))
            sys.exit(1)
            
    except Exception as e:
        update_logs(eventRecorder.record(eventName, caller, "FAILURE", "EXCEPTION", str(e)))
       
def update_logs(eventData):
    logger_data = Logger(eventData)
    logger_data.write_to_file()
    logger.read_and_print_file()
    
if __name__ == "__main__":
    verify_java_upgrade_install_windows()
