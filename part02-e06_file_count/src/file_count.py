#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename) as f:
        lines = f.readlines()
        lns = len(lines)
        words = 0
        for line in lines:
            words += len(line.split())
        chars = 0
        for line in lines:
            chars += len(line)
    return lns, words, chars
        

def main():
    for filename in sys.argv[1:]:
        lns, words, chars = file_count(filename)
        print(f"{lns}\t{words}\t{chars}\t{filename}")
    #print(file_count(filename="src/test.txt"))

if __name__ == "__main__":
    main()
