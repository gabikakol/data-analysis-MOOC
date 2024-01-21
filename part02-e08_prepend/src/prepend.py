#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here

    def __init__(self, x):
        self.x = x

    def write(self, string):
        print(self.x + string)


def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
