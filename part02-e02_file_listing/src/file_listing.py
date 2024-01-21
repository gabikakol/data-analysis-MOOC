##!/usr/bin/env python3

import re

def file_listing(filename="src/listing.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()
        files = []
        for line in lines:
            files.append(re.findall(r"\w+\.py", line))
        return files

def main():
    print(file_listing(filename="src/listing.txt"))
    
if __name__ == "__main__":
    main()

#-rwxr-xr-x 1 jttoivon hyad-all    2356 Dec 11 11:50 add_colab_link.py