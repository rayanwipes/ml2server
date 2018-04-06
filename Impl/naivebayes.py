from sklearn import naive_bayes
from sklearn import datasets
from sklearn import metrics
from sklearn.externals import joblib


# Naive Bayes Classifier
class NaiveBayes():
    GAUSSIAN, MULTINOMIAL, BERNOULLI = range(3)

    # Make the Classifier based on needed Model
    @staticmethod
    def _make_NB_classifier(modeltype):
        if modeltype == NaiveBayes.GAUSSIAN:
            return naive_bayes.GaussianNB()
        elif modeltype == NaiveBayes.MULTINOMIAL:
            return naive_bayes.MultinomialNB()
        elif modeltype == NaiveBayes.BERNOULLI:
            return naive_bayes.BernoulliNB()

    # Build classifier for Naive Bayes
    def __init__(self, **kwargs):
        modeltype = NaiveBayes.GAUSSIAN
        self.model = None
        for k in kwargs:
            v = kwargs[k]
            if k == 'filename':
                self.model = joblib.load(v)
            elif k == 'modeltype':
                modeltype = v
        if self.model is None:
            self.model = NaiveBayes._make_NB_classifier(modeltype)

    # Serialize model into byte string
    def dump_model(self):
        return pickle.dumps(self.clf)

    # Save Model To file
    def save_model(self, filename):
        joblib.dump(self.model, filename)

    # Split train and test data by ratio
    def train_test_split(self, data, ratio=.4):
        X, y = data
        x1, x2, y1, y2 = train_test_split(
            X, y,
            test_size=ratio,
            random_state=0)
        return [[x1, y1], [x2, y2]]

    # Trains the NB model on imported data
    def fit(self, train_data):
        X, y = train_data
        return self.model.fit(X, y)

    # Trains the NB model incrementally on imported data
    def partial_fit(self, train_data):
        X, y = train_data
        return self.model.partial_fit(X, y)

    # Get feature importances
    def feature_importances(self):
        return self.clf.feature_importances_

    # Obtain score for the test data
    def score(self, test_data):
        X, y = test_data
        return self.clf.score(X, y)

    # Gets prediction for passed in data
    def predict(self, data_to_predict):
        return self.model.predict(data_to_predict)

    # Debug Function
    def test(self):
        dataset = datasets.load_iris()
        self.model.fit(dataset.data, dataset.target)
        expected = dataset.target
        predicted = self.model.predict(dataset.data)
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))
