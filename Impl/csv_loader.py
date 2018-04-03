import csv
import pandas
from sklearn.datasets import *


def load_csv(filename, columns=None):
    return pandas.read_csv(filepath_or_buffer=filename, usecols=columns)


def load_csv_xy(filename, ycolumn, xcolumns=None):
    f = open(filename, 'r')
    no_cols = len(next(csv.reader(f, delimiter=',')))
    f.close()
    if xcolumns is None:
        xcolumns = [i for i in range(no_cols) if i != ycolumn]
    X = load_csv(filename, xcolumns).T
    y = load_csv(filename, [ycolumn]).T
    return [X, y]


if __name__ == "__main__":
    print(load_csv_xy('file.csv', 0))
