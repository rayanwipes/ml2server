from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
from numpy import array_equal

import matplotlib.pyplot as plt


# Class for operations of Support Vector Machines (SVM's)
class SupportVectorMachine():

    # Create classifier for SVM
    @staticmethod
    def _make_svm_classifier(gamma_value, c_value):
        return svm.SVC(gamma=gamma_value, C=c_value)

    # Build classifier for SVM
    def __init__(self, gamma_value=0.001, c_value=10, **kwargs):
        SVM = SupportVectorMachine
        self.classifier = None
        for k in kwargs:
            v = kwargs[k]
            if k == 'filename':
                self.classifier = joblib.load(v)
        if self.classifier is None:
            self.classifier = SVM._make_svm_classifier(gamma_value, c_value)

    # Serialize model into a string
    def dump_model(self):
        return pickle.dumps(self.clf)

    # Saves model to file
    def save_model(self, filename):
        joblib.dump(self.classifier, filename)

    # Split train and test data
    def train_test_split(self, data, ratio=.4):
        X, y = data
        x1, x2, y1, y2 = train_test_split(
            X, y,
            test_size=ratio,
            random_state=0)
        return [[x1, y1], [x2, y2]]

    # Trains the SVM on imported data"""
    def fit(self, train_data):
        X, y = train_data
        return self.classifier.fit(X, y)

    # Get feature importances
    def feature_importances(self):
        return self.clf.feature_importances_

    # Obtain score on the given test data
    def score(self, test_data):
        X, y = test_data
        return self.clf.score(X, y)

    # Predicts value of specified data point
    def predict(self, data_to_predict):
        return self.classifier.predict(data_to_predict)

    def test(self):
        digits = datasets.load_digits()
        self.fit(digits.data[:-10], digits.target[:-10])
        print("Prediction =", self.predict(digits.data[-2]))
        print("Actual =", digits.target[-2])
        plt.imshow(digits.images[-2], cmap=plt.cm.gray_r,
                   interpolation="nearest")
        plt.show()
