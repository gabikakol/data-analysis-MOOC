#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    return a[a[:,1] > a[:,-2]]

    
def main():
    a = np.array([[8,9,3,8,8], [0,5,3,9,9], [1,2,3,4,5], [6,7,8,9,0]])
    print(column_comparison(a))

if __name__ == "__main__":
    main()
