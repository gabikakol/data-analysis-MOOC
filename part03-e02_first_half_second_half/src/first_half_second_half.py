#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    x = int(a.shape[1] / 2)
    b = a[:,:x]
    c = a[:,x:]
    y = np.sum(b,axis=1) > np.sum(c,axis=1)
    return np.array(a[y])

def main():
    a = np.array([[1, 3, 4, 2],
                [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()