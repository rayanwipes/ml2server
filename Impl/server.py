from flask import Flask
app = Flask(__name__)
from flask import request
from flask import jsonify
import json
import algorithms

@app.route("/")
def main():
	return "hello"

@app.route('/training/<model_id>', methods=["POST"])
def create_model(model_id):
    data        = json.loads(request.data)
    algorithm   = data['algorithm']
    if (algorithm == "naive-bayes"):
        model = algorithms.naive(data)
    elif (algorithm == ""):
        model = algorithms.whatnot(data)
    else:
        return 401
    #send to backend
    return jsonify("redirect")

@app.route('/training/<model_id>')
def get_status(model_id):
    #fetch status
    return jsonify({"data": { "percent_trained": 0}})

@app.route('/training/<model_id>', methods=["DELETE"])
def stop_model(model_id):
    #stop it
    return jsonify(200)

@app.route('/model/<model_id>/prediction')
def predict(model_id):
    input_uuid = json.loads(request.data)['input_data']
    if (input_uuid):
        return jsonify(algorithms.whatever(model_id, input_uuid))
    else: 
        return jsonify("No input data parameter")

@app.route('/suggest')
def suggest():
    data = json.loads(request.data)
    prediction = "naive"
    return jsonify(prediction)

