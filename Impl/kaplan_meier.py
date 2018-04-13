from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import pandas as pd
import os
import csv


class KaplanMeier():
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
        self.lines = kplt
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

    def save_csv(self, filename, plots=None):
        if os.path.isfile(filename):
            os.remove(filename)
        ax = plt.gca()
        line = ax.lines[0]

        x_data = line.get_xdata()
        y_data = line.get_ydata()

        d = {'x': x_data, 'y': y_data}
        df = pd.DataFrame(data=d)
        df.to_csv(filename, index=False)
