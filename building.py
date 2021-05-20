import pygame
import gridObject as go
import consts

class Building(go.GridObject):
    def __init__(self, pos, color = consts.GREY):
        super().__init__(pos, color)

    def draw(self, win):
        x, y, w, h = self.shapeInfo()
        pygame.draw.rect(win, self._color, self._rect)
        pygame.draw.rect(win, consts.WHITE, pygame.Rect((x + 16, y + 16),(8, 16)))
        pygame.draw.circle(win, consts.BLACK, (x + 22, y + 25), 1)
