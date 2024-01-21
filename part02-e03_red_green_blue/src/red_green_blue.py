#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    ans = []
    with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                x = re.findall("([0-9]+)", line)
                y = re.findall("([a-zA-Z]+[a-zA-Z ]*[0-9]*)", line)              
                string = f"{x[0]}\t{x[1]}\t{x[2]}\t{y[0]}"
                ans.append(string)
    ans.pop(0)
    return (ans)

def main():
    print(red_green_blue(filename="src/rgb.txt"))

if __name__ == "__main__":
    main()


#'255\t250\t250\tsnow'