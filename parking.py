import pygame
import gridObject as go
import consts

class Parking(go.GridObject):
    def __init__(self, pos, orientation = 0, color = consts.YELLOW):
        super().__init__(pos, (255, 255, 0))
        self._vehicle = None
        self._orientation = orientation

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def orientation(self):
        return self._orientation

    def setVehicle(self, newVehic):
        self._vehicle = newVehic

    def draw(self, win):
        x, y, w, h = self.shapeInfo()
        pygame.draw.line(win, consts.LIGHTGREY, (x, y), (x, y + 32), 2)
        pygame.draw.line(win, consts.LIGHTGREY, (x + 32 - 2, y), (x + 32 - 2, y + 32), 2)
        pygame.draw.line(win, self._color, (x + 8, y + 4), (x + 24, y + 4), 2)
