#!/usr/bin/env python3

def find_matching(L, pattern):
    ans = []
    for x, y in enumerate(L):
        if pattern in y:
            ans.append(x)
    return ans

def main():
    x = (find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))
    print(x)

if __name__ == "__main__":
    main()
