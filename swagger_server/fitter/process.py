import os
import signal
import subprocess
import time
import pipes


class Process:
    def __init__(self, successfile):
        self.process = None
        self.running = False
        self.successfile = successfile
        if os.path.exists(self.successfile):
            os.remove(self.successfile)

    def start(self, args):
        # subprocess.Popen(args, shell=True)
        self.running = True
        args = [args[0]] + [self.successfile] + args[1:]
        args = [pipes.quote(arg) for arg in args]
        print(args)
        self.process = subprocess.Popen(args)

    def is_finished(self):
        return self.running and os.path.exists(self.successfile)

    def kill(self):
        # os.kill(process.pid, signal.SIGINT)
        self.process.terminate()
        self.running = False

    def force_stop(self):
        self.process.kill()
        self.running = False

    def finalize(self):
        if self.is_finished():
            os.remove(self.successfile)
        self.running = False


if __name__ == "__main__":
    p = Process('success')
    p.start('sleep 5; touch success')
    time.sleep(2)
    p.kill()

