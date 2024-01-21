#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    elif n > 0:
        return reduce(lambda x, _: x @ a, range(n-1), a)
    elif n < 0:
        return np.linalg.inv(matrix_power(a, abs(n)))

def main():
    a = np.array([[2, 1], [1, 1]])
    n = 3
    result = matrix_power(a, n)
    print(result)

if __name__ == "__main__":
    main()
