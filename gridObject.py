import consts
import pygame
import visible as vis

class GridObject(vis.Visible):
    def __init__(self, pos = (0, 0), color = consts.BLUE, size = (1, 1)):
        self._pos = pos
        size = (size[0] * 32, size[1] * 32)
        x, y = pos[0] * 32, pos[1] * 32
        self._rect = pygame.Rect((x, y), size)
        self._color = color

    def shapeInfo(self):
        return self._rect.x, self._rect.y, self._rect.width, self._rect.height

    def draw(self, win):
        pygame.draw.rect(win, self._color, self._rect)

    @property
    def pos(self):
        return self._pos

    def setPos(self, newPos):
        self._pos = newPos

    def step(self, cache, vehicLocs, buildings, spots):
        pass
