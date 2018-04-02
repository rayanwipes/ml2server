import pandas as pd
import csv


# Things written for the future, if this has to be used
OP_FIT, OP_SCORE, OP_PREDICT = range(3)
MDL_NAIVE_BAYES_GAUSSIAN, MDL_NAIVE_BAYES_MULTINOMIAL, \
    MDL_NAIVE_BAYES_BERNOULLI, MDL_RANDOM_FOREST, MDL_SVM = range(5)


# cursory removing all empty rows, in the future, more careful data pruning
# will be used
def clean_data(request):
    df = pd.DataFrame(request)
    df.dropna(axis=0, how="any")
    return df
    # print(df)


def create_model(model_type):
    if model_type == MDL_NAIVE_BAYES_GAUSSIAN:
        model = NaiveBayes(NaiveBayes.TYPE_GAUSSIAN,
                           model_type, existing_model)
    elif model_type == MDL_NAIVE_BAYES_MULTINOMIAL:
        model = NaiveBayes(NaiveBayes.TYPE_MULTINOMIAL,
                           model_type, existing_model)
    elif model_type == MDL_NAIVE_BAYES_BERNOULLI:
        model = NaiveBayes(NaiveBayes.TYPE_BERNOULLI,
                           model_type, existing_model)
    elif model_type == MDL_NAIVE_BAYES_RANDOM_FOREST:
        model = RandomForests(model_type, existing_model)
    elif model_type == MDL_NAIVE_BAYES_SVM:
        model = SVM(model_type, existing_model)
    else:
        raise Exception("Non compatible model type")

    return model


def fit(data, model):
    model.fit(data)
    return model


def predict(x_data, model):
    return model.predict(x_data)


def cross_validate(model, x_Data, y_Data, k=None):
    score = k
    if k is None:
        score = 5
    # Validation function and macros will change depending upon what type of
    # data, classifier is being used
    scores = cross_val_score(model, x_Data, y_Data, cv=score)
    return scores


def score(model, X_data):
    model.score(X_data)


# Multiple arguments if needed for the future, it has all of the
# functionality of the above
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

    if operation is None or model_type is None:
        raise Exception("No model type provided")

    model = None
    # getDataFromFile in the fit bit
    if model_type == MDL_NAIVE_BAYES_GAUSSIAN:
        model = NaiveBayes(NaiveBayes.TYPE_GAUSSIAN,
                           model_type, existing_model)
    elif model_type == MDL_NAIVE_BAYES_MULTINOMIAL:
        model = NaiveBayes(NaiveBayes.TYPE_MULTINOMIAL,
                           model_type, existing_model)
    elif model_type == MDL_NAIVE_BAYES_BERNOULLI:
        model = NaiveBayes(NaiveBayes.TYPE_BERNOULLI,
                           model_type, existing_model)
    elif model_type == MDL_RANDOM_FOREST:
        model = RandomForests(model_type, existing_model)
    elif model_type == MDL_SVM:
        model = SVM(model_type, existing_model)
    else:
        raise Exception("Broken Model Type")

    return model

    if operation == OP_FIT:
        data = getData(data_filename)
        model.fit(data)
    elif operation == OP_SCORE:
        # will need to give it an x and y
        data = getData(data_filename)
        model.score(data)
    elif operation == OP_PREDICT:
        if X is None:
            raise Exception("No X value given to predict from")
        model.predict(X)
    else:
        raise Exception("Operation not recognised")
