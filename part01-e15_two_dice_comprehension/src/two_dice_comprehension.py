#!/usr/bin/env python3

def main():
    L = [(i,j) for i in range(1,7) for j in range(1,7) if i+j==5]
    for i in L:
        print(i)

if __name__ == "__main__":
    main()
