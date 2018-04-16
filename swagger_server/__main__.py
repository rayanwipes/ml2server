#!/usr/bin/env python3

import sys
import connexion
import logging


from swagger_server import encoder
from swagger_server.fitter.task_manager import *
from swagger_server.controllers.global_variables import *

def main():
    backend_ip = sys.argv[1]
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    global_variables_init(backend_ip)
    print("initialised variables")
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'JHProject ML API'})
    app.run(port=8080)
    # task_manager.set_finished()


if __name__ == '__main__':
    main()
