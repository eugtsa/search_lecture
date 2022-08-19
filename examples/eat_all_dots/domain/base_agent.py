from domain.world import World
from domain.action import Action


class BaseAgent:
    def get_action(self, world: World) -> Action:
        raise NotImplementedError()
