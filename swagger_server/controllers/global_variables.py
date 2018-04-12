from swagger_server.fitter.task_manager import *
from threading import *

def global_variables_akjdfhdkjas_init():
    global task_manager
    global lock
    task_manager = TaskManager()
    lock = Lock()
