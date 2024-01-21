#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if n == 1:
        return np.array([[n]])
    else:
        bottom_left = np.eye(n, dtype=int)
        bottom_right = np.fliplr(bottom_left)
        bottom = []
        for i in range(len(bottom_left)):
                bottom.append(np.concatenate((bottom_left[i], bottom_right[i][1:])))
        bottom = np.array(bottom)
        top = (np.flipud(bottom))
        return np.concatenate((top, bottom[1:]))

def main():
    n = 1
    print(diamond(n))

if __name__ == "__main__":
    main()
