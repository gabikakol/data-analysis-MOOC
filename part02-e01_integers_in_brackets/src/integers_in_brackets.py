#!/usr/bin/env python3

import re

def integers_in_brackets(s):
    pat=r"(?:\[(\s*?[-+]?\d+\s*?)\])"
    return list(map(eval, re.findall(pat, s)))  

def main():
    s = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    print(integers_in_brackets(s))
    
if __name__ == "__main__":
    main()
