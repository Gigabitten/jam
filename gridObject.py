import consts
import pygame
import visible as vis

class GridObject(vis.Visible):
    def __init__(self, pos = (0, 0), color = consts.BLUE, size = (1, 1)):
        pos = (pos[0] * consts.TILESIZE, pos[1] * consts.TILESIZE)
        size = (size[0] * consts.TILESIZE, size[1] * consts.TILESIZE)
        self._rect = pygame.Rect(pos, size)
        self._color = color

    def shapeInfo(self):
        return self._rect.x, self._rect.y, self._rect.width, self._rect.height

    def draw(self, win):
        pygame.draw.rect(win, self._color, self._rect)

    def pos(self):
        return self._rect.topleft

    def step(self):
        pass
