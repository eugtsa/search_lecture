from ctypes.wintypes import WPARAM
from domain.action import Action
from domain.world import World
from domain.base_agent import BaseAgent
from domain.point import Point
import random
from queue import Queue


class BfsAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self._actions = None

    def do_search(self, world: World):
        # remember where we have been already

        states_been_at = {
            self.get_world_hashstr(world),
        }
        states_queue = Queue()
        states_queue.put(world)

        while not states_queue.empty():
            state_to_explore = states_queue.get()
            if state_to_explore.is_finished():
                break
            else:
                for action in self.get_allowed_actions(state_to_explore):
                    new_state = state_to_explore.copy().apply_action(action)
                    new_state.prev_world = state_to_explore
                    new_state.action_from_prev_taken = action
                    new_world_hashstr = self.get_world_hashstr(new_state)
                    if new_world_hashstr not in states_been_at:
                        states_been_at.add(new_world_hashstr)
                        states_queue.put(new_state)

        print("Endgame score: " + str(state_to_explore.score))

        # backtracking the actions from best end
        actions = list()
        while state_to_explore != world:
            actions.append(state_to_explore.action_from_prev_taken)
            state_to_explore = state_to_explore.prev_world

        return actions

    def get_action(self, world: World) -> Action:
        if self._actions is None:
            self._actions = self.do_search(world)

        return self._actions.pop()

    def get_world_hashstr(self, world: World):
        return "{},{},{},{}".format(world.cur_pos.x, world.cur_pos.y, world.dots, world.action_from_prev_taken)

    def get_allowed_actions(self, world: World):
        allowed_actions = list()

        cur_pos = world.cur_pos
        # let's scan the directions and don't bang into walls to avoid -3 penalty
        if Point(cur_pos.x - 1, cur_pos.y) not in world.map.walls:
            allowed_actions.append(Action.LEFT)
        if Point(cur_pos.x + 1, cur_pos.y) not in world.map.walls:
            allowed_actions.append(Action.RIGHT)
        if Point(cur_pos.x, cur_pos.y - 1) not in world.map.walls:
            allowed_actions.append(Action.UP)
        if Point(cur_pos.x, cur_pos.y + 1) not in world.map.walls:
            allowed_actions.append(Action.DOWN)
        return allowed_actions
