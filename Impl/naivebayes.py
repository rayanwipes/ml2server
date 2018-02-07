from sklearn import naive_bayes
from sklearn import datasets
from sklearn import metrics
from sklearn.externals import joblib


# Naive Bayes Classifier
class NaiveBayes():
    # Make the Classifier based on needed Model
    @staticmethod
    def _make_NB_classifier(modeltype):
        if modeltype == 0:
            return naive_bayes.GaussianNB()
        elif modeltype == 1:
            return naive_bayes.MultinomialNB()
        elif modeltype == 2:
            return naive_bayes.BernoulliNB()

    # Build classifier for Naive Bayes
    def __init__(self, modeltype=0, model=None):
        if model is None:
            self.model = NaiveBayes._make_NB_classifier(modeltype)
        else:
            self.model = NaiveBayes.loadModel()

    # Save Model To file
    def saveModel(self):
        joblib.dump(self.model, 'nb.pkl')

    # Load Model from file
    def loadModel(self):
        self.model = joblib.load('nb.pkl')
        return self

    # Trains the NB model on imported data
    def fit(self, data, features):
        X, y = data, features
        return self.model.fit(X, y)

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


