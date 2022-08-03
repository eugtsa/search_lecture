from re import X


class Point:
    def __init__(self, x: int, y: int = None) -> None:
        if y is None:
            if type(x) is Point:
                self._x = x.x
                self._y = x.y
        else:
            self._x = x
            self._y = y

    def __hash__(self):
        return self.x * 100 + self.y

    def __str__(self):
        return 'Point(x={},y={})'.format(self.x,self.y)

    def __repr__(self):
        return self.__str__()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, __o: object) -> bool:
        if __o.x == self.x:
            return __o.y == self.y
        return False
