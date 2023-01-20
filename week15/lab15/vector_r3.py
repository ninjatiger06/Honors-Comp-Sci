import math
import pickle

class VectorR3:
    """"
        Represents a vector in R^3, allows basic arithmetic
    """
    def __init__(self, x: 'Real', y: 'Real', z: 'Real'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"⟨{self.x}, {self.y}, {self.z}⟩"
    
    def __repr__(self):
        return f"VectorR3({self.x}, {self.y}, {self.z})"

    def __abs__(self) -> 'float':
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

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


if __name__ == '__main__':
    vector1 = VectorR3(2, 8, 6)
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

    pickle = vector4.__bytes__()
    print(pickle)

    print(vector1 == vector2, vector3 == vector4, vector1 == vector3)