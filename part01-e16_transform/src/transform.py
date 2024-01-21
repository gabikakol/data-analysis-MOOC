#!/usr/bin/env python3

def transform(s1, s2):
    x = ((zip((s1.split()), s2.split())))
    return list(map(lambda x: int(x[0]) * int(x[1]), x))

def main():
    s1 = "1 5 3"
    s2 = "2 6 -1"
    print(transform(s1, s2))

if __name__ == "__main__":
    main()
