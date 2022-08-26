from ctypes.wintypes import WPARAM
from domain.action import Action
from domain.world import World
from domain.base_agent import BaseAgent
from domain.point import Point
from heapq import heappush, heappop, heapify


class AstarAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self._actions = None

    def do_astar_search(self, world):
        # remember where we have been already
        states_been_at = {
            self.get_world_hashstr(world),
        }

        start_score = world.score

        states_heap = list()
        heapify(states_heap)

        heappush(states_heap, (0, world))

        while len(states_heap) > 0:
            prev_heap_score, state_to_explore = heappop(states_heap)

            # removing prev heuristic value out after we prioritized next state using it
            if state_to_explore.prev_world is not None:
                prev_heap_score = prev_heap_score - self.heuristic(state_to_explore.prev_world,state_to_explore)
            
            if state_to_explore.is_finished():
                break
            else:
                for action in self.get_allowed_actions(state_to_explore):
                    new_state = state_to_explore.apply_action(action)
                    new_state.prev_world = state_to_explore
                    new_state.action_from_prev_taken = action

                    new_world_hashstr = self.get_world_hashstr(new_state)
                    if new_world_hashstr not in states_been_at:
                        if new_state.score < start_score - 10:
                            continue

                        states_been_at.add(new_world_hashstr)

                        # this is what makes it an A* - we added heuristics on top of greedy
                        score_for_heap = prev_heap_score + self.get_cost(world.rules, state_to_explore,new_state) + self.heuristic(
                            state_to_explore, new_state
                        )

                        heappush(states_heap, (score_for_heap, new_state))

        print("Possible endgame scores: " + str(state_to_explore.score))

        # backtracking the actions from best end
        actions = list()
        while state_to_explore != world:
            actions.append(state_to_explore.action_from_prev_taken)
            state_to_explore = state_to_explore.prev_world

        return actions

    def get_cost(self,game_rules, prev_world, next_world):
        return 5 + prev_world.score - next_world.score

    # admissable heuristic - never overestimates the actual minimal cost
    def heuristic(self, prev_state, cur_state):
        value = 0
        if len(cur_state.dots) > 0:
            value += max(
                self.manhattan_distance(d, cur_state.cur_pos) for d in cur_state.dots
            )
        return value

    def manhattan_distance(self, p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def get_action(self, world: World) -> Action:
        if self._actions is None:
            self._actions = self.do_astar_search(world)

        return self._actions.pop()

    def get_world_hashstr(self, world: World):
        return "{},{},{},{}".format(
            world.cur_pos.x, world.cur_pos.y, world.dots, world.score
        )

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
