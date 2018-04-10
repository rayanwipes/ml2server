#!/usr/bin/env python3


from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split
import unittest
import import_impl


from svm import *
from csv_loader import *
from randomforest import *


class CsvLoaderTest(unittest.TestCase):
    def test_int_in_target(self):
        data = load_csv_xy('Test/dataset/ints.csv', [0])
        print(data)
        X, y = data
        for e in [(X[0][i], type(X[0][i])) for i in range(len(X[0]))]:
            print(e)

    def test_dataset_format(self):
        data = load_csv_xy('Test/dataset/file.csv', [15])
        test_svm = SupportVectorMachine()
        test_svm.fit(data)
        rf = RandomForests()
        rf.fit(data)

    def test_csv_data_confusion(self):
        data = load_csv_xy('Test/dataset/file.csv', [15])
        print(data)
        X, y = data
        for e in [(X[0][i], type(X[0][i])) for i in range(len(X[0]))]:
            print(e)
        clf = SupportVectorMachine()
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=.4)
        clf.fit([X_train, y_train])
        predicted_values = clf.predict(X_val)

        print(metrics.classification_report(y_val, predicted_values))
        print("\nAccuracy: " + str(metrics.accuracy_score(y_val,
                                                          predicted_values)))
        print("F-Score: " + str(metrics.f1_score(y_val, predicted_values,
                                                 average='macro')) + "\n")
        print("Confusion Matrix:\n" +
              str(metrics.confusion_matrix(y_val, predicted_values)) + "\n")


if __name__ == '__main__':
    unittest.main()
