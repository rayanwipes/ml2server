from sklearn.datasets import *
from sklearn.metrics import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

import pickle
from random import randint


class RandomForests:
    INITIALIZE, INITIALIZE_FROM_STRING, INITIALIZE_FROM_FILE = range(3)

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

    def fit(self, train_data, make_new_model=False):
        X, y = train_data
        if make_new_model:
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

    def gen_sample_problem(self):
        nfeat = randint(3, 100)
        # nfeat=100
        nred = randint(0, min(10, max(0, int((nfeat-2) / 2) - 1), 10))
        nrep = randint(0, min(max(0, nfeat - nred - 2), 10))
        # print(nfeat, nred, nrep)
        data = make_classification(
            n_samples=10000,
            n_features=nfeat,
            n_redundant=nred,
            n_repeated=nrep,
            n_classes=2,
            n_clusters_per_class=2,
            flip_y=0.00,  # default 0.01
            class_sep=1.0,
            hypercube=False,
            shift=0.0,
            scale=1.0,
            shuffle=True,
            random_state=0
        )
        return data

    def predict(self, X):
        return self.clf.predict(X)
