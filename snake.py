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

    def move(self):
        for c in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[c] = (self.snake_body[c - 1][0],
            self.snake_body[c - 1][1])
        if self.snake_direction == 0:  # UP
            self.snake_body[0] = (self.snake_body[0][0],
            self.snake_body[0][1] - 10)
        if self.snake_direction == 1:  # DOWN
            self.snake_body[0] = (self.snake_body[0][0],
            self.snake_body[0][1] + 10)
        if self.snake_direction == 3:  # RIGHT
            self.snake_body[0] = (self.snake_body[0][0] + 10,
            self.snake_body[0][1])
        if self.snake_direction == 2: # LEFT
            self.snake_body[0] = (self.snake_body[0][0] - 10,
            self.snake_body[0][1])