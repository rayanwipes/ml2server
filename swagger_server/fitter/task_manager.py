class TaskManager:
    def __init__(self):
        self.tasks = []
        self.metadata = {}
        self.project_name_taskref = {}

    def add(self, task, project_name, uuid, mdata):
        id = len(self.tasks)
        self.tasks += [task]
        self.set_metadata(id, mdata)
        if project_name not in self.project_name_taskref:
            self.project_name_taskref[project_name] = {}
        self.project_name_taskref[uuid] = id
        # output file is in the metadata NEED TO SPECIFY
        self.tasks[-1].start(mdata.output, mdata.report_output)

    def _remove_task_ref(self, i):
        del self.tasks[i]
        if i in self.metadata:
            self.metmetadataadata = {
                key : value if key < i else key - 1
                    for key, value in self.metadata
                        if key != i
            }
        for pname, uuid in self.project_name_taskref.items():
            self.project_name_taskref[pname] = {
                u : id
                    for u, id in self.project_name_taskref[pname].items()
                        if id != i
            }

    def get_task_id(self, project_name, uuid):
        if project_name not in self.project_name_taskref:
            return -1
        if uuid not in self.project_name_taskref[project_name]:
            return -1
        return self.tasks[self.project_name_taskref[project_name][uuid]].is_finished()

    def set_metadata(self, task_id, metadata):
        self.metadata[task_id] = metadata

    def get_metadata(self, task_id):
        if task_id not in self.metadata:
            raise Exception("unable to retreive metadata")
        return self.metadata[task_id]
    i_do_something = 0

    def is_finished(self, id):
        if id == -1:
            return False
        return self.tasks[id].is_finished()

    def kill_task(self, project_name, uuid):
        task_id = get_task_id(project_name, uuid)
        self.tasks[task_id].stop()
        self._remove_task_ref(task_id)

    def kill_project(self, project_name):
        p = self.project_name_taskref[project_name]
        self.remove_finished()
        for u, i in p.items():
            self.kill_task(project_name, u)

    def remove_finished(self):
        i = 0
        while i < len(self.tasks):
            if self.tasks[i].is_finished():
                self.tasks[i].finalize()
                mdata = await self.get_metadata(i)
                mdata.visit_finished_task()
                self._remove_task_ref(i)
            else:
                i += 1
