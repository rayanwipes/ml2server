import pandas
from sklearn.datasets import *


def load_csv(filename, columns=None):
    return pandas.read_csv(filepath_or_buffer=filename, usecols=columns)


def load_csv_xy(filename, ycolumn, xcolumns=None):
    return [
        load_csv(xcolumns),  # X
        load_csv(ycolumn)  # y
    ]
