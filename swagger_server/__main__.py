#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.fitter.task_manager import *
from threading import *
from time import sleep
import datetime
import asyncio


task_manager = TaskManager()
lock = Lock()

def run_task_manager(name):
    global task_manager
    print("task manager thread started")
    while True:
        sleep(10)
        lock.acquire()
        task_manager.remove_finished()
        print("removed the finished things at " + str(datetime.datetime.now()))
        if task_manager.is_done():
            lock.release()
            break
        lock.release()
    print("task manager thread finished")


def run_server(args):
    print("server thread started")
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'JHProject ML API'})
    app.run(port=8080)
    # task_manager.set_finished()

    print("server thread finished")


def main():
    # start the subshell here
    thread1 = Thread(target=run_task_manager, args=("Thread-1", ) )
    thread2 = Thread(target=run_server, args=("Thread-2", ) )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
#     print("Running the app")
#     event_loop = asyncio.get_event_loop()
#
# #    tm_future = asyncio.Future()
# #    asyncio.ensure_future(run_task_manager(tm_future))
# #
# #    server_future = asyncio.Future()
# #    asyncio.ensure_future(run_server(server_future))
#
# #    sleep(1)
#     print("future wait")
#     try:
#         event_loop.run_until_complete(asyncio.gather(
#             run_server(),
#             run_task_manager()
#         ))
#     finally:
#         event_loop.close()


if __name__ == '__main__':
    main()
