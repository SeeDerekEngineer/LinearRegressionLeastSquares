import LinearRegressionLeastSquares as lrls
import numpy as np


if __name__ == "__main__":
    yourData = np.array([[1, 1], [2, 2], [1, 3], [4, 6]])
    lrlsRunner = lrls.LinearRegressionLeastSquares(yourData)
    print (lrlsRunner.getSlope(), lrlsRunner.getIntercept())