"""
Predictive Models made from scratch
"""
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:

    def __init__(self):
        self.x = None
        self.y = None
        self.m = None
        self.alpha = None
        self.n_iters = None
        self.theta = None

    def __add_intercept(self):

        self.m = self.x.shape[0] #number of training samples
        ones = np.ones((self.m, 1))
        self.x = np.hstack((ones, self.x))
        self.theta = np.zeros((self.x.shape[1], 1)) # create a 1D array of zeros of same length as X rows
        self.y = self.y[:, np.newaxis]

    def __gradient_descent(self):
        '''
        theta = theta - (1/m) * [(XTranspose dot ((X dot theta) - y))]
        '''
        self.__add_intercept()

        for i in range (self.n_iters):
            temp = self.x.dot(self.theta) - self.y
            temp2 = self.x.T.dot(temp)
            self.theta = self.theta - ((self.alpha/self.m) * temp2)
        print(self.theta)

    def fit(self, x, y, alpha=0.01, n_iters=500):
        self.x = x
        self.y= y
        self.alpha = alpha
        self.n_iters = n_iters
        self.__gradient_descent()

    def predict(self, x):
        pass

def test():
    pass

if __name__ == '__main__':
    test()
