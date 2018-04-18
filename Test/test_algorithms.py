#!/usr/bin/env python3


import import_impl
import unittest
from random import shuffle
from sklearn import datasets
from sklearn import metrics

from svm import *
from randomforest import *
from naivebayes import *
from problem_generator import *


class TestClass(unittest.TestCase):
    def test_standard_datasets(self):
        models = [
            (RandomForests(), 'random-forest'),
            (SupportVectorMachine(), 'suppor-vector-machine'),
            (NaiveBayes(modeltype=NaiveBayes.GAUSSIAN), 'nb-gaussian'),
            (NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL), 'nb-multinomial'),
            (NaiveBayes(modeltype=NaiveBayes.BERNOULLI), 'nb-bernoulli')
        ]
        data_sets = [
            (datasets.load_digits(return_X_y=True), 'digits'),
            (datasets.load_iris(return_X_y=True), 'iris'),
            (datasets.load_breast_cancer(return_X_y=True), 'breast cancer')
        ]
        for data, name in data_sets:
            print('Testing on', name, 'dataset')
            for m, mname in models:
                print('Fitting model', mname)
                train_data, test_data = m.train_test_split(data)
                m.fit(train_data)
                x_train, y_train = train_data
                x_test, y_test = test_data
                y_pred = m.predict(x_test)
                # print(metrics.classification_report(y_test,
                #                                     y_pred))
                print("\tAccuracy: " +
                      str(metrics.accuracy_score(y_test,
                                                 y_pred)))
                print("\tF-Score: " + str(metrics.f1_score(y_test, y_pred,
                                                           average='macro'))
                      + "\n")
                # print("Confusion Matrix:\n" +
                #       str(metrics.confusion_matrix(y_test, y_pred)) +
                #       "\n")
            print(self.sample_data(data))

    def test_random_classification(self):
        models = [
            (RandomForests(), 'random-forest'),
            (SupportVectorMachine(), 'suppor-vector-machine'),
            (NaiveBayes(modeltype=NaiveBayes.GAUSSIAN), 'nb-gaussian'),
            # not supported as it requires non-negative values in the data
            # (NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL), 'nb-multinomial'),
            (NaiveBayes(modeltype=NaiveBayes.BERNOULLI), 'nb-bernoulli')
        ]
        problem = gen_sample_problem(PROBLEM_CLASSIFICATION)
        print("Testing on randomly generated classification problem")
        for m, mname in models:
            print('Fitting model', mname)
            train_data, test_data = m.train_test_split(problem)
            m.fit(train_data)
            x_train, y_train = train_data
            x_test, y_test = test_data
            y_pred = m.predict(x_test)
            # print(metrics.classification_report(y_test,
            #                                     y_pred))
            print("\tAccuracy: " +
                  str(metrics.accuracy_score(y_test,
                                             y_pred)))
            print("\tF-Score: " + str(metrics.f1_score(y_test, y_pred,
                                                       average='macro'))
                  + "\n")
            # print("Confusion Matrix:\n" +
            #       str(metrics.confusion_matrix(y_test, y_pred)) +
            #       "\n")

    def test_random_regression(self):
        models = [
            (RandomForests(), 'random-forest'),
            (SupportVectorMachine(), 'suppor-vector-machine')
        ]
        problem = gen_sample_problem(PROBLEM_REGRESSION)
        print("Testing on randomly generated regression problem")
        for m, mname in models:
            print('Fitting model', mname)
            train_data, test_data = m.train_test_split(problem)
            m.fit(train_data)
            print("\tScore:", m.score(test_data))
            # print(metrics.classification_report(y_test,
            #                                     y_pred))
            # print("\tAccuracy: " +
            #       str(metrics.accuracy_score(y_test,
            #                                  y_pred)))
            # print("\tF-Score: " + str(metrics.f1_score(y_test,
            #                                          y_pred,
            #                                          average='macro'))
            #                                          + "\n")
            # print("Confusion Matrix:\n" +
            #       str(metrics.confusion_matrix(y_test, y_pred)) +
            #       "\n")

    def get_provisional_score(self, model, sdata, tdata):
        model.fit(sdata)
        return model.score(tdata)

    def sample_data(self, data, no_rows=None):
        X, y = data
        no_sr = int(min(len(X) * .4, 100) if no_rows is None else no_rows)
        no_tr = int(min(1.5 * no_sr, len(X) - no_sr))
        print('variables', no_sr, no_tr)
        shrows = list(range(len(y)))
        shuffle(shrows)
        sample_rows = shrows[:no_sr]
        test_rows = shrows[no_sr:no_sr+no_tr]

        X_s = [X[i] for i in sample_rows]
        y_s = [y[i] for i in sample_rows]
        X_t = [X[i] for i in test_rows]
        y_t = [y[i] for i in test_rows]

        # now training on the algorithms

        nb_g = NaiveBayes(modeltype=NaiveBayes.GAUSSIAN)
        nb_m = NaiveBayes(modeltype=NaiveBayes.MULTINOMIAL)
        nb_b = NaiveBayes(modeltype=NaiveBayes.BERNOULLI)
        svm = SupportVectorMachine()
        rf = RandomForests()

    return [self.get_provisional_score(m, [X_s, y_s], [X_t, y_t])
            for m in [nb_g, nb_m, nb_b, svm, rf]]


if __name__ == "__main__":
    unittest.main()
