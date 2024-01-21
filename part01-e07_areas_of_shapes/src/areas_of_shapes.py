#!/usr/bin/env python3

import math

def main():

    while True:

        shape = input("Choose a shape (triangle, rectangle, circle): ")

        if len(shape) == 0:
            break

        elif shape == "triangle":
            a = float(input("Give base of the triangle: "))
            b = float(input("Give height of the triangle: "))
            area = a*b/2
            print(f"The area is {area:.6f}")

        elif shape == "rectangle":
            a = float(input("Give width of the rectangle: "))
            b = float(input("Give height of the rectangle: "))
            area = a*b
            print(f"The area is {area}")

        elif shape == "circle":
            r = float(input("Give the radius of the circle: "))
            area = math.pi*r**2
            print(f"The area is {area}")

        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
