#!/usr/bin/env python3


def main():
    for i in range(1,11):
        t = triple(i)
        s = square(i)
        if s>t:
            break
        else:
            print(f"triple({i})=={t} square({i})=={s}")

def triple(x):
    return 3*x

def square(x):
    return x*x

if __name__ == "__main__":
    main()
