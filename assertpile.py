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
assert game.stepNum == 0
assert game.displayGridLines == True
assert game.grid == []
# side note around here:
# can't really be expected to test the drawing expect by just *watching it work*
game.handleKeypress(pygame.K_g)
assert game.displayGridLines == False

gridObj = go.GridObject(WIN, (1, 10))
assert gridObj.shapeInfo() == (32, 320, 32, 32)
assert gridObj._color == consts.BLUE
assert gridObj._win == WIN

# buildings are basically just grid objects with a custom draw() so idk this is sorta unnecessary
build = b.Building(WIN, (1, 10))
assert build.shapeInfo() == (32, 320, 32, 32)
assert build._color == consts.GREY

vehic = v.Vehicle(WIN, (1, 10), consts.LIGHTGREY)
assert vehic.shapeInfo() == (32, 320, 32, 32)
assert vehic._color == consts.LIGHTGREY

park = p.Parking(WIN, (1, 10))
assert park.shapeInfo() == (32, 320, 32, 32)
assert park._color == consts.YELLOW

for item in [gridObj, build, vehic, park]:
    game.grid.append(item)
game.step()

print("\nTests successfully passed!")
