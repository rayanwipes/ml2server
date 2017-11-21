import pickle
import sklearn.ensemble
import sklearn.datasets


from random import randint
from sklearn.externals import joblib


class RandomForests:
    INITIALIZE, INITIALIZE_FROM_STRING, INITIALIZE_FROM_FILE = range(3)

    @staticmethod
    def _make_rfclassifier():
        return sklearn.ensemble.RandomForestClassifier(
            max_features='auto',
            oob_score=True
        )

    @staticmethod
    def _load_model_from_file(filename):
        return joblib.load(filename)

    @staticmethod
    def _load_model(model):
        return pickle.loads(model)

    @staticmethod
    def initialize():
        return RandomForests(RandomForests.INITIALIZE)

    @staticmethod
    def initialize_from_model(model):
        return RandomForests(RandomForests.INITIALIZE_FROM_STRING, model)

    @staticmethod
    def initialize_from_file(filename):
        return RandomForests(RandomForests.INITIALIZE_FROM_FILE, filename)

    def __init__(self, modeltype=0, model=None):
        if modeltype == RandomForests.INITIALIZE:
            self.rf = RandomForests._make_rfclassifier()
        elif modeltype == RandomForests.INITIALIZE_FROM_STRING:
            self.rf = RandomForests._load_model(model)
        elif modeltype == RandomForests.INITIALIZE_FROM_FILE:
            self.rf = RandomForests._load_model_from_file(model)
        else:
            raise Exception("invalid model initializer flag")

    def dump_model(self):
        return pickle.dumps(self.rf)

    def dump_model_into_file(self, filename):
        joblib.dump(self.rf, filename)

    def fit(self, data):
        X, y = data
        return self.rf.fit(X, y)

    def gen_sample_problem(self):
        nfeat = randint(0, 100)
        data = sklearn.datasets._make_classification(
            n_samples=1000,
            n_features=nfeat,
            n_redundant=randint(0, nfeat/2),
            n_repeated=randint(0, nfeat/2),
            n_classes=2,
            flip_y=0.01,
            class_sep=1.0,
            hypercube=True,
            shift=0.0,
            scale=1.0,
            shuffle=True,
            random_state=0
        )
        return data

    def predict(self, X):
        self.rf.predict(X)
