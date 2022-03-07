import pygame, random
from pygame.locals import *

"""Functions"""


def colision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def onGrid_random_spawn():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10) and (y // 10 * 10)


"""Colors"""

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0

"""Directions"""

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

my_direction = LEFT

pygame.init()

"""Screen"""
SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()  # this will be our clock object

run = True

# Game loop
while run:
    clock.tick(10)  # our clock object will set the game fps
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    SCREEN.fill(BLACK)
    pygame.display.update()
