import pygame


class Snake:
    def __init__(self):
        self.snake_body = [(200, 200), (210, 200), (220, 200)]
        self.snake_skin = pygame.Surface((10, 10))
        self.RIGHT = 3
        self.LEFT = 2
        self.DOWN = 1
        self.UP = 0
        self.snake_direction = self.LEFT

    def turn_up(x):
        self.snake_body[0] = (self.snake_body[0][0],
        self.snake_body[0][1] - 10)

    def turn_down(x):
        self.snake_body[0] = (self.snake_body[0][0],
        self.snake_body[0][1] + 10)

    def turn_left(x):
        self.snake_body[0] = (self.snake_body[0][0] - 10,
        self.snake_body[0][1])

    def turn_right(x):
        self.snake_body[0] = (self.snake_body[0][0] + 10,
        self.snake_body[0][1])


