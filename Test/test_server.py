import unittest
import os
import import_impl
from server import * 
import json

class BasicTests(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_main_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_model_route(self):
        params = {'algorithm': 'naive-bayes'}
        response = self.app.post('/training/123212', data=json.dumps(params))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data, "redirect")
        print("-")
        print("Traning model redirects route to backend to store")
        print("-------------------------------------------------")

    def test_status_model(self):
        response = self.app.get('/training/123212', data={})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['data']['percent_trained'], 0)
        print("-")
        print("Fetch status of a model traning")
        print("-----------------------------------------------")

    
    def test_delete_model(self):
        response = self.app.delete('training/123212', data={})
        self.assertEqual(response.status_code, 200)
        print("-")
        print("Delete route works")
        print("-----------------------------------------------")

    def test_model_prediction(self):
        params = {'input_data': '2132331232'}
        response = self.app.get('/model/121321/prediction', data=json.dumps(params))
        self.assertEqual(response.status_code, 200)
        print("-")
        print("Prediction route returns 200 status code")
        print("----------------------------------------------")

    def test_suggest_model(self):
        response = self.app.get('/suggest', data="2121321")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data, "naive")
        print("-")
        print("Suggest model returns model selected")
        print("----------------------------------------------")
        


if __name__ == "__main__":
    unittest.main()
