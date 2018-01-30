def svm(data):
    xData = data['x']
    yData = data['y']
    modeltype =0
    clf = NaiveBayes(modeltype)
    clf.fit(xData,yData)
    return clf

def rf(data):
    

def nb(data):
    xData = data['x']
    yData = data['y']
    modeltype =0
    clf = NaiveBayes(modeltype)
    clf.fit(xData,yData)
    return clf


def sort(request):
    if request['type'] == "svm":
        return svm(request['data'])
    elif request['type'] == "nb":
        return svm(request['nb'])
    elif request['type'] == "rf"
        return rf(request['data'])
