from domain.action import Action

from domain.world import World
from domain.base_agent import BaseAgent
from domain.point import Point
import random


class SmartRandomWalkAgent(BaseAgent):
    def get_action(self, world: World) -> Action:
        allowed_actions = list()

        cur_pos = world.cur_pos
        # let's scan the directions and don't bang into walls to avoid -3 penalty
        if Point(cur_pos.x-1,cur_pos.y) not in world.map.walls:
            allowed_actions.append(Action.LEFT)
        if Point(cur_pos.x+1,cur_pos.y) not in world.map.walls:
            allowed_actions.append(Action.RIGHT)
        if Point(cur_pos.x,cur_pos.y-1) not in world.map.walls:
            allowed_actions.append(Action.UP)
        if Point(cur_pos.x,cur_pos.y+1) not in world.map.walls:
            allowed_actions.append(Action.DOWN)
            

        return random.choice(allowed_actions)
