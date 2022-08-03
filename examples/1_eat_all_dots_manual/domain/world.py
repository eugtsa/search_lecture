from domain.point import Point
from domain.rules import Rules
from domain.action import Action
from domain.map import Map
from typing import Set


class World:
    def __init__(
        self,
        rules: Rules,
        map: Map,
        dots: Set[Point],
        cur_pos: Point,
        cur_score: int,
        tick_num: int = 0,
    ) -> None:
        self._rules = rules
        self._map = map
        self._dots = dots
        self._cur_pos = cur_pos
        self._cur_score = cur_score
        self._tick_num = tick_num

    @property
    def map(self):
        return self._map

    @property
    def tick_num(self):
        return self._tick_num

    @property
    def dots(self):
        return self._dots

    @property
    def score(self):
        return self._cur_score

    @property
    def cur_pos(self):
        return self._cur_pos

    def is_finished(self):
        return self._cur_pos == self._map.finish_pos

    def apply_action(self, action: Action):
        # if action is not Action.ALL_ACTIONS:
        #    raise NotImplementedError()
        # parse actions
        new_pos = self._cur_pos
        new_dots = self._dots

        if action == Action.LEFT:
            new_pos = Point(self._cur_pos.x - 1, self._cur_pos.y)
        elif action == Action.RIGHT:
            new_pos = Point(self._cur_pos.x + 1, self._cur_pos.y)
        elif action == Action.UP:
            new_pos = Point(self._cur_pos.x, self._cur_pos.y - 1)
        elif action == Action.DOWN:
            new_pos = Point(self._cur_pos.x, self._cur_pos.y + 1)

        # get score change
        score_change = self._rules.move_score

        if new_pos in self._map.walls:
            score_change = self._rules.hit_wall_score
            new_pos = self._cur_pos

        elif new_pos in self._dots:
            score_change = self._rules.dot_score
            new_dots = set([d for d in self._dots if d != new_pos])

        elif new_pos == self._map.finish_pos:
            score_change = self._rules.finish_score

        # returning new world state
        return World(
            rules=self._rules,
            map=self._map,
            dots=new_dots,
            cur_pos=new_pos,
            cur_score=self._cur_score + score_change,
            tick_num=self.tick_num + 1,
        )
