from sklearn import svm
from sklearn import datasets

import matplotlib.pyplot as plt

"""Class for operations of Support Vector Machines (SVM's)"""
class SupportVectorMachine():

    """Create classifier for SVM"""
    @staticmethod
    def _make_svm_classifier():
        return svm.SVC(gamma=0.001, C=100)

    """Build classifier for SVM"""
    def __init__(self):
        self.classifier = SupportVectorMachine._make_svm_classifier()

    """Trains the SVM on imported data"""
    def fit(self, data, features):
        X, y = data, features
        return self.classifier.fit(X, y)

    """Predicts value of specified data point"""
    def predict(self, data_to_predict):
        return self.classifier.predict(data_to_predict)

    def test(self):
        digits = datasets.load_digits()
        self.fit(digits.data[:-10], digits.target[:-10])
        print("Prediction =", self.predict(digits.data[-2]))
        plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation="nearest")
        plt.show()

if __name__ == "__main__":
    svm = SupportVectorMachine()
    svm.test()

