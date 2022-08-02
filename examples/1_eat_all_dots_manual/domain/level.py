import numpy as np
from domain.point import Point
from domain.map import Map
from typing import List

class Level:
    def __init__(self, map:Map, start_pos:Point, goal_pos:Point, dots:List[Point]) -> None:
        self._start_pos = start_pos
        self._goal_pos = goal_pos
        self._map = map
        self._dots = dots