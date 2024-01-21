#!/usr/bin/env python3

def distinct_characters(L):
    #return {}
    dic = {}
    for i in range(len(L)):
        length = len(set(L[i]))
        dic[L[i]] = length
    return dic


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
