import random
import pygame


class Apple:
    def __init__(self):
        self.apple = pygame.Surface((10, 10))
        self.x = 0
        self.y = 0
        self.position = self.x, self.y

    def onGrid_Random_Spawn(self):
        x = random.randint(0, 590) // 10 * 10
        y = random.randint(0, 590) // 10 * 10
        self.x = (x // 10 * 10)
        self.y = (y // 10 * 10)
        self.position = self.x, self.y
