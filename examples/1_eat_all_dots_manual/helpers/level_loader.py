import os
from domain.point import Point
from domain.map import Map


class LevelLoader:
    def list_levels(self):
        return sorted(os.listdir("levels"))

    def load_level(self, filename):
        with open("levels" + os.sep + filename) as f:
            max_size_x = 0
            max_size_y = 0
            walls = list()
            dots = set()
            start_pos = None
            finish_pos = None
            for y, l in enumerate(f.readlines()):
                max_size_y += 1

                l = l.strip()
                if len(l) > max_size_x:
                    max_size_x = len(l)

                for x, sym in enumerate(l):
                    if sym.lower() == "x":
                        walls.append(Point(x, y))
                    elif sym.lower() == "s":
                        start_pos = Point(x, y)
                    elif sym.lower() == "f":
                        finish_pos = Point(x, y)
                    elif sym == ".":
                        dots.add(Point(x, y))

        return (
            Map(
                size_x=max_size_x,
                size_y=max_size_y,
                walls=walls,
                start_pos=start_pos,
                finish_pos=finish_pos,
            ),
            dots,
        )
