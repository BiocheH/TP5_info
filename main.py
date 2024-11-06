#imports éventuels

class Point:
    def __init__(self, *args) -> None:
        if isinstance(args[0], Point) or isinstance(args[0], tuple):
            self.x, self.y = args[0][0], args[0][1]
        else:
            self.x, self.y = args[0], args[1]

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __getitem__(self, coord):
        if coord < -2 or coord > 1:
            raise IndexError
        return [self.x, self.y][coord]

print(Point(1, 2))
print(Point((3, 4)))
print(Point(Point(5, 6)))
