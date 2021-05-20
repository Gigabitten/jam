import pygame
import visible as vis
import consts

class Drivable(vis.Visible):
    def __init__(self, color = consts.DARKGREY):
        super().__init__(color)
