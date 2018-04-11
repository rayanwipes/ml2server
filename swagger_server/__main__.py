#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.fitter.task_manager import *
import threading
from time import sleep
import asyncio


task_manager = TaskManager()


async def run_task_manager():
    print("task manager thread started")
    while not task_manager.EXIT_FLAG:
        sleep(0.5)
        # await task_manager.remove_finished()
    print("task manager thread finished")


async def run_server():
    print("server thread started")
    sleep(5)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'JHProject ML API'})
    app.run(port=8080)
    await task_manager.set_finished()
    print("server thread finished")


def main():
    # start the subshell here

    print("Running the app")
    event_loop = asyncio.get_event_loop()

#    tm_future = asyncio.Future()
#    asyncio.ensure_future(run_task_manager(tm_future))
#
#    server_future = asyncio.Future()
#    asyncio.ensure_future(run_server(server_future))

#    sleep(1)
    print("future wait")
    try:
        event_loop.run_until_complete(asyncio.gather(
            run_server(),
            run_task_manager()
        ))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
