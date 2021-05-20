import pygame
import drivable as d
import consts

class Road(d.Drivable):
    def __init__(self, start, end, isVertical, color = consts.DARKGREY):
        super().__init__(color)
        self._vertical = isVertical
        self._start = start
        self._start = (start[0] * 32,
                       start[1] * 32)
        self._end = (end[0] * 32,
                     end[1] * 32)
        self.vertical = None
        if start[0] == end[0]:
            self.vertical = True
        elif start[1] == end[1]:
            self.vertical = False
        # a value of None lets it know that it's neither and should not be acknowledged

    def start(self):
        return self._start
    
    def end(self):
        return self._end

    def draw(self, win):
        pygame.draw.line(win, self._color, self._start, self._end, 32 * 2)        
        pygame.draw.line(win, consts.YELLOW, self._start, self._end, 5)
        pygame.draw.line(win, consts.BLACK, self._start, self._end, 3)
