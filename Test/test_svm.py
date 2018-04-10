#!/usr/bin/env python3

from numpy import array_equal
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

import import_impl
import unittest

from svm import *
from problem_generator import *


def analyse(testing_svm, digits):
    accuracy = 0
    actual = []
    for i in range(-49, 0):
        prediction = testing_svm.predict(digits.data[i].reshape(1, -1))
        actual.append(digits.target[i])
        if array_equal(prediction, actual):
            accuracy += 1
        actual.pop()
    return (accuracy/50.0)*100


class SVMUnitTests(unittest.TestCase):
    def test_SVM_Functionality(self):
        print("\n############################################################")
        print("Testing SVM functionality:")
        digits = datasets.load_digits()
        test_svm = SupportVectorMachine()
        test_svm.fit([digits.data, digits.target])
        predicted_values = test_svm.predict(digits.data)

        print(metrics.classification_report(digits.target, predicted_values))
        print("\nAccuracy: " +
              str(metrics.accuracy_score(digits.target, predicted_values)))
        print("F-Score: " + str(metrics.f1_score(digits.target,
                                                 predicted_values,
                                                 average='macro')) + "\n")
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(digits.target, predicted_values)) +
              "\n")
        print("############################################################")

    def test_SVM_Accuracy(self):
        print("\n############################################################")
        print("Checking default SVM settings accuracy (Gamma value=0.001," +
              " C=10, and trained on 75% of the data):")
        digits = datasets.load_digits()
        test_svm = SupportVectorMachine()

        X_train, X_val, y_train, y_val = train_test_split(
            digits.data, digits.target, test_size=0.75, random_state=1)

        test_svm.fit([X_train, y_train])
        predicted_values = test_svm.predict(X_val)

        print(metrics.classification_report(y_val, predicted_values))
        print("\nAccuracy: " + str(metrics.accuracy_score(
                                                          y_val,
                                                          predicted_values)))
        print("F-Score: " + str(metrics.f1_score(y_val,
                                                 predicted_values,
                                                 average='macro')) + "\n")
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(y_val, predicted_values)) + "\n")
        print("############################################################")

    def test_SVM_Regressor(self):
        print("\n############################################################")
        print("Testing SVM regressor:")
        X, y = gen_sample_problem(PROBLEM_REGRESSION)
        test_svm = SupportVectorMachine()
        train, test = test_svm.train_test_split([X, y])
        test_svm.fit(train)
        predicted_values = test_svm.predict(X)

        print("\nAccuracy: ", test_svm.score(test))
        print("############################################################")

    def test_gamma_value(self):
        print("\n############################################################")
        print("Analysis of altering SVM gamma value:")
        digits = datasets.load_digits()
        gamma_values = [1, 0.5, 0.25, 0.1, 0.05, 0.01, 0.001, 0.0001, 0.00001]
        for i in gamma_values:
            svm_gamma = SupportVectorMachine(i, 100)
            svm_gamma.fit([digits.data[:-50], digits.target[:-50]])
            print("With a gamma value of ",
                  i, " algorithm correctly predicts ",
                  analyse(svm_gamma, digits), "%")
        print("############################################################")

    def test_fit_size(self):
        print("\n############################################################")
        print("Analysis of altering amount of training data:")
        digits = datasets.load_digits()
        # 1797
        fit_sizes = [-1500, -1250, -1000, -750, -500, -250, -100, -50]
        for i in fit_sizes:
            svm_fit = SupportVectorMachine(0.01, 100)
            svm_fit.fit([digits.data[:i], digits.target[:i]])
            print("Trained on ", i, ", algorithm correctly predicts ",
                  analyse(svm_fit, digits), "%")
        print("############################################################")

    def test_c_value(self):
        print("\n############################################################")
        print("Analysis of altering C values:")
        digits = datasets.load_digits()
        c_values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

        for i in c_values:
            svm_c = SupportVectorMachine(0.001, i)
            svm_c.fit([digits.data[:-50], digits.target[:-50]])

            print("With C value of ", i, " accuracy is ",
                  analyse(svm_c, digits), "%")
        print("############################################################")

    def test_combined(self):
        print("\n############################################################")
        print("Analysis of both tests combined:")
        digits = datasets.load_digits()
        gamma_values = [1, 0.5, 0.25, 0.1, 0.05, 0.01, 0.001, 0.0001, 0.00001]
        c_values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
        fit_sizes = [-1500, -1250, -1000, -750, -500, -250, -100, -50]

        for i in gamma_values:
            for j in c_values:
                for k in fit_sizes:
                    svm_combined = SupportVectorMachine(i, j)
                    svm_combined.fit([digits.data[:k], digits.target[:k]])

                    print("With gamma value of ", i, "and C value of ", j,
                          " and training size of ", k,
                          " overall accuracy is: ",
                          analyse(svm_combined, digits), "%")
        print("############################################################")


if __name__ == "__main__":
    unittest.main()
