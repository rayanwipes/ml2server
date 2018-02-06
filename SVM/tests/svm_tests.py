from sklearn import svm
import unittest


class SVMUnitTests(unittest.TestCase):

    #Tests testing is working.
    def initTests(self):
        self.assertEqual("1", "1")

    #Tests fitting data method doesn't return null value
    def testFittingData(self):
        trainingSamples = [[0, 0], [1, 1]]
        classLabels = [0, 1]
        clf = svm.SVC()
        fittedData = clf.fit(trainingSamples, classLabels)
        self.assertTrue(fittedData != None)

    #Tests predicting data doesn't return null.
    def testPredictingData(self):
        trainingSamples = [[0, 0], [1, 1]]
        classLabels = [0, 1]
        clf = svm.SVC()
        fittedData = clf.fit(trainingSamples, classLabels)
        prediction = clf.predict([[2., 2.]])
        self.assertTrue(prediction != None)


if __name__ == "__main__":
    unittest.main()
