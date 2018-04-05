import csv
import pandas
from sklearn.datasets import *
from sklearn import metrics
from sklearn import preprocessing
from randomforest import *
from svm import *


lab_enc = preprocessing.LabelEncoder()


def load_csv(filename, columns=None):
    return pandas.read_csv(filepath_or_buffer=filename, usecols=columns)


def load_csv_xy(filename, ycolumns, xcolumns=None):
    f = open(filename, 'r')
    no_cols = len(next(csv.reader(f, delimiter=',')))
    f.close()
    if xcolumns is None:
        xcolumns = [i for i in range(no_cols) if i not in ycolumns]
    X = load_csv(filename, xcolumns).values
    y = load_csv(filename, ycolumns).values.ravel()
    y = lab_enc.fit_transform(y)
    return [X, y]
