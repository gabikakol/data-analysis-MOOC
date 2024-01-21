#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    a = np.sum(X*Y, axis=1)
    len_x = scipy.linalg.norm(X, 2, axis=1)
    len_y = scipy.linalg.norm(Y, 2, axis=1)
    b = a/(len_x*len_y)
    b = np.clip(b, -1, 1)
    ans = np.arccos(b)/np.pi*180
    return ans

def main():
    X = np.array([[1, 2, 3], [4, 5, 6]])
    Y = np.array([[2, 1, 3], [7, 3, 6]])
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
