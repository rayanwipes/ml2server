from . import *
from random import *
from swagger_server.algorithms.classifier import *

def get_provisional_score(model, sdata, tdata):
    model.fit(sdata)
    return model.score(tdata)

class SuggestAlgorithm():
    def __init__(self):
        pass

    def suggest_algorithms(self, data, no_rows=None):
        # current = True
        # if current:
            # return [50,60,50,60,50]
        no_sr = min(len(X) * .4, 100) if no_rows is None else no_rows
        no_tr = min(1.5 * no_rows, len(X) - no_rows)
        X, y = data
        shrows = range(len(y))
        shuffle(sample_rows)
        sample_rows = shrows[:no_sr]
        test_rows = shrows[no_sr:no_sr+no_tr]

        X_s = [X[i] for i in sample_rows]
        y_s = [y[i] for i in sample_rows]
        X_t = [X[i] for i in test_rows]
        y_t = [y[i] for i in test_rows]

        ret_list = []
        # now training on the algorithms

        nb_g = NaiveBayes(modeltype=NaiveBayes.GAUSSIAN)
        nb_m = NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL)
        nb_b = NaiveBayes(modeltype=NaiveBayes.BERNOULLI)
        svm = SupportVectorMachine()
        rf = RandomForests()

        return [
            get_provisional_score(m, [X_s, y_s], [X_t, y_t])
                for m in [nb_g, nb_m, nb_b, svm, rf]
        ]
