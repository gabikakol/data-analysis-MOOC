#!/usr/bin/env python3


def main():
    for i in range(1,11):
        s = square(i)
        t = triple(i)
        if s>t:
            break
        print(f"triple({i})=={t} square({i})=={s}")

def square(x):
    return x*x

def triple(x):
    return 3*x

if __name__ == "__main__":
    main()
