import pygame

class Snake:
    def __init__(self, snake_body, snake_pos,snake_skin):
        self.snake_skin = pygame.Surface(10, 10)  # cobra em si
        self.snake_body = [(200, 200), (210, 200), (220, 200)]  # lista de checkagem pra saber o tamanho da cobra
        self.UP = 0
        self.DOWN = 1
        self.LEFT = 2
        self.RIGHT = 3
        self.my_direction = self.LEFT
    
    def snake_eat():
        self.snake_skin.append((0,0))
        return self.snake_body
