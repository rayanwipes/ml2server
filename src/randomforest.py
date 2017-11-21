import sklearn.ensemble
import sklearn.datasets

class RandomForests:
    @staticmethod
    def make_rfclassifier():
        return sklearn.ensemble.RandomForestClassifier(
            max_features='auto',
            oob_score=True
        )

    def __init__(self):
        self.rf = make_rfclassifier()

    def fit(self, data):
        X, y = data
        return self.rf.fit(X, y)

    def get_sample_problem(self):
        data = sklearn.datasets.make_classification(
            n_samples=1000,
            n_features=no_features,
            n_redundant=randint(0, no_features/2),
            n_repeated=randint(0, no_features/2),
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
