from time import sleep
from yaml import parse
from domain.base_agent import BaseAgent
from helpers.exceptions import (
    RetryLevelException,
    NextLevelException,
    QuitGameException,
)
from helpers.level_loader import LevelLoader
from domain.rules import Rules
from domain.world import World
from helpers.world_renderer_simple import WorldRenderSimple
from helpers.key_press import press_any_key
import importlib
import argparse
import pygame


def raise_if_special_keys_pressed():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise QuitGameException()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                raise NextLevelException()
            if event.key == pygame.K_r:
                raise RetryLevelException()
            if event.key == pygame.K_q:
                raise QuitGameException()


def play_level(current_world: World, agent_class: BaseAgent):
    wrs = WorldRenderSimple(current_world.map.size_x, current_world.map.size_y)

    agent = agent_class()

    wrs.render_world(current_world)

    # draw initital world
    while not current_world.is_finished():
        action = agent.get_action(current_world)
        current_world = current_world.apply_action(action)
        wrs.render_world(current_world)
        sleep(0.05)
        raise_if_special_keys_pressed()
        # draw world + score
    wrs.render_world(current_world)
    press_any_key()
    return current_world.score


def to_classname(module_name: str):
    return "".join(w.capitalize() for w in module_name.split("_"))


def load_agent_class(agent_name: str):
    agent_module_name = agent_name
    agent_module = importlib.import_module("domain.agents." + agent_module_name)
    return getattr(agent_module, to_classname(agent_module_name))


def main(args):
    agent_class = load_agent_class(args.agent)
    ll = LevelLoader()
    total_score = 0

    for level_name in ll.list_levels():
        level_finished = False

        while not level_finished:
            try:
                map, dots = ll.load_level(level_name)
                current_world = World(Rules(), map, dots, map.start_pos, total_score)
                score = play_level(current_world, agent_class)
                total_score += score
                level_finished = True
            except NextLevelException as e:
                level_finished = True
            except RetryLevelException as e:
                pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--agent", type=str, default="keyboard_agent")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)
