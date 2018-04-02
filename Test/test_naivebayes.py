#!/usr/bin/env python3

import unittest
import import_impl
from naivebayes import *
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class MyTest(unittest.TestCase):

    # Tests that it basically runs.
    def test_Functional_Gaussian(self):
        nb = NaiveBayes(modeltype=NaiveBayes.GAUSSIAN)
        dataset = datasets.load_breast_cancer()
        nb.fit(dataset.data, dataset.target)
        y_predicted = nb.predict(dataset.data)
        y_val = dataset.target
        print("\n############################################################")
        print("Testing Gaussian Functionality:")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(y_val, y_predicted)) + "\n")

        if len(set(y_predicted)) == 2:
            print("Receiver Operating Characteristics:")
            fpr, tpr, _ = metrics.roc_curve(y_val, y_predicted)
            print(fpr)
            print(tpr)

            plt.figure()
            lw = 2
            plt.plot(fpr, tpr, color='orange', lw=lw, label='ROC curve')
            plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristics for Gaussian' +
                      ' Functionality')
            plt.legend(loc='lower right')
            plt.show()

        print("############################################################")

    # Test that it is within a level of accuracy.
    def test_Accuracy_Gaussian(self):
        nb = NaiveBayes(modeltype=NaiveBayes.GAUSSIAN)
        dataset = datasets.load_breast_cancer()
        X_train, X_val, y_train, y_val = train_test_split(
            dataset.data, dataset.target, test_size=0.2, random_state=1)
        nb.fit(X_train, y_train)
        y_predicted = nb.predict(X_val)
        num_right = (y_val == y_predicted).sum()
        print("\n############################################################")
        print("Testing Gaussian prediction accuracy:")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(y_val, y_predicted)) + "\n")

        if len(set(y_predicted)) == 2:
            print("Receiver Operating Characteristics:")
            fpr, tpr, _ = metrics.roc_curve(y_val, y_predicted)
            print(fpr)
            print(tpr)

            plt.figure()
            lw = 2
            plt.plot(fpr, tpr, color='orange', lw=lw, label='ROC curve')
            plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristics for Gaussian' +
                      ' Prediction Accuracy')
            plt.legend(loc='lower right')
            plt.show()

        print("############################################################")

    # Test for consistency of results from previous.
    def test_Consistency_Gaussian(self):
        nb = NaiveBayes(modeltype=NaiveBayes.GAUSSIAN)
        dataset = datasets.load_iris()
        nb.fit(dataset.data, dataset.target)
        nb2 = NaiveBayes(modeltype=NaiveBayes.GAUSSIAN)
        nb2.fit(dataset.data, dataset.target)
        result1 = nb.predict([dataset.data[1]])
        result2 = nb2.predict([dataset.data[1]])
        self.assertEqual(result1, result2)

    # Tests that it basically runs.
    def test_Functional_Multinomial(self):
        nb = NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL)
        dataset = datasets.load_breast_cancer()
        nb.fit(dataset.data, dataset.target)
        y_predicted = nb.predict(dataset.data)
        y_val = dataset.target
        print("\n############################################################")
        print("Testing Multinomial Functionality:")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(y_val, y_predicted)) + "\n")

        if len(set(y_predicted)) == 2:
            print("Receiver Operating Characteristics:")
            fpr, tpr, _ = metrics.roc_curve(y_val, y_predicted)
            print(fpr)
            print(tpr)

            plt.figure()
            lw = 2
            plt.plot(fpr, tpr, color='orange', lw=lw, label='ROC curve')
            plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristics for Multinomial' +
                      ' Functionality')
            plt.legend(loc='lower right')
            plt.show()

        print("############################################################")

    # Test that it is within a level of accuracy.
    def test_Accuracy_Multinomial(self):
        nb = NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL)
        dataset = datasets.load_breast_cancer()
        X_train, X_val, y_train, y_val = train_test_split(
            dataset.data, dataset.target, test_size=0.2, random_state=1)
        nb.fit(X_train, y_train)
        y_predicted = nb.predict(X_val)
        print("\n############################################################")
        print("Testing Multinomial prediction accuracy:")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(y_val, y_predicted)) + "\n")

        if len(set(y_predicted)) == 2:
            print("Receiver Operating Characteristics:")
            fpr, tpr, _ = metrics.roc_curve(y_val, y_predicted)
            print(fpr)
            print(tpr)

            plt.figure()
            lw = 2
            plt.plot(fpr, tpr, color='orange', lw=lw, label='ROC curve')
            plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristics for Multinomial' +
                      ' Prediction Accuracy')
            plt.legend(loc='lower right')
            plt.show()

        print("############################################################")

    # Test for consistency of results from previous.
    def test_Consistency_Multinomial(self):
        nb = NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL)
        dataset = datasets.load_iris()
        nb.fit(dataset.data, dataset.target)
        nb2 = NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL)
        nb2.fit(dataset.data, dataset.target)
        result1 = nb.predict([dataset.data[1]])
        result2 = nb2.predict([dataset.data[1]])
        self.assertEqual(result1, result2)

    # Tests that it basically runs.
    def test_Functional_Bernoulli(self):
        nb = NaiveBayes(modeltype=NaiveBayes.BERNOULLI)
        dataset = datasets.load_breast_cancer()
        nb.fit(dataset.data, dataset.target)
        y_predicted = nb.predict(dataset.data)
        y_val = dataset.target
        print("\n############################################################")
        print("Testing Bernoulli Functionality:")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(y_val, y_predicted)) + "\n")
        print(len(set(y_predicted)))

        if len(set(y_predicted)) == 2:
            print("Receiver Operating Characteristics:")
            fpr, tpr, _ = metrics.roc_curve(y_val, y_predicted)
            print(fpr)
            print(tpr)

            plt.figure()
            lw = 2
            plt.plot(fpr, tpr, color='orange', lw=lw, label='ROC curve')
            plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristics for Bernoulli' +
                      ' Functionality')
            plt.legend(loc='lower right')
            plt.show()

        print("############################################################")

    # Test that it is within a level of accuracy.
    def test_Accuracy_Bernoulli(self):
        nb = NaiveBayes(modeltype=NaiveBayes.BERNOULLI)
        dataset = datasets.load_breast_cancer()
        X_train, X_val, y_train, y_val = train_test_split(
            dataset.data, dataset.target, test_size=0.2, random_state=1)
        nb.fit(X_train, y_train)
        y_predicted = nb.predict(X_val)
        print("\n############################################################")
        print("Testing Bernoulli prediction accuracy:")
        print(metrics.classification_report(y_val, y_predicted))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val, y_predicted)))
        print("F-Score: " + str(metrics.f1_score(y_val, y_predicted)))
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(y_val, y_predicted)) + "\n")

        if len(set(y_predicted)) == 2:
            print("Receiver Operating Characteristics:")
            fpr, tpr, _ = metrics.roc_curve(y_val, y_predicted)
            print(fpr)
            print(tpr)

            plt.figure()
            lw = 2
            plt.plot(fpr, tpr, color='orange', lw=lw, label='ROC curve')
            plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristics for Bernoulli' +
                      ' Prediction Accuracy')
            plt.legend(loc='lower right')
            plt.show()

        print("############################################################")

    # Test for consistency of results from previous.
    def test_Consistency_Bernoulli(self):
        nb = NaiveBayes(modeltype=NaiveBayes.BERNOULLI)
        dataset = datasets.load_iris()
        nb.fit(dataset.data, dataset.target)
        nb2 = NaiveBayes(modeltype=NaiveBayes.BERNOULLI)
        nb2.fit(dataset.data, dataset.target)
        result1 = nb.predict([dataset.data[1]])
        result2 = nb2.predict([dataset.data[1]])
        self.assertEqual(result1, result2)


if __name__ == '__main__':
    plt.switch_backend('agg')
    unittest.main()
