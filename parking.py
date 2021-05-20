import pygame
import gridObject as go
import consts

class Parking(go.GridObject):
    def __init__(self, pos, color = consts.YELLOW):
        super().__init__(pos, (255, 255, 0))
        self._vehicle = None

    def draw(self, win):
        x, y, w, h = self.shapeInfo()
        pygame.draw.line(win, consts.LIGHTGREY, (x, y), (x, y + consts.TILESIZE), 2)
        pygame.draw.line(win, consts.LIGHTGREY, (x + consts.TILESIZE - 2, y), (x + consts.TILESIZE - 2, y + consts.TILESIZE), 2)
        pygame.draw.line(win, self._color, (x + 8, y + 4), (x + 24, y + 4), 2)
