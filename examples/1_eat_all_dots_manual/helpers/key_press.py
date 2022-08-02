import pygame
from domain.exceptions import QuitGameException
from time import sleep

def press_any_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise QuitGameException()

            if event.type == pygame.KEYDOWN:
                return
        sleep(0.05)