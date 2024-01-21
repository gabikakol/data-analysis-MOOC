#!/usr/bin/env python3

def extract_numbers(s):
    x = s.split()
    L = []
    for i in x:
        try:
            L.append(int(i))
        except ValueError:
            try:
                L.append(float(i))
            except ValueError:
                pass
    return L

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
