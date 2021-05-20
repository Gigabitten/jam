import pygame
import drivable as d
import consts

class Intersection(d.Drivable):
    def __init__(self, pos, isNonIntersection = False, color = consts.DARKGREY):
        super().__init__(color)
        self._pos = pos
        self._nonIntersection = isNonIntersection

    def draw(self, win):
        x, y = self._pos[0], self._pos[1]
        pygame.draw.rect(win, self._color, pygame.Rect((x - 32, y - 32), (2 * 32, 2 * 32)))
        pygame.draw.line(win, consts.STOPRED, (x - 32, y + 24), (x - 32, y + 32))
        pygame.draw.line(win, consts.STOPRED, (x + 32, y - 32), (x + 32, y - 24))
        pygame.draw.line(win, consts.STOPRED, (x - 32, y - 32), (x - 24, y - 32))
        pygame.draw.line(win, consts.STOPRED, (x + 24, y + 32), (x + 32, y + 32))
