from snake import Snake
from apple import Apple
import pygame
from pygame.locals import *

"""Functions"""


def colision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


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
obj2 = Apple()
obj2.onGrid_Random_Spawn()  # position get
run = True

# Game loop
while run:
    clock.tick(10)  # our clock object will set the game fps
    for event in pygame.event.get():#  event catcher for inputs
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
    if colision(obj.snake_body[0], obj2.position):
        obj2.onGrid_Random_Spawn()
        obj.snake_body.append((0, 0))

    for c in range(len(obj.snake_body) - 1, 0, -1):
        obj.snake_body[c] = (obj.snake_body[c - 1][0],
        obj.snake_body[c - 1][1])
    if obj.snake_direction == obj.UP:  # Snake moving
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
    obj2.apple.fill(RED)
    for pos in obj.snake_body:
        SCREEN.blit(obj.snake_skin, pos)
    SCREEN.blit(obj2.apple, obj2.position)
    pygame.display.update()
