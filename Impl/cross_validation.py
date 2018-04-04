from sklearn import cross_val_score

class CrossValidation:
    def __init__(self, model=None):
        self.model = model

    def set(self, model):
        self.model = model

    def score(self, data, cv=None):
        X, y = data
        return cross_val_score(self.model, X, y, cv=cv)
