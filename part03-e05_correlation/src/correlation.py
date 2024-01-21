#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    sepal_length = data[:, 0]
    petal_length = data[:, 2]
    correlation, _ = scipy.stats.pearsonr(sepal_length, petal_length)
    return correlation

def correlations():
    data = load()
    correlations_matrix = np.corrcoef(data, rowvar=False)
    return correlations_matrix

def main():
    print("Pearson correlation between sepal length and petal length:", lengths())
    print("Correlations between all variables:\n", correlations())

if __name__ == "__main__":
    main()
