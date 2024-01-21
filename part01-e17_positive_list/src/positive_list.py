#!/usr/bin/env python3

def positive_list(L):
    x = filter(lambda x: x > 0, L)
    return list(x)

def main():
    L = [1, -2, 3, -4, 5]
    print((positive_list(L)))

if __name__ == "__main__":
    main()
