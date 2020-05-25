import numpy as np


class LinearRegressionLeastSquares:
    def __init__(self, array):
        self.data = array
        self.xData = np.ravel(self.data[:, :1])
        self.yData = np.ravel(self.data[:, 1:])
        self.xMean = np.mean(self.xData)
        self.yMean = np.mean(self.yData)
        self.xSTD = np.round(np.std(self.xData, ddof=1), 3)
        self.ySTD = np.round(np.std(self.yData, ddof=1), 3)
        self.rValue = self.getRValue()
        self.slope = self.getSlope()
        self.intercept = self.getIntercept()

    def getRValue(self):
        normalization = (1/(len(self.xData) - 1))
        xySum = 0
        for i in range(0, 4):
            xDeviation = (self.xData[i] - self.xMean)/self.xSTD
            yDeviation = (self.yData[i] - self.yMean)/self.ySTD
            xySum += xDeviation * yDeviation
        rValue = np.round(normalization * xySum, 3)
        return rValue

    def getSlope(self):
        slope = np.round(self.rValue * self.ySTD / self.xSTD, 2)
        return slope

    def getIntercept(self):
        intercept = np.round(self.yMean - (self.slope * self.xMean), 2)
        return intercept