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

# Init The Client
    def __init__(self, auth_name, token_value, endpoint):
        self.auth = {auth_name: token_value}
        self.endpoint = endpoint

    def requestData(self, projectName, filename):
        r = requests.get(self.endpoint + "/" + projectName + "/files/" +
                         filename, headers=self.auth)
        if r.status_code is not 200:
            return r.status_code, r.text
        else:
            return r.status_code, r.text

    def requestDataByID(self, projectName, filename, id):
        r = requests.get(self.endpoint + "/" + projectName +
                         "/files_by_id/" + id, headers=self.auth)
        if r.status_code is not 200:
            return r.status_code, r.text
        else:
            return r.status_code, r.text

    # This is a post
    def sendMetadata(self, projectName, filename):
        r = requests.get(self.endpoint + "/" + projectName + "/files/" +
                         filename + "?view=meta", headers=self.auth)
        if r.status_code is not 200:
            return r.status_code, r.text
        else:
            newMeta = r.json
            newMeta['version'] = newMeta['version'] + 1
            r = requests.post(path + "?action=update", data=newMeta)
            if r.status_code is not 200:
                return r.status_code, r.text

    def sendMetadataByID(self, projectName, id):
        r = requests.post(self.endpoint + "/" + projectName + "/files_by_id/" +
                          id + "?view=meta", headers=self.auth)
        if r.status_code is not 200:
            return r.status_code, r.text
        else:
            newMeta = r.json
            newMeta['version'] = newMeta['version'] + 1
            r = requests.post(path+"?action=update", data=newMeta)
            if r.status_code is not 200:
                return r.status_code, r.text

    def createModel(self, projectName, filename):
        payload = {'some': 'data'}
        r = requests.post(self.endpoint + "/" + projectName + "/files/" +
                          filename + "?action=upload", headers=self.auth)
        if r.status_code is not 200:
            return r.status_code, r.text
        return r.status_code, r.text

    def createModelByID(self, projectName, filename, id):
        payload = {'some': 'data'}
        r = requests.post(self.endpoint + "/" + projectName + "/files_by_id/" +
                          id + "?action=upload",
                          headers=self.auth, data=json.dumps(payload))
        if r.status_code is not 200:
            return r.status_code, r.text
        return r.status_code, r.text

    def updateModel(self, projectName, filename):
        # Need to look at specifics of sending a raw file
        r = requests.post(self.endpoint + "/" + projectName + "/" + filename +
                          "?action=upload", headers=self.auth)
        if r.status_code is not 200:
            return r.status_code, r.text
        else:
            self.sendMetadata(path)

    def updateModelByID(self, projectName, filename, id):
        # Need to look at specifics of sending a raw file
        r = requests.post(self.endpoint + "/" + projectName + "/files_by_id/" +
                          id + "?action=upload", headers=self.auth)
        if r.status_code is not 200:
            return r.status_code, r.text
        else:
            self.sendMetadata(path)

    def deleteModel(self, projectName, id):
        r = requests.post(self.endpoint + "/" + projectName + "/files_by_id/" +
                          id+"?action=delete", headers=self.auth)
        return r.status_code, r.text


cli = Client("Authorization", "Bearer 0ac78004-1fa6-4f81-b988-3946e8fd989e",
             "http://138.251.29.105:8080")
user = {"Authorization": "Bearer 0ac78004-1fa6-4f81-b988-3946e8fd989e"}
indeed, text = cli.createModel("testProject", "dnasfasfagos")
nice, stuff = cli.requestData("testProject", "dingoasga")
parsed = json.loads(nice)
print(json.dumps(parsed, indent=4, sort_keys=True))
print(stuff)
parsed = json.loads(text)
print(json.dumps(parsed, indent=4, sort_keys=True))
print indeed
