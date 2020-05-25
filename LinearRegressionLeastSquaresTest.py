import unittest
import LinearRegressionLeastSquares as lrls
import numpy as np


class LinearRegressionLeastSquaresTest(unittest.TestCase):

    def setUp(self):
        testArray = np.array([[1, 1], [2, 2], [2, 3], [3, 6]])
        self.testObject = lrls.LinearRegressionLeastSquares(testArray)

    def testCreationOfLRLS_returnsAsExpected(self):
        testData = np.array([[1, 1], [2, 2], [2, 3], [3, 6]])
        self.assertEquals(testData.tolist(), self.testObject.data.tolist())

    def testGetXandYValues_returnsAsExpected(self):
        testData = np.array([1, 2, 2, 3])
        self.assertEquals(testData.tolist(), self.testObject.xData.tolist())
        testData = np.array([1, 2, 3, 6])
        self.assertEquals(testData.tolist(), self.testObject.yData.tolist())

    def testGetMeans_returnsAsExpected(self):
        testXMean = 2
        self.assertEquals(testXMean, self.testObject.xMean)
        testYMean = 3
        self.assertEquals(testYMean, self.testObject.yMean)

    def testGetStandardDeviations_returnsAsExpected(self):
        testXSTD = 0.816
        self.assertEquals(testXSTD, self.testObject.xSTD)
        testYSTD = 2.160
        self.assertEquals(testYSTD, self.testObject.ySTD)

    def testGetR_returnsAsExpected(self):
        testRValue = 0.946
        self.assertEquals(testRValue, self.testObject.rValue)

    def testGetSlope_returnsAsExpected(self):
        testSlope = 2.50
        self.assertEquals(testSlope, self.testObject.slope)

    def testGetIntercept_returnsAsExpected(self):
        testIntercept = -2.00
        self.assertEquals(testIntercept, self.testObject.intercept)

if __name__ == '__main__':
    unittest.main()