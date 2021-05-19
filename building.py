import pygame
import gridObject as go
import consts

class Building(go.GridObject):
    def __init__(self, win, pos, color = consts.GREY):
        super().__init__(win, pos, color)

    def draw(self):
        x, y, w, h = self.shapeInfo()
        pygame.draw.rect(self._win, self._color, self._rect)
        pygame.draw.rect(self._win, consts.WHITE, pygame.Rect((x + 16, y + 16),(8, 16)))
        pygame.draw.circle(self._win, consts.BLACK, (x + 22, y + 25), 1)
