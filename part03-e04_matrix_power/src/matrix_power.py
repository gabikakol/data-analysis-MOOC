#!/usr/bin/env python3

import numpy as np
import functools

def matrix_power(a, n):
    np.eye(2)

    if n == 0:
        return np.eye(a.shape[0])
    elif n > 0:
        return np.linalg.matrix_power(a, n)
    else:
        return np.linalg.inv(np.linalg.matrix_power(a, -n))

def main():
    x = np.array([[1,2],[3,4]])
    print(matrix_power(x, 2))

if __name__ == "__main__":
    main()
