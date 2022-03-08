import pygame


class Snake:
    def __init__(self, snake_pos):
        self.snake = pygame.Surface(10, 10)
        self.snake_body = [(200, 200), (210, 200), (220, 200)]
