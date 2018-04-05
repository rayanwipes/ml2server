#!/usr/bin/env python3


import sys

from classifier import *
from cox_regression import *
from kaplan_meier import *
from csv_loader import *


NBG, NBM, NBB, SVM, RF, KX, COX, KMF = [
    'nb-gaussian',
    'nb-multinomial',
    'nb-bernoulli',
    'svm',
    'rf',
    'k-cross',
    'cox',
    'kmf'
]


def is_classifier(alg):
    return alg in [NBG, NBM, NBB, SVM, RF]


def get_classifier_type(alg):
    if alg in [NBG, NBM, NBB]:
        return NaiveBayes
    elif alg in [SVM]:
        return SupportVectorMachine
    elif alg in [RF]:
        return RandomForests
    else:
        raise Exception('cannot find classifier type for ' + str(alg))


def is_kcross(alg):
    return alg == KX


def is_cox(alg):
    return alg == COX


def is_kmf(alg):
    return alg == MKF


# https://stackoverflow.com/questions/1158076/implement-touch-using-python
def touch(fname, mode=0o666, dir_fd=None, **kwargs):
    flags = os.O_CREAT | os.O_APPEND
    with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
        os.utime(f.fileno() if os.utime in os.supports_fd else fname,
            dir_fd=None if os.supports_fd else dir_fd, **kwargs)


if __name__ == "__main__":
    print('ARGS: ', sys.argv)
    successfile, alg, datafile, output = sys.argv[1:5]
    args = sys.argv[5:]
    print(successfile, alg, datafile, output)
    if is_classifier(alg):
        c = None
        clftype = get_classifier_type(alg)
        if clftype == NaiveBayes:
            mtype = None
            if alg == NBG:
                mtype = NaiveBayes.GAUSSIAN
            elif alg == NBM:
                mtype = NaiveBayes.MULTINOMIAL
            elif alg == NBB:
                mtype = NaiveBayes.BERNOULLI
            else:
                raise Exception('unknown nbtype of ' + str(mtype))
            c = Classifier(classifier=clftype, modeltype=mtype)
        else:
            c = Classifier(classifier=clftype)
        ycolumn = int(args[0])
        args = args[1:]
        data = load_csv_xy(datafile, [ycolumn], [int(x) for x in args] if len(args) else None)
        c.fit(data)
        c.save_model(output)
    elif is_kcross(alg):
        pass
    elif is_cox(alg):
        cox = CoxRegression()
        report_output, dur_col, event_col = args[:3]
        args = args[3:]
        ycolumn = int(args[0])
        args = args[1:]
        data = load_csv_xy(datafile, ycolumn, [int(x) for x in args] if len(args) else None)
        cox.fit(data, dur_col, event_col)
        pass  # dump output into output and report output
    elif is_kmf(alg):
        report_output = args[0]
        args = args[1:]
        kmf = KaplanMeierFitter()
        args = args[1:]
        ycolumn = int(args[0])
        data = load_csv_xy(datafile, ycolumn, [int(x) for x in args] if len(args) else None)
        kmf.fit(data)
        pass  # dump plot/table into output and report output
    touch(successfile)
