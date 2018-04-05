from sklearn.metrics import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.utils.multiclass import type_of_target
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

import pickle
from random import randint


class RandomForests:
    @staticmethod
    def _make_rfclassifier(**kwargs):
        no_estim = 100
        no_threads = 1
        verbosity = 0
        for key in kwargs:
            if key == 'n_estimators':
                no_estim = kwargs[key]
            elif key == 'verbose':
                verbosity = kwargs[key]
            elif key == 'threads':
                no_threads = kwargs[key]
        return RandomForestClassifier(
            n_estimators=no_estim,
            criterion="gini",
            max_features=None,
            oob_score=True,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=2,
            min_weight_fraction_leaf=.0,
            max_leaf_nodes=None,
            bootstrap=True,
            verbose=verbosity,
            warm_start=False,
            random_state=0,
            n_jobs=no_threads)

    @staticmethod
    def _make_rfregressor(**kwargs):
        no_estim = 100
        no_threads = 1
        verbosity = 0
        for key in kwargs:
            if key == 'n_estimators':
                no_estim = kwargs[key]
            elif key == 'verbose':
                verbosity = kwargs[key]
            elif key == 'threads':
                no_threads = kwargs[key]
        return RandomForestRegressor(
            n_estimators=no_estim,
            max_features=None,
            oob_score=True,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=2,
            min_weight_fraction_leaf=.0,
            max_leaf_nodes=None,
            bootstrap=True,
            verbose=verbosity,
            warm_start=False,
            random_state=0,
            n_jobs=no_threads)

    def __init__(self, **kwargs):
        self.clf = None
        for k in kwargs:
            v = kwargs[k]
            if k == 'filename':
                self.clf = joblib.load(v)
            elif k == 'binary':
                self.clf = pickle.loads(v)
        if self.clf is None:
            self.clf = RandomForests._make_rfclassifier()

    def dump_model(self):
        return pickle.dumps(self.clf)

    def save_model(self, filename):
        joblib.dump(self.clf, filename)

    def train_test_split(self, data, ratio=.4):
        X, y = data
        x1, x2, y1, y2 = train_test_split(
            X, y,
            test_size=ratio,
            random_state=0)
        return [[x1, y1], [x2, y2]]

    def fit(self, train_data):
        X, y = train_data
        if type_of_target(y) in ['continuous', 'continuous-multioutput']:
            self.clf = RandomForests._make_rfregressor(
                n_estimators=100,
                verbose=0,
                threads=-1)
        else:
            self.clf = RandomForests._make_rfclassifier(
                n_estimators=100,
                verbose=0,
                threads=-1)
        return self.clf.fit(X, y)

    def feature_importances(self):
        return self.clf.feature_importances_

    def score(self, test_data):
        X, y = test_data
        return self.clf.score(X, y)

    def predict(self, X):
        return self.clf.predict(X)
