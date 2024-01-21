#!/usr/bin/env python3

def reverse_dictionary(d):
    dic = {}
    for key in d:
        fin = d[key]
        for i in range(len(fin)):
            if fin[i] in dic:
                dic[fin[i]].append(key)
            else:
                dic[fin[i]] = [key]
    return dic

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
