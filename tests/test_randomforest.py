#!/usr/bin/env python3

import unittest
from operator import add

from randomforests import *


class RandomForestTest(unittest.TestCase):
    def mean(a):
        return float(reduce(add, a) / len(a))

    def test_scoring(self):
        rf = RandomForests()
        a = []
        for i in range(10):
            if i % 10 == 0:
                print(i, "...")
            data = rf.gen_sample_problem()
            train, test = rf.train_test_split(data)
            rf.fit(train, True)
            print("model size: ", len(rf.dump_model()))
            a += [rf.score(test)]
        print(len(a))
        print(sorted(a)[:10])
        fail_rate = float(len([x for x in a if x < .94999]))
        print(str(100. * (1. - fail_rate) / len(a))) + "%")
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
            accuracy_check("iris", load_iris(return_X_y=True)),
            .94999)

    def test_diabetes(self):
        self.assertGreater(
            accuracy_check("diabetes", load_diabetes(return_X_y=True)),
            .94999)

    def test_breast_cancer(self):
        self.assertGreater(
            accuracy_check(
                "breast cancer",
                load_breast_cancer(return_X_y=True)),
            .94999)


if __name__ == "__main__":
    unittest.main()
