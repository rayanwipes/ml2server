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
        'version': "",
        'namespaces': {
            'ML2': {
                'model_store_dir': ""
            }
        }
    })

    def requestData(self, projectName, filename):
        r = requests.get(projectName+"/"+filename)
        if r.status_code is not 200:
            return None, r.status_code
        else:
            return r.data, r.status_code

    def requestModel(self, path, filename):
        r = requests.get(path)
        if r.status_code is not 200:
            return r.status_code
        else:
            fileTemp = open(filename)
            fileTemp.write(r.data)
            return filename, r.status_code

    # This is a post
    def sendMetadata(self, path):
        r = requests.get(path)
        if r.status_code is not 200:
            return r.status_code
        else:
            newMeta = r.json
            newMeta['version'] = newMeta['version'] + 1
            r = requests.post(path+"?action=update", data=newMeta)
            if r.status_code is not 200:
                return r.status_code

    def createModel(self, path, id):
        r = requests.post(path+"?action=create")
        if r.status_code is not 200:
            return r.status_code

    def updateModel(self, path, modelData, id):
        r = requests.post(path)
        if r.status_code is not 200:
            return r.status_code
        else:
            self.sendMetadata(path)

    def deleteModel(self, path, id):
        r = requests.post(path+"?action=delete")
        if r.status_code is not 200:
            return r.status_code
        return "success"

cli = Client()
lisat = [1]
nice, stuff = cli.requestData("https://138.251.29.186:8080","")
print(nice + stuff)