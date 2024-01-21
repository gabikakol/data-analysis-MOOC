#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    #return the array whose rows are sorted based on column c, in the following way. Rows are ordered so that those rows with the most frequent element in column c come first, then come the rows with the second most frequent element in column c, and so on. Therefore, the values outside column c don't affect the ordering in any way.
    #use np.unique
    # among those rows that contain in column c a number that appear twice in column c the order can be arbitrary.
    x = np.array(a)
    y = x[:,c]
    z = np.unique(y, return_counts=True)
    w = np.argsort(z[1])[::-1]
    return x[np.argsort(np.searchsorted(z[0][w], y))]
    """
    x = np.unique(a, axis=0, return_counts=True)
    return x[0][np.argsort(x[1])]
    """

def main():
    a = [[5,0,3,3,7,9,3,5,2,4],[7,6,8,8,1,6,7,7,8,1],[5,9,8,9,4,3,0,3,5,0],[3,3,1,0,0,1,9,7,6,8]]
    print(most_frequent_first(a, -1))

if __name__ == "__main__":
    main()

