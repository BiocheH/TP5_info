from cmath import phase
from math import sqrt

class Point:
    def __init__(self, *args) -> None:
        if isinstance(args[0], Point) or isinstance(args[0], tuple):
            self.x, self.y = args[0][0], args[0][1]
        else:
            self.x, self.y = args[0], args[1]

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __getitem__(self, coord) -> float:
        if coord < -2 or coord > 1:
            raise IndexError
        return [self.x, self.y][coord]

    def __eq__(self, other) -> bool:
        assert isinstance(other, Point), 'can only compare two instances of Point'
        return self[0] == other[0] and self[1] == other[1]

    def __add__(self, other):
        return Point(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return Point(self[0] - other[0], self[1] - other[1])

    def angle(self, other) -> float:
        assert isinstance(other, Point), 'given point must be instance of Point'
        assert self != other, 'given point must be different from current point in order to trace a line going through both'
        cpoint = complex(self[0] - other[0], self[1] - other[1])
        return phase(cpoint)

    def distance(self, other) -> float:
        assert isinstance(other, Point), 'given point must be instance of Point'
        diff = self - other
        return sqrt(diff[0]**2 + diff[1]**2)

    def det(self, A, B) -> float:
        assert isinstance(A, Point) and isinstance(B, Point), 'given points must be instances of Point'
        diffA = A - self
        diffB = B - self
        return diffA[0]*diffB[1] - diffB[0]*diffA[1]
    # On remarque que det>0 quand la droite est au-dessus du point courant, =0 quand alignés, <0 quand en dessous.



p = Point(1, 2)
q = Point((3, 2))
r = Point(1, 3)
print(p.angle(r))
print(p.distance(r))
print(p.det(q, r))
