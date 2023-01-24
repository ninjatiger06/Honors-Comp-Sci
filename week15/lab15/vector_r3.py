"""
Name: Jonas Pfefferman
Date: 1/18/23
Purpose: Creates a VectorR3 class, or a 3D vector, and run a number of tests on its functionality
"""

import math
import pickle
from numbers import Real

class VectorR3:
    """"
        Represents a vector in R^3, allows basic arithmetic
    """
    def __init__(self, x: 'Real', y: 'Real', z: 'Real'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> 'str':
        return f"⟨{self.x}, {self.y}, {self.z}⟩"
    
    def __repr__(self) -> 'str':
        return f"VectorR3({self.x}, {self.y}, {self.z})"

    def __abs__(self) -> 'float':
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other: 'VectorR3') -> 'VectorR3':
        sumX = self.x + other.x
        sumY = self.y + other.y
        sumZ = self.z + other.z
        return VectorR3(sumX, sumY, sumZ)

    def __sub__(self, other: 'VectorR3') -> 'VectorR3':
        diffX = self.x - other.x
        diffY = self.y - other.y
        diffZ = self.z - other.z
        return VectorR3(diffX, diffY, diffZ)

    def __mul__(self, other: 'VectorR3 | Real') -> 'Real | VectorR3':
        if type(other) == 'Real':
            prodX = self.x * other
            prodY = self.y * other
            prodZ = self.z * other
            return VectorR3(prodX, prodY, prodZ)
        else:
            prodX = self.x * other.x
            prodY = self.y * other.y
            prodZ = self.z * other.z
            return prodX + prodY + prodZ

    def __neg__(self) -> 'VectorR3':
        return VectorR3(self.x * -1, self.Y * -1, self.z * -1)

    def __bool__(self) -> 'bool':
        isVector = True
        if self.x == 0 and self.y == 0 and self.z == 0:
            isVector = False
        return isVector

    def __bytes__(self) -> 'bytes':
        dump = pickle.dumps(self)
        return dump

    def __eq__(self, other: 'VectorR3') -> 'bool':
        areEqual = True
        if self.x != other.x or self.y != other.y or self.z != other.z:
            areEqual = False
        return areEqual

    def __matmul__(self, other: 'VectorR3') -> 'VectorR3':
        newX = (self.y * other.z) - (self.z * other.y)
        newY = (self.z * other.x) - (self.x * other.z)
        newZ = (self.x * other.y) - (self.y * other.x)
        return VectorR3(newX, newY, newZ)

    def cos(*args) -> 'float':
        if len(args) == 1 and isinstance(args[0], Real):
            return math.cos(args[0])
        elif len(args) == 2 and isinstance(args[0], VectorR3) and isinstance(args[1], VectorR3):
            numerator = args[0] * args[1]
            denom1 = abs(args[0])
            denom2 = abs(args[1])
            denominator = denom1 * denom2
            return numerator / denominator
        else:
            print("Not properly implemented")

    def sin(*args) ->'float':
        if len(args) == 1 and isinstance(args[0], Real):
            return math.sin(args[0])
        elif len(args) == 2 and isinstance(args[0], VectorR3) and isinstance(args[1], VectorR3):
            vectorCos = VectorR3.cos(args[0], args[1])
            subtractor = vectorCos ** 2
            return math.sqrt(1 - subtractor)
        else:
            print("Not properly implemented")

    def tan(*args) -> 'float':
        if len(args) == 1 and isinstance(args[0], Real):
            return math.tan(args[0])
        elif len(args) == 2 and isinstance(args[0], VectorR3) and isinstance(args[1], VectorR3):
            vectorSin = VectorR3.sin(args[0], args[1])
            vectorCos = VectorR3.cos(args[0], args[1])
            print(vectorSin, vectorCos)
            return vectorSin / vectorCos
        else:
            print("Not properly implemented")


if __name__ == '__main__':
    vector1 = VectorR3(4, -1, 2)
    print(vector1)
    vector2 = eval(vector1.__repr__())
    # vector2 = VectorR3(1, 2, 7)
    print(vector2)

    vector3 = vector1 + vector2
    print(vector3)
    bool3 = vector3.__bool__()
    vector4 = VectorR3(0, 0, 0)
    print(vector4)
    bool4 = vector4.__bool__()
    print(bool3, bool4)

    vector5 = VectorR3(-2, 3, 5)

    pickle = vector4.__bytes__()
    print(pickle)

    cosine1 = VectorR3.cos(3)
    cosine2 = VectorR3.cos(vector1, vector5)
    cosBreak1 = VectorR3.cos(vector1)
    cosBreak2 = VectorR3.cos(vector1, 2)

    tan1 = VectorR3.tan(vector1, vector5)
    print(tan1)