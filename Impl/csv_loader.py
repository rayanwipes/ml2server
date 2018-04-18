import csv
import pandas
from sklearn.datasets import *
from sklearn import metrics
from sklearn import preprocessing


lab_enc = preprocessing.LabelEncoder()


def load_csv(filename, columns=None):
    return pandas.read_csv(filepath_or_buffer=filename, usecols=columns).values


def load_headers(filename, columns=None):
    cols = []
    f = open(filename, 'r')
    cols = next(csv.reader(f, delimiter=','))
    f.close()
    if columns is None:
        return cols
    return [cols[i] for i in columns]



def load_csv_xy(filename, ycolumns, xcolumns=None):
    f = open(filename, 'r')
    no_cols = len(load_headers(filename))
    f.close()
    if xcolumns is None:
        xcolumns = [i for i in range(no_cols) if i not in ycolumns]
    X = load_csv(filename, xcolumns)
    y = load_csv(filename, ycolumns).ravel()
    y = lab_enc.fit_transform(y)
    return [X, y]


def unload_csv(filename, headers, table):
    with open(filename, 'w') as f:
        w = csv.writer(f, dialect='excel', delimiter=',')
        w.writerow(headers)
        w.writerows(table)
