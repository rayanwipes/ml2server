from sklearn import svm
from sklearn import datasets

import matplotlib.pyplot as plt

"""Class for operations of Support Vector Machines (SVM's)"""
class SupportVectorMachine():

    """Create classifier for SVM"""
    @staticmethod
    def _make_svm_classifier(gamma_value):
        return svm.SVC(gamma=gamma_value, C=100)

    """Build classifier for SVM"""
    def __init__(self, gamma_value):
        self.classifier = SupportVectorMachine._make_svm_classifier(gamma_value)

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
        print ("Actual =", digits.target[-2])
        plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation="nearest")
        plt.show()


def gamma_value_tests():
    print "Analysis of altering SVM gamma value:"
    print "Gamma value= 1"
    digits = datasets.load_digits()
    svm_gamma1 = SupportVectorMachine(0.01)
    svm_gamma1.fit(digits.data[:-10], digits.target[:-10])
    accuracy1 = 0

    for i in range(-9, 0):
        prediction = svm_gamma1.predict(digits.data[i].reshape(1,-1))
        print "Prediction for ", i, prediction
        print "Actual= ", digits.target[i]
        if prediction == digits.target[i]:
            accuracy1 + 1

    print accuracy1


if __name__ == "__main__":
    # svm = SupportVectorMachine(0.01)
    # svm.test()
    gamma_value_tests()
