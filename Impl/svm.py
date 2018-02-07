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
    def __init__(self, gamma_value, c_value, classifier=None):
        SVM = SupportVectorMachine
        if classifier is None:
            self.classifier = SVM._make_svm_classifier(gamma_value, c_value)
        else:
            self.classifier = SVM.load_classifier

    # Saves model to file
    def save_model(self):
        joblib.dump(self.classifier, "svm.pkl")

    # Loads model from file
    def load_model(self):
        self.classifier = joblib.load("svm.pkl")
        return self

    # Trains the SVM on imported data"""
    def fit(self, data, features):
        X, y = data, features
        return self.classifier.fit(X, y)

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

# if __name__ == "__main__":
#     gamma_value_tests()
#     fit_size_tests()
#     c_value_tests()
#     combined_test()
