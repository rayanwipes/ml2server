class TaskManager:
    def __init__(self):
        self.tasks = []
        self.metadata = {}
        self.project_name_taskref = {}

    def add(self, task, project_name, uuid, output, report_output=None):
        id = len(self.tasks)
        self.tasks += [task]
        if project_name not in self.project_name_taskref:
            self.project_name_taskref[project_name] = {}
        self.project_name_taskref[uuid] = id
        self.tasks[-1].start(output, report_output)

   def _remove_task_ref(self, i):
        del self.tasks[i]
        del self.metadata[i]
        for pname, uuid in self.project_name_taskref.items():
            self.project_name_taskref[pname] = {
                u : id
                    for u, id in self.project_name_taskref[pname].items()
                        if id != i
            }

    def get_task_id(self, project_name, uuid):
        if project_name not in self.project_name_taskref:
            return -1
        if uuid not in self.project_name_taskref[project_name]
            return -1
        return self.tasks[self.project_name_taskref[project_name][uuid]].is_finished()

    def set_netadata(self, id, metadata):
        self.metadata[id] = metadata

    def get_metadata(self, id):
        if id not in self.metadata:
            raise Exception("unable to retreive metadata")
        return self.metadata[id]

    def is_finished(self, id):
        if id == -1:
            return False
        return self.tasks[id].is_finished()

    def kill_task(self, project_name, uuid):
        id = get_task_id(project_name, uuid)
        self.tasks]id].stop()
        self._remove_task_ref(id)

    def kill_project(self, project_name):
        p = self.project_name_taskref[project_name]
        self.remove_finished()
        for u, i in p.items():
            self._remove_task_ref(p[u])

    def remove_finished(self):
        i = 0
        while i < len(self.tasks):
            if self.tasks[i].is_finished():
                self.tasks[i].finalize()
                self._remove_task_ref(i)
            else:
                i += 1
