import pygame
import gridObject as go
import consts as c
import random

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def offsets(pos):
    x, y = pos
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def drivable(t):
    return t == c.ROAD or t == c.INTERSECTION

class Vehicle(go.GridObject):
    def __init__(self, pos, color = c.GREEN):
        super().__init__(pos, color)
        self._vertical = True
        self._waitTimer = 0
        self._destination = None
        self._targetSpot = None
        self._store = None

    def draw(self, win):
        x, y, w, h = self.shapeInfo()
        if self._vertical:
            pygame.draw.rect(win, self._color, pygame.Rect((x + 8, y),(w - 16, h)))
        else:
            pygame.draw.rect(win, self._color, pygame.Rect((x, y + 8),(w, h - 16)))

    def step(self, cache, vehicLocs, buildings, spots):
        if self._waitTimer > 0:
            self._waitTimer -= 1
            if self._waitTimer == 0:
                oldVert, oldPos = self._store
                self._vertical = oldVert
                self.setPos(oldPos)
                self._store = None
                self._rect.topleft = self.pos[0] * 32, self.pos[1] * 32
                self._targetSpot.setVehicle(None)
                self._targetSpot = None
                self._destination = None
            return
        if self._destination is None:
            self._destination = random.choice(buildings)
        if self._targetSpot is None or self._targetSpot.vehicle is not None:
            dest = self._destination.pos
            best, bestDist = spots[0], distance(dest, spots[0].pos)
            for spot in spots:
                if spot.vehicle is None:
                    dist = distance(dest, spot.pos)
                    if dist < bestDist:
                        best, bestDist = spot, dist
            self._targetSpot = best
        if self._targetSpot is not None:
            if self._targetSpot.pos in offsets(self.pos):
                self._store = self._vertical, self.pos
                self._rect.topleft = self._targetSpot._rect.topleft
                self.setPos(self._targetSpot.pos)
                self._vertical = self._targetSpot.orientation % 2 == 0
                self._waitTimer = 20
                self._targetSpot.setVehicle(self)
            else:
                # right, left, down, up
                validDirs = [False, False, False, False]
                offs = offsets(self.pos)
                dirs = []
                for off in offs:
                    if off in cache:
                        dirs.append(cache[off][0])
                    else:
                        dirs.append(None)
                right, left, down, up = dirs[0], dirs[1], dirs[2], dirs[3]
                validDirs[0] = drivable(up) and drivable(right) and down != c.INTERSECTION
                validDirs[1] = drivable(down) and drivable(left) and up != c.INTERSECTION
                validDirs[2] = drivable(right) and drivable(down) and left != c.INTERSECTION
                validDirs[3] = drivable(left) and drivable(up) and right != c.INTERSECTION
                prefs = []
                horizDone = False
                if self._targetSpot.pos[0] > self.pos[0]:
                    prefs.append(0)
                    prefs.append(1)
                    prefs.append(2)
                    prefs.append(3)                    
                elif self._targetSpot.pos[0] < self.pos[0]:
                    prefs.append(1)
                    prefs.append(0)
                    prefs.append(2)
                    prefs.append(3)                    
                elif self._targetSpot.pos[1] > self.pos[1]:
                    prefs.append(2)
                    prefs.append(0)
                    prefs.append(1)
                    prefs.append(3)                    
                elif self._targetSpot.pos[1] < self.pos[1]:
                    prefs.append(3)
                    prefs.append(0)
                    prefs.append(1)
                    prefs.append(2)                    

                x, y = self._rect.topleft
                posX, posY = self.pos
                for pref in prefs:
                    if validDirs[pref]:
                        if pref == 0:
                            self._rect.topleft = x + 32, y
                            self.setPos((posX + 1, posY))
                            self._vertical = False
                        elif pref == 1:
                            self._rect.topleft = x - 32, y
                            self.setPos((posX - 1, posY))                            
                            self._vertical = False                            
                        elif pref == 2:
                            self._rect.topleft = x, y + 32
                            self.setPos((posX, posY + 1))                            
                            self._vertical = True                            
                        elif pref == 3:
                            self._rect.topleft = x, y - 32
                            self.setPos((posX, posY - 1))                            
                            self._vertical = True
                        break
