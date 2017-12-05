from flask import request

def getHeaderValue(name):
    ret = request.headers.get(name)
    dataset = requests.headers.get("dataset")
    if ret = 'NB':
        return naive_bayes(dataset)
    elif ret = "RF":
        return random_forests(dataset)
    elif ret = "SVM":
        return support_vector_machines(dataset)
    elif ret = "KFOLD":
        return;
