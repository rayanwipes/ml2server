import unittest
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import metrics

class MyTest(unittest.TestCase):
    # Loads up the Iris datset
    # Test taking 30 percent of the iris data set in the test, and the rest in training using a SVM
    # Since SVMs are being used for the data, the c value was always set at 1 to keep it consistant
    def setUp(self):
        self.iris = datasets.load_iris()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.iris.data, self.iris.target, test_size=0.3, random_state=0)

    # Just test the initial scoring fitting the data
    def test0(self):
        clf = svm.SVC(C=1).fit(self.X_train, self.y_train)
        score = clf.score(self.X_test, self.y_test)
        print("Plain scoring it without any k fold cross validation reveals an accuracy on the data of")
        print(score)

    # Testing using k fold cross validation where k was set to 8
    # It then takes the average accuracy of the array of scores, and gives an uncertainty in the result
    def test1(self):
        # sets the C value for the SVM for 1 to be consistent with the tests
        clf = svm.SVC( C=1)
        # Actually perform a cross value score with the iris dataset and the iris target set
        scores = cross_val_score(clf, self.iris.data, self.iris.target, cv=8)
        print("Average with Standard Deviation with no specfic scoring macro %0.3f (+/- %0.3f)" % (scores.mean(), scores.std() * 2))
        print(scores)


    # Do the same thing with the cross val score except this time you can add a metric to score it on. in this case it is macro averaged
    def test2(self):
        clf = svm.SVC( C=1)
        scores = cross_val_score(clf, self.iris.data, self.iris.target, cv=8, scoring='f1_macro')
        print("Average with Standard Deviation scoring it with macro averaging %0.3f (+/- %0.3f)" % (scores.mean(), scores.std() * 2))
        print(scores)

    # This test checks what happend when the number of times that cross validation occurs i.e. k increasing
    def test_big(self):
        for i in range(2,10):
            clf = svm.SVC( C=1)
            scores = cross_val_score(clf, self.iris.data, self.iris.target, cv=i, scoring='f1_macro')
            print("K is %i Average with Standard Deviation scoring it with macro averaging %0.3f (+/- %0.3f)" % (i,scores.mean(), scores.std() * 2))
            print(scores)


if __name__ == "__main__":
    unittest.main()
