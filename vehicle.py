import pygame
import gridObject as go
import consts

class Vehicle(go.GridObject):
    def __init__(self, win, pos, color = consts.GREEN):
        super().__init__(win, pos, color)
        self._vertical = True

    def draw(self):
        x, y, w, h = self.shapeInfo()
        if self._vertical:
            pygame.draw.rect(self._win, self._color, pygame.Rect((x + 8, y),(w - 16, h)))
        else:
            pygame.draw.rect(self._win, self._color, pygame.Rect((x, y + 8),(w, h - 16)))

    def step(self, stepNum):
        if(stepNum % 60 == 0):
            if self._vertical:
                self._rect.y += consts.TILESIZE
            else:
                self._rect.x += consts.TILESIZE
            self._vertical = not self._vertical                
