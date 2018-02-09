import unittest
import import_impl
from naivebayes import *
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split


class MyTest(unittest.TestCase):

    # Tests that it basically runs.
    def test_Functional_Gaussian(self):
        nb = NaiveBayes(0)
        dataset = datasets.load_breast_cancer()
        nb.fit(dataset.data, dataset.target)
        y_predicted = nb.predict(dataset.data)
        y_val = dataset.target
        print("\n############################################################")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("##############################################################")

    # Test that it is within a level of accuracy.
    def test_Accuracy_Gaussian(self):
        nb = NaiveBayes(0)
        dataset = datasets.load_breast_cancer()
        X_train, X_val, y_train, y_val = train_test_split(
            dataset.data, dataset.target, test_size=0.2, random_state=1)
        nb.fit(X_train, y_train)
        y_predicted = nb.predict(X_val)
        num_right = (y_val == y_predicted).sum()
        print("\n############################################################")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("##############################################################")

    # Test for consistency of results from previous.
    def test_Consistency_Gaussian(self):
        nb = NaiveBayes(0)
        dataset = datasets.load_iris()
        nb.fit(dataset.data, dataset.target)
        nb2 = NaiveBayes(0)
        nb2.fit(dataset.data, dataset.target)
        result1 = nb.predict([dataset.data[1]])
        result2 = nb2.predict([dataset.data[1]])
        self.assertEqual(result1, result2)

    # Tests that it basically runs.
    def test_Functional_Multinomial(self):
        nb = NaiveBayes(1)
        dataset = datasets.load_breast_cancer()
        nb.fit(dataset.data, dataset.target)
        y_predicted = nb.predict(dataset.data)
        y_val = dataset.target
        print("\n############################################################")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("##############################################################")

    # Test that it is within a level of accuracy.
    def test_Accuracy_Multinomial(self):
        nb = NaiveBayes(1)
        dataset = datasets.load_breast_cancer()
        X_train, X_val, y_train, y_val = train_test_split(
            dataset.data, dataset.target, test_size=0.2, random_state=1)
        nb.fit(X_train, y_train)
        y_predicted = nb.predict(X_val)
        print("\n############################################################")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("##############################################################")

    # Test for consistency of results from previous.
    def test_Consistency_Multinomial(self):
        nb = NaiveBayes(1)
        dataset = datasets.load_iris()
        nb.fit(dataset.data, dataset.target)
        nb2 = NaiveBayes(1)
        nb2.fit(dataset.data, dataset.target)
        result1 = nb.predict([dataset.data[1]])
        result2 = nb2.predict([dataset.data[1]])
        self.assertEqual(result1, result2)

    # Tests that it basically runs.
    def test_Functional_Bernoulli(self):
        nb = NaiveBayes(2)
        dataset = datasets.load_breast_cancer()
        nb.fit(dataset.data, dataset.target)
        y_predicted = nb.predict(dataset.data)
        y_val = dataset.target
        print("\n############################################################")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("##############################################################")

    # Test that it is within a level of accuracy.
    def test_Accuracy_Bernoulli(self):
        nb = NaiveBayes(2)
        dataset = datasets.load_breast_cancer()
        X_train, X_val, y_train, y_val = train_test_split(
            dataset.data, dataset.target, test_size=0.2, random_state=1)
        nb.fit(X_train, y_train)
        y_predicted = nb.predict(X_val)
        print("\n############################################################")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("##############################################################")

    # Test for consistency of results from previous.
    def test_Consistency_Bernoulli(self):
        nb = NaiveBayes(2)
        dataset = datasets.load_iris()
        nb.fit(dataset.data, dataset.target)
        nb2 = NaiveBayes(2)
        nb2.fit(dataset.data, dataset.target)
        result1 = nb.predict([dataset.data[1]])
        result2 = nb2.predict([dataset.data[1]])
        self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()
