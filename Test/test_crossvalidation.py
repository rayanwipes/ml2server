import unittest
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
import import_impl
from cross_validation import *
from randomforest import *
from sklearn import naive_bayes


class CrossValidationTest(unittest.TestCase):
    def setUp(self):
        self.iris = datasets.load_iris()
        self.x_train, self.X_test, self.y_train, self.y_test = \
            train_test_split(self.iris.data, self.iris.target,
                             test_size=0.3, random_state=0)

    def testSVM(self):
        clf = svm.SVC(C=1)
        test_cross = CrossValidation(clf)
        scores = test_cross.score([self.iris.data, self.iris.target], cv=3)
        print("Cross validation with the svm algorithm working")

    def testRandomForests(self):
        random_forest = RandomForests()
        test_cross = CrossValidation(random_forest.clf)
        scores = test_cross.score([self.iris.data, self.iris.target], cv=3)
        print("Cross validation with random forests works")

    def testNaiveBayesGaussian(self):
        gaussian = naive_bayes.GaussianNB()
        test_cross = CrossValidation(gaussian)
        scores = test_cross.score([self.iris.data, self.iris.target], cv=3)
        print("Cross validation with Naive Bayes Gaussian")

    def testNaiveBayesMultinomial(self):
        multinomial = naive_bayes.MultinomialNB()
        test_cross = CrossValidation(multinomial)
        scores = test_cross.score([self.iris.data, self.iris.target], cv=3)
        print("Cross validation with Naive Bayes Multinomial")


if __name__ == "__main__":
    unittest.main()
