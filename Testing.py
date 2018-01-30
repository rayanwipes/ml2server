import unittest
import NaiveBayes
class TestKFoldCrossValidation(unittest.TestCase):
    def initTests(self):
        self.assertEqual("1","1")

    def testKFold(self):
        # values = [(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2)]
        nb = NaiveBayes(0)
        n = len(values)
        average =[]
        for value in range(0,n):
            currList = a[:value] + a[value+1:]
            average.append((value,validate(train(currList),values[i])))
        totalAverage = float(sum(average)) / float(len(values))


if __name__ == '__main__':
    unittest.main()
