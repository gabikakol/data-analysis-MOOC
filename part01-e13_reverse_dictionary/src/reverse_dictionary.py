#!/usr/bin/env python3

def reverse_dictionary(d):
    dic = {}
    for key, value in d.items():
        for v in value:
            if v in dic:
                dic[v].append(key)
            else:
                dic[v] = [key]
    return dic

def main():
    x = reverse_dictionary({"a": ['g'], "b": ['h'], "c": ['g']})
    print(x)

if __name__ == "__main__":
    main()
