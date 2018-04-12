

class Client():

    def __init__(self):
        pass

    def request_data(self,input_columns):
        return "hello",200

    def request_model(self,model_id,project_name):
        return "data stuff",200

    def create_model(self,uuid,project_name):
        return "model created boys",200

    def update_model(self,project_name,uuid,the_data_to_update):
        return "it worked",200

    def delete_model(self,model_id,project_name):
        return "it worked",200

    def remove_from_metadata(self,model_id,project_name):
        return "it worked",200

    def get_metadata(self,project_name):
        return "you're authorised",200


stuff = "potato"
