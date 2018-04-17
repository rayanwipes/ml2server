from swagger_server.controllers.global_variables import *
from swagger_server.algorithms.backend-client import *

def end_client_things(client,json):
    # need to add the thing where the final file gets updated
    ouput_file_info = metadata['files']
    c.update_model(files)
    c.update_metadata(project_name)

def get_ip():
    global ip_lock
    global ip
    ip_lock.aquire()
    var = yield ip
    ip_lock.release()
    return var
