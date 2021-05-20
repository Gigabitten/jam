# Making this in a bit of a rush, so testing will consist of a big pile of asserts.
# Should be fine, honestly. It was hardly much more in the class assignments.

import pygame
import gridObject as go
import consts
import building as b
import vehicle as v
import parking as p
import jam

WIN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
game = jam.Game()
assert game.grid == []
assert game.tickInterval == 60
# side note around here:
# can't really be expected to test the drawing expect by just *watching it work*

# testing that keyboard input modifies state correctly
linesWere = game.displayGridLines
game.handleKeypress(pygame.K_g)
assert game.displayGridLines == (not linesWere)
game.handleKeypress(pygame.K_MINUS)
assert game.tickInterval == 70
game.handleKeypress(pygame.K_EQUALS)
game.handleKeypress(pygame.K_EQUALS)
assert game.tickInterval == 50
for i in range(10):
    game.handleKeypress(pygame.K_EQUALS)
assert game.tickInterval == 10
game.handleKeypress(pygame.K_0)
assert game.tickInterval == 60

# object initialization testing
gridObj = go.GridObject((1, 10))
assert gridObj.shapeInfo() == (32, 320, 32, 32)
assert gridObj._color == consts.BLUE

# buildings are basically just grid objects with a custom draw() so idk this is sorta unnecessary
build = b.Building((1, 10))
assert build.shapeInfo() == (32, 320, 32, 32)
assert build._color == consts.GREY

vehic = v.Vehicle((1, 10), consts.LIGHTGREY)
assert vehic.shapeInfo() == (32, 320, 32, 32)
assert vehic._color == consts.LIGHTGREY

parkingSpace = p.Parking((1, 10))
assert parkingSpace.shapeInfo() == (32, 320, 32, 32)
assert parkingSpace._color == consts.YELLOW
assert parkingSpace._vehicle == None

# testing the effects of stepping
for item in [gridObj, build, vehic, parkingSpace]:
    game.grid.append(item)

g = jam.Game()

g.addRoad((1, 0), (1, 10))
g.addBuilding((0, 10))
g.addParking((2, 8))
vhc = v.Vehicle((0, 0))
g.grid.append(vhc)

g.findIntersections()

g.step()
assert vhc._destination is not None
assert vhc._targetSpot is not None
oldPos = vhc.pos()
g.step()
g.step()
assert vhc._destination is not None
assert vhc._targetSpot is not None
assert oldPos != vhc.pos()

print("\nTests successfully passed!")
