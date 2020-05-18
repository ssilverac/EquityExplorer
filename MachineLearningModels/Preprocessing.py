import numpy as np

def feature_normalization(X):
    X = (X-np.mean(X)) / np.std(X)

    return X
