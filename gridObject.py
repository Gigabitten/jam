import consts
import pygame

class GridObject():
    def __init__(self, win, pos = (0, 0), color = consts.BLUE, size = (1, 1)):
        self._win = win
        pos = (pos[0] * consts.TILESIZE, pos[1] * consts.TILESIZE)
        size = (size[0] * consts.TILESIZE, size[1] * consts.TILESIZE)
        self._rect = pygame.Rect(pos, size)
        self._color = color

    def draw(self):
        pygame.draw.rect(self._win, self._color, self._rect)

    def pos(self):
        return self._rect.topleft

    def step(self):
        pass
