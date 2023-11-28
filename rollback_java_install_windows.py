from common import Logger
from record import EventRecorder
import os

logger = Logger()
eventRecorder = EventRecorder()
rollback_java_version = os.environ['FROM_VERSION']

def rollback_java_install_windows():
    eventName = "Rollback java installation in Windows"
    caller = logger.get_caller()
    try:
        print(eventName)
        if "11.0.10" in rollback_java_version:
            update_logs(eventRecorder.record(eventName, caller, "SUCCESS"))
        else:
            message = "Error occured while executing rollback of Java installation in Windows"
            update_logs(eventRecorder.record(eventName, caller, "FAILURE", "ERROR", message))
            
    except Exception as e:
        update_logs(eventRecorder.record(eventName, caller, "FAILURE", "EXCEPTION", str(e)))
       
def update_logs(eventData):
    logger_data = Logger(eventData)
    logger_data.write_to_file()
    logger.read_and_print_file()
    
if __name__ == "__main__":
    rollback_java_install_windows()
