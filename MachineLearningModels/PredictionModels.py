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
        self.theta = None
        self.predict_x = None
        self.y_predict = None

    def fit(self, x, y):

        self.y = y
        m = self.y.size
        self.x = np.stack([np.ones(m), x], axis=1)
        self.theta = np.linalg.inv(self.x.T.dot(self.x)).dot(self.x.T).dot(y)

    def predict(self, x):
        self.predict_x = x
        self.predict_x = np.stack([np.ones(self.predict_x.size), self.predict_x], axis=1)
        self.y_predict = self.predict_x.dot(self.theta)
        return self.y_predict

    def plot_line_of_best_fit(self, x, y):
        '''Function needs work'''
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(x, y)
        plt.show()

def test():
    pass

if __name__ == '__main__':
    test()
