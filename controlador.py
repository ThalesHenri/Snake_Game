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
snake_obj = Snake()  # this will be our snake object
apple_obj = Apple()
apple_obj.onGrid_Random_Spawn()  # position get
run = True

# Game loop
while run:
    clock.tick(10)  # our clock object will set the game fps
    for event in pygame.event.get():#  event catcher for inputs
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and snake_obj.snake_direction != snake_obj.DOWN:
                snake_obj.move_up()
            if event.key == K_DOWN and snake_obj.snake_direction != snake_obj.UP:
                snake_obj.move_down()
            if event.key == K_LEFT and snake_obj.snake_direction != snake_obj.RIGHT:
                snake_obj.move_left()
            if event.key == K_RIGHT and snake_obj.snake_direction != snake_obj.LEFT:
                snake_obj.move_right()


    if colision(snake_obj.snake_body[0], apple_obj.position):
        apple_obj.onGrid_Random_Spawn()
        snake_obj.snake_body.append((0, 0))


    SCREEN.fill(BLACK)
    snake_obj.snake_skin.fill(WHITE)
    apple_obj.apple.fill(RED)
    for pos in snake_obj.snake_body:
        SCREEN.blit(snake_obj.snake_skin, pos)
    SCREEN.blit(apple_obj.apple, apple_obj.position)
    pygame.display.update()
