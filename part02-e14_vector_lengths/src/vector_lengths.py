#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(np.square(a), axis=1))

def main():
    print(vector_lengths(np.array([[1, 2], [3, 4]])))

if __name__ == "__main__":
    main()
