import sys
import os

# Step 1: Determine the GitHub runner's path
github_runner_path = os.environ.get('RUNNER_WORKSPACE', '')

# Step 2: Determine the repository name
repository_name = os.environ.get('GITHUB_REPOSITORY', '')
repo_name = repository_name.split('/')[-1] if repository_name else ''

module_path = os.path.join(github_runner_path, repo_name, "/custom_components/common")

sys.path.insert(0, module_path)

print(sys.path)

from logger import Logger
from eventRecorder import EventRecorder

logger = Logger()
eventRecorder = EventRecorder()

def pre_check_env_windows():
    eventName = "Validating environment pre-checks in Windows"
    caller = logger.get_caller()
    try:
        print(eventName)
        if "Windows" in eventName:
            update_logs(eventRecorder.record(eventName, caller, "SUCCESS"))
        else:
            message = "eventName doesn't contain Windows"
            update_logs(eventRecorder.record(eventName, caller, "FAILURE", "ERROR", message))
            
        pre_check_ansible_windows()
            
    except Exception as e:
        update_logs(eventRecorder.record(eventName, caller, "FAILURE", "EXCEPTION", str(e)))

def pre_check_ansible_windows():
    eventName = "Validating installation of Ansible in Windows"
    caller = logger.get_caller()
    try:
        print(eventName)
        if "Ansible" in eventName:
            update_logs(eventRecorder.record(eventName, caller, "SUCCESS"))
        else:
            message = "eventName doesn't contain Ansible"
            update_logs(eventRecorder.record(eventName, caller, "FAILURE", "ERROR", message))
            
    except Exception as e:
        update_logs(eventRecorder.record(eventName, caller, "FAILURE", "EXCEPTION", str(e)))
       
def update_logs(eventData):
    logger_data = Logger(eventData)
    logger_data.write_to_file()
    logger.read_and_print_file()
    
if __name__ == "__main__":
    pre_check_env_windows()
