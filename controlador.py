from snake import Snake
from apple import Apple 
import pygame
import random
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


pygame.init()

"""Screen"""
SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

"""Pygame Objects"""

clock = pygame.time.Clock()  # this will be our clock object
obj = Snake()  # this will be our snake object


run = True

# Game loop
while run:
    clock.tick(10)  # our clock object will set the game fps
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and obj.snake_direction != obj.DOWN:
                obj.snake_direction = obj.UP
            if event.key == K_DOWN and obj.snake_direction != obj.UP:
                obj.snake_direction = obj.DOWN
            if event.key == K_LEFT and obj.snake_direction != obj.RIGHT:
                obj.snake_direction = obj.LEFT
            if event.key == K_RIGHT and obj.snake_direction != obj.LEFT:
                obj.snake_direction = obj.RIGHT
    for c in range(len(obj.snake_body) - 1, 0, -1):
        obj.snake_body[c] = (obj.snake_body[c - 1][0],
        obj.snake_body[c - 1][1])

    if obj.snake_direction == obj.UP:
        obj.snake_body[0] = (obj.snake_body[0][0],
        obj.snake_body[0][1] - 10)
    if obj.snake_direction == obj.DOWN:
        obj.snake_body[0] = (obj.snake_body[0][0],
        obj.snake_body[0][1] + 10)
    if obj.snake_direction == obj.RIGHT:
        obj.snake_body[0] = (obj.snake_body[0][0] + 10, obj.snake_body[0][1])
    if obj.snake_direction == obj.LEFT:
        obj.snake_body[0] = (obj.snake_body[0][0] - 10, obj.snake_body[0][1])


    SCREEN.fill(BLACK)
    obj.snake_skin.fill(WHITE)
    for pos in obj.snake_body:
        SCREEN.blit(obj.snake_skin, pos)
    pygame.display.update()
