class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks += [task]

    def remove_finished(self):
        for t in self.tasks:
            if t.is_finished():
                t.finalize()
