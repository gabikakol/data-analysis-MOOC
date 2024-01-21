#!/usr/bin/env python3

def sum_equation(L):
    sum = 0
    if len(L) == 0:
        return "0 = 0"
    for i in L:
        sum += i
    return f"{' + '.join(str(i) for i in L)} = {sum}"

def main():
    L = [1,5,7]
    print(sum_equation(L))

if __name__ == "__main__":
    main()
