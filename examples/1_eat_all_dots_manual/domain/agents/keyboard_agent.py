from domain.action import Action
from domain.world import World
from domain.exceptions import QuitGameException
import pygame


class KeyboardAgent:
    def get_action(self, world:World)->Action:
        while True:
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