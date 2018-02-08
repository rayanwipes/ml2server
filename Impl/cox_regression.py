import lifelines as lf
import lifelines.datasets
import pickle


class CoxRegression:
    def __init__(self, **kwargs):
        alpha = .66
        self.cph = None
        for k in kwargs:
            if k == 'filename':
                self.cph = pickle.load(kwargs[k])
                return
            elif k == 'string':
                self.cph = pickle.loads(kwargs[k])
                return
            elif k == 'alpha':
                alpha = kwargs[k]
        self.cph = lf.CoxPHFitter(alpha)

    def dump(self):
        return pickle.dumps(self.cph)

    def dump_into_file(self, filename):
        pickle.dump(self.cph, filename)

    def fit(self, dframe, **kwargs):
        self.cph.fit(dframe, **kwargs)

    def score(self):
        return self.cph.score_


if __name__ == "__main__":
        dframe = lf.datasets.load_rossi()
        # print(dframe)
        cox = CoxRegression(alpha=.8)
        cox.fit(dframe, duration_col='week', event_col='arrest')
        cox.cph.print_summary()
