"""
Name: Jonas Pfefferman
Date: 1/18/23
Purpose: Creates a VectorR3 class, or a 3D vector, and runs a number of tests on
        its functionality
"""

from __future__ import annotations
import math
import pickle
from numbers import Real

class VectorR3:
    """"Represents a vector in R^3, allows basic arithmetic"""

    def __init__(self, x: Real, y: Real, z: Real):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        """Returns user-friendly version of vector"""

        return f"⟨{self.x}, {self.y}, {self.z}⟩"
    
    def __repr__(self) -> str:
        """Returns string that could be used to recreate the vector"""

        return f"VectorR3({self.x}, {self.y}, {self.z})"

    def __abs__(self) -> float:
        """Finds the pythagorean length in R3"""

        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other: VectorR3) -> VectorR3:
        """Component-wise addition(adding each coordinate to its counterpart)"""

        sumX = self.x + other.x
        sumY = self.y + other.y
        sumZ = self.z + other.z
        return VectorR3(sumX, sumY, sumZ)

    def __iadd__(self, other: VectorR3) -> VectorR3:
        """Component-wise addition but for +="""

        self.x += other.x
        self.y += other.y
        self.z += other.z
        return VectorR3(self.x, self.y, self.z)

    def __sub__(self, other: VectorR3) -> VectorR3:
        """ Component-wise subtraction - same process as addition"""

        diffX = self.x - other.x
        diffY = self.y - other.y
        diffZ = self.z - other.z
        return VectorR3(diffX, diffY, diffZ)

    def __isub__(self, other: VectorR3) -> VectorR3:
        """Component-wise subtraction but for -="""

        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return VectorR3(self.x, self.y, self.z)

    def __mul__(self, other: VectorR3 | Real) -> Real | VectorR3:
        """Either dot product (if both VectorR3's) or scalar multiplication"""

        if isinstance(other, Real):
            prodX = self.x * other
            prodY = self.y * other
            prodZ = self.z * other
            return VectorR3(prodX, prodY, prodZ)
        else:
            prodX = self.x * other.x
            prodY = self.y * other.y
            prodZ = self.z * other.z
            return prodX + prodY + prodZ

    def __neg__(self) -> VectorR3:
        """Negates each coordinate"""

        # return VectorR3(self.x * -1, self.Y * -1, self.z * -1)
        return self * -1

    def __bool__(self) -> bool:
        """If vector isn't all 0's returns True, if 0 vector returns False"""

        isVector = True
        if self.x == 0 and self.y == 0 and self.z == 0:
            isVector = False
        return isVector

    def __bytes__(self) -> bytes:
        """Returns self as binary pickle"""

        dump = pickle.dumps(self)
        return dump

    def __eq__(self, other: VectorR3) -> bool:
        """Checks to see if two vectors are equal"""

        areEqual = True
        if self.x != other.x or self.y != other.y or self.z != other.z:
            areEqual = False
        return areEqual

    def __matmul__(self, other: VectorR3) -> VectorR3:
        """Returns a cross-product between two vectors in R3"""

        newX = (self.y * other.z) - (self.z * other.y)
        newY = (self.z * other.x) - (self.x * other.z)
        newZ = (self.x * other.y) - (self.y * other.x)
        return VectorR3(newX, newY, newZ)

    def __len__(self: VectorR3) -> Tuple:
        """Returns length of 3 (list is x-cord, y-cord, z-cord) as a tuple"""
        return 3


def cos(*args: Real | [VectorR3, VectorR3]) -> float:
    """Returns math.cos of number or returns cos of angle between vectors"""

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

def sin(*args: Real | [VectorR3, VectorR3]) -> float:
    """Returns math.sin of number or returns sin of angle between vectors"""

    if len(args) == 1 and isinstance(args[0], Real):
        return math.sin(args[0])
    elif len(args) == 2 and isinstance(args[0], VectorR3) and isinstance(args[1], VectorR3):
        vectorCos = cos(args[0], args[1])
        subtractor = vectorCos ** 2
        return math.sqrt(1 - subtractor)
    else:
        print("Not properly implemented")

def tan(*args: Real | [VectorR3, VectorR3]) -> float:
    """Returns math.tan of number or returns tan of angle between vectors"""

    if len(args) == 1 and isinstance(args[0], Real):
        return math.tan(args[0])
    elif len(args) == 2 and isinstance(args[0], VectorR3) and isinstance(args[1], VectorR3):
        vectorSin = sin(args[0], args[1])
        vectorCos = cos(args[0], args[1])
        return vectorSin / vectorCos
    else:
        print("Not properly implemented")


def main():
    vector1 = VectorR3(4, -1, 2)
    vector2 = eval(vector1.__repr__())

    assert vector1 == vector2

    vector3 = vector1 + vector2
    bool3 = vector3.__bool__()
    assert vector3
    assert vector3 == VectorR3(8, -2, 4)
    assert vector1 - vector2 == VectorR3(0, 0, 0)

    vector6 = eval(vector1.__repr__())
    vector6 += vector2
    assert vector6 == VectorR3(8, -2, 4)
    vector7 = eval(vector1.__repr__())
    vector7 -= vector2
    assert vector7 == VectorR3(0, 0, 0)

    vector4 = VectorR3(0, 0, 0)
    bool4 = vector4.__bool__()
    assert not vector4

    pickle = vector4.__bytes__()
    print(pickle)

    vector5 = VectorR3(-2, 3, 5)

    assert vector1 * 2 == VectorR3(8, -2, 4)
    assert vector1 * vector5 == -1

    assert -vector1 == VectorR3(-4, 1, -2)

    assert vector1 @ vector5 == VectorR3(-11, -24, 10)

    assert len(vector1) == 3

    assert cos(3) == math.cos(3)
    assert sin(3) == math.sin(3)
    assert tan(3) == math.tan(3)

    assert cos(vector1, vector5) ==  -0.03539961627023944
    assert sin(vector1, vector5) == 0.9993732371681362
    assert tan(vector1, vector5) == -28.231188426986208



if __name__ == '__main__':
    main()