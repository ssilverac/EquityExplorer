"""
Predictive Models made from scratch
"""
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:

    def __init__(self):

        self.xs = None
        self.ys = None
        self.slope = None
        self.y_intercept = None



    def __calc_slope_and_intercept(self):
        slope = (((mean(self.xs) * mean(self.ys)) - mean(self.xs*self.ys)) / ((mean(self.xs) ** 2) - mean(self.xs**2)))

        y_intercept = mean(self.ys) - slope*mean(self.xs)

        self.slope = slope
        self.y_intercept = y_intercept

    def fit_model(self, xs, ys):
        self.xs = xs
        self.ys = ys

        self.__calc_slope_and_intercept()

    def predict(self, x):

        predict_y = [(self.slope * x) + self.y_intercept]
        return predict_y

    def plot_line_of_best_fit(self):

        regression_line = [(self.slope * x) + self.y_intercept for x in self.xs]
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(self.xs, self.ys)
        ax.plot(self.xs, regression_line, 'r')
        plt.show()



def test():
    pass

if __name__ == '__main__':
    test()
