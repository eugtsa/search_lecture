import random

from domain.action import Action
from domain.world import World
from domain.base_agent import BaseAgent


class NaiveRandomWalkAgent(BaseAgent):
    def get_action(self, world: World) -> Action:
        # taking random actions!
        return random.choice([Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT])
