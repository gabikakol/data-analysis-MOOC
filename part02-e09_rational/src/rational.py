#!/usr/bin/env python3

class Rational(object):
    
    def __init__(self, numerator, denominator):
        self.x = numerator
        self.y = denominator

    def __str__(self):
        return str(self.x) + "/" + str(self.y)

    def __add__(self,other):
        return Rational(self.x*other.y + other.x*self.y, self.y*other.y)

    def __sub__(self,other):
        return Rational(self.x*other.y - other.x*self.y, self.y*other.y)

    def __mul__(self,other):
        return Rational(self.x*other.x, self.y*other.y)

    def __truediv__(self,other):
        return Rational(self.x*other.y, self.y*other.x)

    def __eq__(self, __o: object) -> bool:
        return self.x/self.y == __o.x/__o.y
    
    def __lt__(self, __o: object) -> bool:
        return self.x/self.y < __o.x/__o.y

    def __le__(self, __o: object) -> bool:
        return self.x/self.y <= __o.x/__o.y

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
