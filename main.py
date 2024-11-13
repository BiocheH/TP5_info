from cmath import phase
from math import sqrt
from math import pi
import matplotlib.pyplot as plt

class Point:
    def __init__(self, *args) -> None:
        if isinstance(args[0], Point) or isinstance(args[0], tuple) or isinstance(args[0], list):
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

    def __lt__(self, other):
        return self[0] < other[0] or (self[0] == other[0] and self[1] < other[1])

    def __le__(self, other):
        return self < other or self == other

    def __add__(self, other):
        return Point(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return Point(self[0] - other[0], self[1] - other[1])

    def angle(self, other) -> float:
        assert isinstance(other, Point), 'given point must be instance of Point'
        assert self != other, 'given point must be different from current point in order to trace a line going through both'
        cpoint = complex(self[0] - other[0], self[1] - other[1])
        return phase(cpoint) + pi

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

class PointList:
    def __init__(self, *args) -> None:
        if isinstance(args[0], list) or isinstance(args[0], tuple):
            temp = list(args[0])
            shallow_copy = temp[:]
        else:
            temp = list(args)
            shallow_copy = temp[:]
        self.l = []
        for elt in shallow_copy:
            self.l.append(Point(elt))
        self.l.sort()
        self.l = sort_by_angle(self.l)

    def __str__(self) -> str:
        return 'Points:\n - ' + '\n - '.join(str(elt) for elt in self.l)

    def plot(self):
        xs = [elt[0] for elt in self.l]
        ys = [elt[1] for elt in self.l]
        plt.scatter(xs, ys)
        for i in range(len(self.l)):
            plt.annotate(i, (xs[i], ys[i]))
        plt.show()

    def extreme(self) -> Point:
        return min(self.l)
    # On remarque quand, pour une instance 'first_list' de PointList, on récupère un point à l'aide de extreme,
    # que ce point est extremal (et notamment minimal) car la relation < définie par (a,b) < (c,d) <=>
    # <=> (a<c) ou (a=c et b<d) est bel et bien une relation d'ordre.

    def without_alignment(self) -> list:
        temp_point = self.l[0]
        for i in range(1, len(self.l) - 1):
            popped = 0
            if temp_point.angle(self.l[i - popped]) == temp_point.angle(self.l[i + 1 - popped]):
                if self.l[i - popped] < self.l[i + 1 -popped]:
                    self.l.pop(i)
                else:
                    self.l.pop(i+1)
                popped += 1
    # effectivement, si 3 points sont alignés, alors celui du milieu est soit dans le polygone et peut être retiré
    # sans modifier l'enveloppe convexe, soit entre deux angles, et idem.


def sort_by_angle(l: list) -> list:
    assert all(isinstance(elt, Point) for elt in l), 'given list must contain only Points'
    temp = l[:]
    temp_point = temp.pop(0)
    temp.sort(key=lambda x: temp_point.angle(x))
    temp = [temp_point] + temp
    return temp


p = Point(1, 3)
q = Point((2, 3))
r = Point(1, 2)
first_list = PointList(p, q, r)
print(first_list)
print(r.angle(p))
print(r.angle(q))
print(first_list.without_alignment())
first_list.plot()
