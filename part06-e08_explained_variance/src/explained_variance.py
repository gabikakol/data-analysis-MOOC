#!/usr/bin/env python3

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

def explained_variance():
    data = pd.read_csv('src/data.tsv', sep='\t')
    x = data.var(axis=0)
    y = PCA()
    y.fit(data)
    return x, y.explained_variance_

def main():
    x, y = explained_variance()
    print(sum(x), sum(y))
    list_x = " ".join([f"{i:.3f}" for i in x])
    list_y = " ".join([f"{i:.3f}" for i in y])
    print(f"The variances are: {list_x}")
    print(f"The explained variances after PCA are: {list_y}")
    plt.plot(np.arange(1, 11), np.cumsum(y))
    plt.show()

if __name__ == "__main__":
    main()