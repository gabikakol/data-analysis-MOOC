#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, string):
        self.string = string

    def write(self, text):
        print(self.string + text)

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
