class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Coords):
            return Coords(self.x + other.x, self.y+other.y)
        else:
            raise NotImplementedError

    def __repr__(self):
        return f'Coords({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Coords):
            return self.x == other.x and self.y == other.y
        else:
            raise NotImplementedError

    def __lt__(self, other):
        if isinstance(other, Coords):
            return (self.x, self.y) < (other.x, other.y)
        else:
            raise NotImplementedError
