from sklearn import svm
from sklearn import datasets
from numpy import array_equal

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


def analyse(testing_svm, digits):
    accuracy = 0
    actual = []

    for i in range(-49, 0):
        prediction = testing_svm.predict(digits.data[i].reshape(1, -1))
        actual.append(digits.target[i])
        if array_equal(prediction, actual):
            accuracy += 1
        actual.pop()

    return accuracy


def gamma_value_tests():
    print "Analysis of altering SVM gamma value:"
    digits = datasets.load_digits()
    gamma_values = [1, 0.5, 0.25, 0.1, 0.05, 0.01, 0.001, 0.0001, 0.00001]

    for i in gamma_values:
        svm_gamma1 = SupportVectorMachine(i)
        svm_gamma1.fit(digits.data[:-50], digits.target[:-50])

        print "With a gamma value of ", i, " algorithm correctly predicts ", analyse(svm_gamma1, digits), \
            " out of 50\n"


def fit_size_tests():
    print "Analysis of altering amount of training data:"
    digits = datasets.load_digits()
    # 1797
    fit_sizes = [-1500, -1250, -1000, -750, -500, -250, -100, -50]

    for i in fit_sizes:
        svm_gamma1 = SupportVectorMachine(0.01)
        svm_gamma1.fit(digits.data[:i], digits.target[:i])

        print "Trained on ", i, ", algorithm correctly predicts ", analyse(svm_gamma1, digits), \
            " out of 50\n"

if __name__ == "__main__":
    # svm = SupportVectorMachine(0.01)
    # svm.test()
    # gamma_value_tests()
    fit_size_tests()