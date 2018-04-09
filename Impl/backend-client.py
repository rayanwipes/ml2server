import requests
import json

class Client:

    fileMeta = json.dumps({
        "file_path": "",
        "file_name": "",
        "id": "",
        "supported_views": {},
        "type": "",
        "metadata": "",
        "status": ""
    })

    projectMeta = json.dumps({
        'version' : "",
        'namespaces' : {
            'ML2' : {
                'model_store_dir' : ""
            }
        }
    })

    def requestData(self,path):
        r = requests.get(path)
        if r.status_code is not 200:
            return r.status_code

    def requestModel(self,path):
        r = requests.get(path)
        if r.status_code is not 200:
            return r.status_code


    # This is a post
    def sendMetadata(self,path):
        r = requests.get(path)
        if r.status_code is not 200:
            return r.status_code
        else:
            newMeta = r.json
            newMeta['version'] = newMeta['version'] + 1
            r = requests.post(path+"?action=update",data = newMeta)
            if r.status_code is not 200:
            return r.status_code


    def createModel(self,path):
        r = requests.post(path+"?action=create")
        if r.status_code is not 200:
            return r.status_code


    def updateModel(self,path, modelData):
        r = requests.post(path)
        if r.status_code is not 200:
            return r.status_code
        else:
            sendMetadata(path)

    def deleteModel(self,path):
        return 1

