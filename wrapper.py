import pandas as pd
import csv
def getData(request):
    df = pd.DataFrame(request)
    df.dropna(axis=0,how="any")
    return df
    # print(df)

'''
Differing formats for the wrapper functions
'''
def svm(data):
    xData = data['x']
    yData = data['y']
    modeltype =0
    clf = SupportVectorMachines(modeltype)
    clf.fit(xData,yData)
    return clf

def rf(data):
    xData = data['x']
    yData = data['y']
    modeltype =0
    clf = RandomForests(modeltype)
    clf.fit(xData,yData)
    return clf

def nb(data):
    xData = data['x']
    yData = data['y']
    modeltype =0
    clf = NaiveBayes(modeltype)
    clf.fit(xData,yData)
    return clf


OP_TRAIN,OP_FIT,OP_SCORE,OP_PREDICT = range(4)
MDL_NAIVE_BAYES_GAUSSIAN, MDL_NAIVE_BAYES_MULTINOMIAL,MDL_NAIVE_BAYES_BERNOULLI, MDL_RANDOM_FOREST, MDL_SVM = range(5)

def sort(operation,model_type,data_fName,existing_model=None):
    model = None
    if model_type = MDL_NAIVE_BAYES_GAUSSIAN:

    elif model_type = MDL_NAIVE_BAYES_MULTINOMIAL:
    elif model_type = MDL_NAIVE_BAYES_BERNOULLI:
    elif model_type = MDL_NAIVE_BAYES_RANDOM_FOREST:
    elif model_type = MDL_NAIVE_BAYES_SVM:    



    # deal with issues
    # getting data in the response

    # convert the data format to a dictionary
    # with the correct headers in place


    readers = csv.reader(open('fName.csv', newline=''), delimiter=',', quotechar='|')
    fName = request['fName']
    # This was done if there was a header in the file
    print(readers.__next__())

    dictionary= {'x': [],'y': []}
    for row in readers:
        dictionary['x'].append(row[0])
        dictionary['y'].append(row[1])

    newDF = getData(dictionary)
