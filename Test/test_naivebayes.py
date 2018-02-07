import unittest
import import_impl
from naivebayes import *


class MyTest(unittest.TestCase):
    # To DO
    def setUp(self):
        pass

    # Run this one many times.
    def test1(self):
        nb = NaiveBayes()
        nb.fit(training[data], training[output])
        self.assertEqual(nb.predict(test), expected)

    # Test that it is within a level of accuracy.
    def test2(self):
        nb = NaiveBayes()
        nb.fit(training[data], training[output])
        y_pred = nb.predict(dataset)
        num_right = (dataset.target != y_pred).sum()
        assertTrue(num_right > ((size / 100) * 90))

    # Test for consistency of results from previous.
    def test3(self):
        nb = NaiveBayes()
        nb.fit(training[data], training[output])
        y_pred = nb.predict(dataset)
        nb2 = NaiveBayes()
        nb2.fit(training[data], training[output])
        y_pred2 = nb.predict(dataset)
        assertEqual(y_pred, y_pred2)

    # Test Predictable output for equal probabilities
    def test4(self):
        nb = NaiveBayes()
        nb.fit(training_equal[data], training_equal[output])
        y_pred = nb.predict(equal_data)
        nb2 = NaiveBayes()
        nb2.fit(training_equal[data], training_equal[output])
        y_pred2 = nb2.predict(equal_data)
        assertEqual(y_pred, y_pred2)


if __name__ == '__main__':
    unittest.main()
