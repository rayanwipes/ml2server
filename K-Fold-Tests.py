import unittest


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import metrics

class MyTest(unittest.TestCase):
    # To DO
    def setUp(self):
        self.iris = datasets.load_iris()
        self.iris.data.shape, iris.target.shape

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            iris.data, iris.target, test_size=0.4, random_state=0)

        self.X_train.shape, self.y_train.shape

        self.X_test.shape, self.y_test.shape


# test
    def test1(self):
        clf = svm.SVC(kernel='linear', C=1).fit(self.X_train, self.y_train)
        score = clf.score(self.X_test, self.y_test)
        print(score)

    def test2(self):
        clf = svm.SVC(kernel='linear', C=1)
        scores = cross_val_score(clf, iris.data, iris.target, cv=5)
        print(scores)
        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
        scores = cross_val_score(clf, iris.data, iris.target, cv=5, scoring='f1_macro')
        print(scores)


if __name__ == "__main__":
    unittest.main()
