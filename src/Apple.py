from pygame.locals import *
from random import randint
Rgb = tuple[int, int, int]


class Apple:
    def __init__(self, rect: Rect, color: Rgb):
        self.rect = rect
        self.color = color

    def random_spawn(self, x1: int, y1: int, x2: int, y2: int):
        x = randint(x1, x2)
        y = randint(y1, y2)
        self.rect.x = x
        self.rect.y = y
