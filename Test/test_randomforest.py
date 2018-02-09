#!/usr/bin/env python3

import unittest
from operator import add
from functools import reduce

import import_impl

from randomforest import *


def mean(a):
    return float(reduce(add, a) / len(a))


class RandomForestTest(unittest.TestCase):
    def test_scoring(self):
        a = []
        no_tests = 10
        for i in range(no_tests):
            if i % 5 == 0:
                print(str(i) + "/" + str(no_tests) + " ...")
            rf = RandomForests()
            data = rf.gen_sample_problem()
            train, test = rf.train_test_split(data)
            rf.fit(train, True)
            # print("model size: ", len(rf.dump_model()))
            a += [rf.score(test)]
            if i % 5 == 4:
                print(a[-5:])
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
        print(confusion_matrix(y, y_pred))
        return accuracy_score(y, y_pred)

    def test_iris(self):
        self.assertGreater(
            self.accuracy_check("iris", load_iris(return_X_y=True)),
            .94999)

    def test_diabetes(self):
        self.assertGreater(
            self.accuracy_check("diabetes", load_diabetes(return_X_y=True)),
            .94999)

    def test_breast_cancer(self):
        self.assertGreater(
            self.accuracy_check(
                "breast cancer",
                load_breast_cancer(return_X_y=True)),
            .94999)


if __name__ == "__main__":
    unittest.main()
