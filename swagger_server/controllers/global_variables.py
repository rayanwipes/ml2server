from swagger_server.fitter.task_manager import *
from threading import *

base_path_to_files = "./swagger_server/tmp_files/"

def global_variables_init(ip_value):
    global task_manager
    global lock
    global ip
    global ip_lock
    ip = ip_value
    task_manager = TaskManager()
    lock = Lock()
    ip_lock = Lock()
