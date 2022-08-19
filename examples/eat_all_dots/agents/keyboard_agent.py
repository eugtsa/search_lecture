from domain.action import Action
import pygame
from time import sleep

from domain.world import World
from helpers.exceptions import QuitGameException, RetryLevelException, NextLevelException
from domain.base_agent import BaseAgent


class KeyboardAgent(BaseAgent):
    def get_action(self, world:World)->Action:
        while True:
            sleep(0.05)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise QuitGameException()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return Action.LEFT
                    if event.key == pygame.K_RIGHT:
                        return Action.RIGHT
                    if event.key == pygame.K_DOWN:
                        return Action.DOWN
                    if event.key == pygame.K_UP:
                        return Action.UP
                    if event.key == pygame.K_n:
                        raise NextLevelException()
                    if event.key == pygame.K_r:
                        raise RetryLevelException()
                    if event.key == pygame.K_q:
                        raise QuitGameException()
                    