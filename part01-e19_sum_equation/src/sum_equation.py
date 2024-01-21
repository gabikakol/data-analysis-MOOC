#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    else:
        s = sum(L)
        #return f"{s} = {' + '.join(map(str, L))}"
        return f"{' + '.join(map(str, L))} = {s}"

def main():
    L = [1,5,7]
    print(sum_equation(L))

if __name__ == "__main__":
    main()
