import lifelines as lf
import lifelines.datasets
import pickle


class CoxRegression:
    def __init__(self, **kwargs):
        alpha = .95
        penalizer = 0.0
        self.cph = None
        for k in kwargs:
            if k == 'alpha':
                alpha = kwargs[k]
        self.cph = lf.CoxPHFitter(
            alpha=alpha,
            tie_method='Efron',
            penalizer=penalizer,
            strata=None)

    def fit(self, dframe, duration_col, event_col=None, **kwargs):
        for k in kwargs:
            pass
        self.cph.fit(df=dframe,
                     duration_col=duration_col,
                     event_col=event_col,
                     show_progress=False,  # verbosity
                     initial_beta=None,
                     strata=None,
                     weights_col=None)  # zero vector

    def score(self):
        return self.cph.score_
