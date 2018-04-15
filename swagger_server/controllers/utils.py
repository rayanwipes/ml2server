

def end_client_things(client,json):
    # need to add the thing where the final file gets updated
    ouput_file_info = metadata['files']
    c.update_model(files)
    c.update_metadata(project_name)


class Metadata:
    def __init__(self,json,visitor,client):
        self.json = json
        self.visitor = visitor
        self.client = client

    def visit_finished_task(self):
        self.visitor(self.client,self.json)
