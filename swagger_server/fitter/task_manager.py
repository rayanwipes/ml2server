class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks += [task]

    def remove_finished(self):
        i = 0
        while i < len(self.tasks):
            if self.tasks[i].is_finished():
                del self.tasks[i]
                self.tasks[i].finalize()
            else:
                i += 1
