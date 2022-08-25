from ctypes.wintypes import WPARAM
from domain.action import Action
from domain.world import World
from domain.base_agent import BaseAgent
from domain.point import Point
from heapq import heappush,heappop,heapify


class UcsAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self._actions = None

    def do_ucs(self, world):
        # remember where we have been already
        states_been_at = {
            self.get_world_hashstr(world),
        }

        start_score = world.score

        states_heap = list()
        heapify(states_heap)

        heappush(states_heap,(0,world))

        possible_ends = list()

        while len(states_heap)>0:
            prev_heap_score, state_to_explore = heappop(states_heap)
            if state_to_explore.is_finished():
                possible_ends.append(state_to_explore)
                break
            else:
                for action in self.get_allowed_actions(state_to_explore):
                    new_state = state_to_explore.copy().apply_action(action)
                    new_world_hashstr = self.get_world_hashstr(new_state)
                    if new_world_hashstr not in states_been_at:
                        if new_state.score<start_score-20:
                            continue
                        new_state.prev_world = state_to_explore
                        new_state.action_from_prev_taken = action
                        states_been_at.add(new_world_hashstr)
                        score_for_heap = prev_heap_score + (5 + state_to_explore.score - new_state.score)
                        heappush(states_heap,(score_for_heap, new_state))

        # getting maximum end for game
        max_end = possible_ends[0]
        max_end_score = max_end.score
        for end in possible_ends:
            if end.score > max_end_score:
                max_end_score = end.score
                max_end = end
        print("Possible endgame scores: " + str([end.score for end in possible_ends]))

        # backtracking the actions from best end
        actions = list()
        while max_end != world:
            actions.append(max_end.action_from_prev_taken)
            max_end = max_end.prev_world

        return actions

    def heuristic(self, prev_state, cur_state):
        return cur_state.score-prev_state.score

    def get_action(self, world: World) -> Action:
        if self._actions is None:
            self._actions = self.do_ucs(world)

        return self._actions.pop()

    def get_world_hashstr(self, world: World):
        return "{},{},{},{}".format(world.cur_pos.x, world.cur_pos.y, world.dots, world.score)

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
