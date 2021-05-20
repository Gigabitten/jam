import pygame
import gridObject as go
import consts

class Vehicle(go.GridObject):
    def __init__(self, pos, color = consts.GREEN):
        super().__init__(pos, color)
        self._vertical = True

    def draw(self, win):
        x, y, w, h = self.shapeInfo()
        if self._vertical:
            pygame.draw.rect(win, self._color, pygame.Rect((x + 8, y),(w - 16, h)))
        else:
            pygame.draw.rect(win, self._color, pygame.Rect((x, y + 8),(w, h - 16)))

    def step(self):
        self._rect.y += consts.TILESIZE
