from domain.point import Point
from typing import List


class Map:
    def __init__(
        self,
        size_x: int,
        size_y: int,
        walls: List[Point],
        start_pos: Point,
    ) -> None:
        self._size_x = size_x
        self._size_y = size_y
        self._walls = set(walls)
        self._start_pos = start_pos

    @property
    def start_pos(self):
        return self._start_pos

    def copy(self):
        return Map(self.size_x,self.size_y,[Point(w) for w in self.walls],Point(self.start_pos))

    @property
    def finish_pos(self):
        return self._finish_pos

    @property
    def walls(self):
        return self._walls

    @property
    def size_x(self):
        return self._size_x

    @property
    def size_y(self):
        return self._size_y
