# Enter you module contents here
__version__ = "0.1.0"
__author__ = "Gabriela"

__doc__="""module triangle contains functions for calculating the hypothenuse and area of a right triangle."""

def hypotenuse(a,b):
    """Returns the hypothenuse of a right triangle with sides a and b."""
    return (a**2 + b**2)**0.5


def area(a,b):
    """Returns the area of a right triangle with sides a and b."""
    return a*b/2