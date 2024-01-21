#!/usr/bin/env python3

import sys
from statistics import stdev

def summary(filename):
    with open(filename) as f:
        ans = []
        for line in f:
            try:
                ans.append(float(line))
            except ValueError:
                continue
    sm = sum(ans)
    diff = sm/len(ans)
    std = stdev(ans)
    return sm, diff, std

def main():
    for filename in sys.argv[1:]:
        sm, diff, std = summary(filename)
        print(f'File: {filename} Sum: {sm:.6f} Average: {diff:.6f} Stddev: {std:.6f}')


if __name__ == "__main__":
    main()