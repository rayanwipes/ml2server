from sklearn.datasets import *
from random import randint


PROBLEM_CLASSIFICATION, PROBLEM_REGRESSION = range(2)


def gen_sample_problem(problem_type=PROBLEM_CLASSIFICATION):
    nfeat = randint(3, 100)
    # nfeat=100
    nred = randint(0, min(10, max(0, int((nfeat-2) / 2) - 1), 10))
    nrep = randint(0, min(max(0, nfeat - nred - 2), 10))
    # print(nfeat, nred, nrep)
    if problem_type == PROBLEM_CLASSIFICATION:
        data = make_classification(
            n_samples=10000,
            n_features=nfeat,
            n_redundant=nred,
            n_repeated=nrep,
            n_classes=2,
            n_clusters_per_class=2,
            flip_y=0.00,  # default 0.01
            class_sep=1.0,
            hypercube=False,
            shift=0.0,
            scale=1.0,
            shuffle=True,
            random_state=0)
    elif problem_type == PROBLEM_REGRESSION:
        data = make_regression(
            n_samples=10000,
            n_features=nfeat,
            n_targets=1,
            noise=0.,
            coef=False,
            random_state=0)
    else:
        raise Exception('unknown problem type requested to generate: ' +
                        str(problem_type))
    return data
