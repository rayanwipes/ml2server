import pandas as pd
import csv
# cursory removing all empty rows, in the future, more careful consideration will be used,
def getData(request):
    df = pd.DataFrame(request)
    df.dropna(axis=0,how="any")
    return df
    # print(df)

OP_FIT,OP_SCORE,OP_PREDICT = range(4)
MDL_NAIVE_BAYES_GAUSSIAN, MDL_NAIVE_BAYES_MULTINOMIAL,MDL_NAIVE_BAYES_BERNOULLI, MDL_RANDOM_FOREST, MDL_SVM = range(5)

def create_model(model_type):
        if model_type = MDL_NAIVE_BAYES_GAUSSIAN:
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
            raise Exception("Broken Model Type")

        return model

def fit(data, model):
    model.fit(data)
    return model

def predict(x_data,model):



# Multiple arguments
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
        raise Exception("No model type provided")


    model = None
    # getDataFromFile in the fit bit

    if operation == OP_FIT:
        data = getData(data_filename)
        model.fit(data)
    elif operation == OP_SCORE:
        # will need to give it an x and y
        data = getData(data_filename)
        model.score(data)
    elif operation == OP_PREDICT:
        if X == None:
            raise Exception("No X value given to predict from")
        model.predict(X)
    else:
        raise Exception("GREAT SCOTT MARTY")
