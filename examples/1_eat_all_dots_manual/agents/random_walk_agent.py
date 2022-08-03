from domain.action import Action

from domain.world import World
from domain.base_agent import BaseAgent
import random


class RandomWalkAgent(BaseAgent):
    def get_action(self, world: World) -> Action:
        return random.choice([Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT])
