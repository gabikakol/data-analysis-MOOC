#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    return np.outer(np.arange(0, n), np.arange(0, n))

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
