from swagger_server.algorithms.svm import *
from swagger_server.algorithms.randomforest import *
from swagger_server.algorithms.naivebayes import *


class Classifier:
    def __init__(self, **kwargs):
        self.clf = None
        clftype, fname, binary = [None] * 3
        for k in kwargs:
            v = kwargs[k]
            if k == 'classifier':
                clftype = v
            elif k == 'filename':
                fname = v
            elif k == 'binary':
                binary = v
        SVM = SupportVectorMachine
        if clftype == RandomForests:
            if fname is not None:
                self.clf = RandomForests(filename=fname)
            elif binary is not None:
                self.clf = RandomForests(binary=binary)
            else:
                self.clf = RandomForests()
        elif clftype == SVM:
            if fname is not None:
                self.clf = SVM(filename=fname)
            elif binary is not None:
                self.clf = SVM(binary=binary)
            else:
                self.clf = SVM()
        elif clftype == NaiveBayes:
            self.clf = NaiveBayes(modeltype=kwargs['modeltype'])
        else:
            raise Exception("unknown classifier: " + str(clftype))

    def dump_model(self):
        return self.clf.dump_model()

    def save_model(self, filename):
        self.clf.save_model(filename)

    def train_test_split(self, data, ratio=.4):
        return self.clf.train_test_data(data, ratio)

    def fit(self, data):
        return self.clf.fit(data)

    def feature_importances(self):
        return self.clf.feature_importances()

    def score(self, test_data):
        return self.clf.score(test_data)

    def predict(self, X):
        return self.clf.predict(X)


if __name__ == "__main__":
    c = Classifier(classifier=RandomForests)
    print(c.clf)
