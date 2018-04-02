from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import os


class kaplan_meier():
    def __init__(self):
        plt.switch_backend('agg')
        self.kmf = KaplanMeierFitter()
        self.event_col = None
        self.dur_col = None
        self.subplots = []
        self.plots = []

    def add_subplot(self, id=111):
        self.subplots += [plt.subplot(id)]
        self.plots = []

    def fit(self, duration_array, death_observed):
        self.kmf.fit(duration_array, event_observed=death_observed)
        # plot = plt if len(self.subplots) == 0 else self.subplots[-1]
        # self.kmf.survival_function_.plot()
        if len(self.subplots) == 0:
            kplt = self.kmf.plot()
        else:
            kplt = self.kmf.plot(ax=self.subplots[-1])
        self.event_col = 'Event'
        self.dur_col = 'Duration'
        # print("Ran the Kaplan Meier Fitter")
        plt.title('Kaplan Meier - Event Observed')
        plt.xlabel(self.dur_col)
        plt.ylabel(self.event_col)
        self.plots += [kplt]

    def save_fig(self, filename, plots=None):
        if os.path.isfile(filename):
            os.remove(filename)
        plt.savefig(filename)
        plt.clf()
        plt.cla()
        self.subplots = []
        self.plots = []
