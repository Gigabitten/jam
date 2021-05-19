import pygame
import gridObject as go
import consts

class Parking(go.GridObject):
    def __init__(self, win, pos, color = consts.GREY):
        super().__init__(win, pos, (255, 255, 0))

    def draw(self):
        x, y, w, h = self.shapeInfo()
        pygame.draw.line(self._win, consts.LIGHTGREY, (x, y), (x, y + consts.TILESIZE), 2)
        pygame.draw.line(self._win, consts.LIGHTGREY, (x + consts.TILESIZE - 2, y), (x + consts.TILESIZE - 2, y + consts.TILESIZE), 2)
        pygame.draw.line(self._win, consts.YELLOW, (x + 8, y + 4), (x + 24, y + 4), 2)
