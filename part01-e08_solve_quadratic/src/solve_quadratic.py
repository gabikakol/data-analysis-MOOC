#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    elif d == 0:
        x = -b/(2*a)
        return (x,x)
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return (x1, x2)


def main():
    print(solve_quadratic(1, 0, -1))

if __name__ == "__main__":
    main()
