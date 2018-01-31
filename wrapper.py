import pandas as pd
import csv
def getData(request):
    df = pd.DataFrame(request)
    df.dropna(axis=0,how="any")
    print(df)

def svm(data):
    xData = data['x']
    yData = data['y']
    modeltype =0
    clf = NaiveBayes(modeltype)
    clf.fit(xData,yData)
    return clf

def rf(data):
    return

def nb(data):
    xData = data['x']
    yData = data['y']
    modeltype =0
    clf = NaiveBayes(modeltype)
    clf.fit(xData,yData)
    return clf


def sort(request):
    data = getData(request)

    if request['type'] == "svm":
        return svm(data)
    elif request['type'] == "nb":
        return svm(data)
    elif request['type'] == "rf":
        return rf(data)

spamReader = csv.reader(open('publisher.csv', newline=''), delimiter=',', quotechar='|')

print(spamReader.__next__())

test= {'x': [],'y': []}
for row in spamReader:
    test['x'].append(row[0])
    test['y'].append(row[1])

getData(test)
