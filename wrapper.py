import pandas as pd
import csv
def getData(request):
    df = pd.DataFrame(request)
    df.dropna(axis=0,how="any")
    return df
    # print(df)

# '''
# Differing formats for the wrapper functions
# '''
# def svm(data):
#     xData = data['x']
#     yData = data['y']
#     modeltype =0
#     clf = SupportVectorMachines(modeltype)
#     clf.fit(xData,yData)
#     return clf
#
# def rf(data):
#     xData = data['x']
#     yData = data['y']
#     modeltype =0
#     clf = RandomForests(modeltype)
#     clf.fit(xData,yData)
#     return clf
#
# def nb(data):
#     xData = data['x']
#     yData = data['y']
#     modeltype =0
#     clf = NaiveBayes(modeltype)
#     clf.fit(xData,yData)
#     return clf


OP_FIT,OP_SCORE,OP_PREDICT = range(4)
MDL_NAIVE_BAYES_GAUSSIAN, MDL_NAIVE_BAYES_MULTINOMIAL,MDL_NAIVE_BAYES_BERNOULLI, MDL_RANDOM_FOREST, MDL_SVM = range(5)

def sort(**kwargs):
    operation = None
    model_type = None
    model_filename = None
    data_filename, X = None, None
    for key in kwargs:
        value = kwargs[key]
        if key == 'operation':
            operation = value
        elif key == 'data_filename':
            data_filename = value
        elif key == 'model_type':
            model_type = value
        elif key == 'X':
            X = value
        elif key == 'model_filename':
            model_filename = value
        else:
            pass

    if operation == None or model_type == None:
        raise Exception("YOU MERELY ADOPTED THE DARKNESS, I WAS BORN IN IT, RAISED BY IT, I DIDN'T SEE THE LIGHT UNTIL I WAS A MAN ")


    model = None

    if model_type = MDL_NAIVE_BAYES_GAUSSIAN:
        #FIX
        model = NaiveBayes(NaiveBayes.TYPE_GAUSSIAN, model_type, existing_model)
    elif model_type = MDL_NAIVE_BAYES_MULTINOMIAL:
        model = NaiveBayes(NaiveBayes.TYPE_MULTINOMIAL, model_type, existing_model)
    elif model_type = MDL_NAIVE_BAYES_BERNOULLI:
        model = NaiveBayes(NaiveBayes.TYPE_BERNOULLI, model_type, existing_model)
    elif model_type = MDL_NAIVE_BAYES_RANDOM_FOREST:
        model = RandomForests(model_type, existing_model)
    elif model_type = MDL_NAIVE_BAYES_SVM:
        model = SVM(model_type, existing_model)
    else:
        raise Exception("Houston we've had a problem")

    # getDataFromFile in the fit bit

    if operation == OP_FIT:
        data = getData(data_filename)
        model.fit(data)
    elif operation == OP_SCORE:
        #might need to give it an x and y
        data = getData(data_filename)
        model.score(data)
    elif operation == OP_PREDICT:
        if X == None:
            raise Exception("YOU'RE GONNA NEED A BIGGER BOAT")
        model.predict(X)
    else:
        raise Exception("GREAT SCOTT MARTY")



    # deal with issues
    # getting data in the response

    # convert the data format to a dictionary
    # with the correct headers in place


    # readers = csv.reader(open('fName.csv', newline=''), delimiter=',', quotechar='|')
    # fName = request['fName']
    # # This was done if there was a header in the file
    # print(readers.__next__())
    #
    # dictionary= {'x': [],'y': []}
    # for row in readers:
    #     dictionary['x'].append(row[0])
    #     dictionary['y'].append(row[1])
    #
    # newDF = getData(dictionary)
