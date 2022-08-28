import random

from domain.action import Action
from domain.world import World
from domain.base_agent import BaseAgent
from domain.point import Point


class BetterRandomWalkAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self._actions = None

    def do_search(self, world: World, n_trials: int = 20):
        trials_ends = list()
        for _ in range(n_trials):
            trial_end = False

            state_to_explore = world
            while trial_end is False:
                action = random.choice(
                    self.get_allowed_actions(state_to_explore))
                new_state = state_to_explore.apply_action(action)
                new_state.prev_world = state_to_explore
                new_state.action_from_prev_taken = action
                state_to_explore = new_state
                if new_state.is_finished():
                    trial_end = True
                    trials_ends.append(new_state)

        # getting maximum end for game
        max_end = trials_ends[0]
        max_end_score = max_end.score
        for end in trials_ends:
            if end.score > max_end_score:
                max_end_score = end.score
                max_end = end
        print("Endgame score: " + str([end.score for end in trials_ends]))

        # backtracking the actions from best end
        actions = list()
        while max_end != world:
            actions.append(max_end.action_from_prev_taken)
            max_end = max_end.prev_world

        return actions

    def get_action(self, world: World) -> Action:
        if self._actions is None:
            self._actions = self.do_search(world, n_trials=80)

        return self._actions.pop()

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
