#!/usr/bin/env python3

import unittest
import lifelines as lf
from lifelines import datasets

import import_impl

from cox_regression import *


class CoxRegressionTest(unittest.TestCase):
    def test_score_validity_rossi(self):
        dframe = lf.datasets.load_rossi()
        cox = CoxRegression()
        cox.fit(dframe, 'week', 'arrest')
        s_arrest = cox.score()
        cox.fit(dframe, 'week', 'fin')
        s_fin = cox.score()
        self.assertGreater(s_fin, s_arrest)


if __name__ == '__main__':
    unittest.main()
