import math

import numpy as np
from pygame.locals import *

Point = tuple[int, int]


class Snake(object):
    def __init__(self, rect: Rect, direction: float, speed: int):
        self.rect = rect
        self.direction = direction
        self.speed = speed
        self.tail = []
        self.last_pos = [rect.left, rect.top]
        self.segment_distance = rect.w/4

    def add_tail(self):
        self.tail.append(self.get_position_by_head())

    def get_position_by_head(self):
        x = math.cos(np.deg2rad(self.direction)) * self.rect.w
        y = math.sin(np.deg2rad(self.direction)) * self.rect.h
        return self.rect.x - x, self.rect.y - y

    def update_tail_position(self):
        if not self.tail or self.distance(self.rect.topleft, self.tail[0]) >= self.segment_distance:
            self.tail.insert(0, (self.rect.x, self.rect.y))
            self.tail.pop()

    @staticmethod
    def distance(pos1: Point, pos2: Point) -> float:
        return math.hypot(pos2[0] - pos1[0], pos2[1] - pos1[1])

    def move(self, delta_time: float = 1):
        x = math.cos(np.deg2rad(self.direction)) * self.speed * delta_time
        y = math.sin(np.deg2rad(self.direction)) * self.speed * delta_time
        self.rect.x += x
        self.rect.y += y
        self.update_tail_position()

    def rotate(self, degrees: int):
        self.direction += degrees

    def set_rotate(self, degrees: int):
        if self.direction - 180 == degrees or self.direction + 180 == degrees:
            return
        self.direction = degrees

    def __str__(self):
        return f"rect: {self.rect}, direction: {self.direction}"
