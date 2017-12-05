from sklearn import naive_bayes
from sklearn import datasets
from sklearn import metrics

# import matplotlib.pyplot as plt

"""Naive Bayes Classifier"""
class NaiveBayes():

    """Make the Classifier based on needed Model"""
    @staticmethod
    def _make_NB_classifier(modeltype=0):
        if modeltype == 0:
            return naive_bayes.GaussianNB()
        elif modeltype == 1:
            return naive_bayes.MultinomialNB()
        elif modeltype == 2:
            return naive_bayes.BernoulliNB()
            

    """Build classifier for Naive Bayes"""
    def __init__(self, modeltype):
        self.model = NaiveBayes._make_NB_classifier(modeltype)
    
    """Trains the NB model on imported data"""
    def fit(self, data, features):
        X, y = data, features
        return self.model.fit(X, y)

    """Gets prediction for passed in data"""
    def predict(self, data_to_predict):
        return self.model.predict(data_to_predict)

    def test(self):
        dataset = datasets.load_iris()
        self.model.fit(dataset.data,dataset.target)
        expected = dataset.target
        predicted = self.model.predict(dataset.data)
        print(metrics.classification_report(expected,predicted))
        print(metrics.confusion_matrix(expected,predicted))

if __name__ == "__main__":
    nb = NaiveBayes(0)
    nb.test()
    nb = NaiveBayes(1)
    nb.test()
    nb = NaiveBayes(2)
    nb.test()