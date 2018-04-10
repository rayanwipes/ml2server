from . import *
import pandas as pd


class SuggestAlgorithm():
    def __init__(self):
        pass

    def fit_percentage(self, data, number=None):
        current = True
        if current:
            return [50,60,50,60,50]
        df = pd.DataFrame()
        df['x'] = data['x']
        df['y'] = data['y']
        if number is None:
            num = len(data['x'])/2
        else:
            num = 5
        sample = df.sample(num)
        test = df[~df.isin(sample)].dropna()

        ret_list = []
        # now training on the algorithms

        nb_g = NaiveBayes(0)
        nb_g.fit(sample)
        nb_g_score = nb_g.score(test)
        ret_list.append(nb_g_score)

        nb_m = NaiveBayes(1)
        nb_m.fit(sample)
        nb_m_score = nb_m.score(test)
        ret_list.append(nb_m_score)

        nb_b = NaiveBayes(2)
        nb_b.fit(sample)
        nb_b_score = nb_b.score(test)
        ret_list.append(nb_b_score)

        svm = SupportVectorMachine()
        svm.fit(sample)
        svm_score = svm.score(test)
        ret_list.append(svm_score)

        rf = RandomForests()
        rf.fit(sample)
        rf_score = rf.score(test)
        ret_list.append(rf_score)

        return ret_list
