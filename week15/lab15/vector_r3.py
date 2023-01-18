import math

class VectorR3:
    """"
        Represents a vector in R^3, allows basic arithmetic
    """
    def __init__(x: 'Real', y: 'Real', z: 'Real'):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self) -> 'float':
        return math.sqrt(self.x + self.y + self.z)

    def __add__(self, other: 'VectorR3') -> 'VectorR3':
        sumX = self.x + other.x
        sumY = self.y + other.y
        sumZ = self.z + other.z
        return VectorR3(sumX, sumY, sumZ)