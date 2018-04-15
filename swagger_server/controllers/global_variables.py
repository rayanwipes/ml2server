from swagger_server.fitter.task_manager import *
from threading import *

base_path_to_files = "./swagger_server/tmp_files/"

def global_variables_akjdfhdkjas_init():
    global task_manager
    global lock
    task_manager = TaskManager()
    lock = Lock()
