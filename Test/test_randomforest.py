#!/usr/bin/env python3

import unittest
from operator import add
from functools import reduce
import matplotlib.pyplot as plt
from random import randint

import import_impl

from randomforest import *
from problem_generator import *
from roc_curve import *


def mean(a):
    return float(reduce(add, a) / len(a))


class RandomForestTest(unittest.TestCase):
    def test_scoring(self):
        print("Random Forest functionality test:")
        a, b = [], []
        no_tests = 10
        for i in range(no_tests):
            if i % 5 == 0:
                print(str(i) + "/" + str(no_tests) + " ...")
            rf = RandomForests()
            problem_type = [
                PROBLEM_CLASSIFICATION, PROBLEM_REGRESSION
            ][randint(0, 1)]
            X, y = gen_sample_problem(problem_type)
            train, test = rf.train_test_split([X, y])
            rf.fit(train)
            y_pred = rf.predict(X)
            # print("model size: ", len(rf.dump_model()))
            a += [rf.score(test)]
            if type_of_target(y) != 'continuous':
                b += [f1_score(y, y_pred)]
            if i % 5 == 4:
                print(a[-5:])
                # print(b[-5:])
        print(len(a))
        print(sorted(a)[:10])
        print("Mean: ", mean(a))
        self.assertGreater(mean(a), .7999)

    def accuracy_check(self, name, data):
        print("DATA: " + name)
        rf = RandomForests()
        X, y = data
        rf.fit([X, y])
        y_pred = rf.predict(X)
        print(classification_report(y, y_pred))
        print("Accuracy: " + str(accuracy_score(y, y_pred)) + "\n")
        if type_of_target(y_pred) == 'continuous':
            print("F-Score: " + str(f1_score(y, y_pred, average='macro')) +
                  "\n")
        print("Confusion Matrix:\n" + str(confusion_matrix(y, y_pred)) + "\n")

        if len(set(y_pred)) == 2:
            generate_roc_graph(y, y_pred, 'Receiver Operating Characteristics for ' + name + ' data')

        print("############################################################")
        return accuracy_score(y, y_pred)

    def test_iris(self):
        print("\n############################################################")
        print("Testing model accuracy against Iris data set:")
        self.assertGreater(
            self.accuracy_check("iris", load_iris(return_X_y=True)),
            .94999)

    def test_diabetes(self):
        print("\n############################################################")
        print("Testing model accuracy against Diabetes data set:")
        self.assertGreater(
            self.accuracy_check("diabetes", load_diabetes(return_X_y=True)),
            .94999)

    def test_breast_cancer(self):
        print("\n############################################################")
        print("Testing model accuracy against Breast Cancer data set:")
        self.assertGreater(
            self.accuracy_check(
                "breast cancer",
                load_breast_cancer(return_X_y=True)),
            .94999)


if __name__ == "__main__":
    plt.switch_backend('agg')
    unittest.main()
