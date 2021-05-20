import pygame
import consts as c
import gridObject as go
import vehicle as v
import building as b
import parking as p
import road as r
import intersection as i

WIN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Jam")
FPS = 60

class Game():
    def __init__(self):
        self.displayGridLines = False
        self.grid = []
        # ticks per frame
        self.tickInterval = 60
        self.xAxisRoads = []
        self.yAxisRoads = []
        self.intersections = []
        self.cache = {}
        self.buildings = []
        self.spots = []

    def findIntersections(self):
        # excuse how obnoxious this section is
        for xRoad in self.xAxisRoads:
            for yRoad in self.yAxisRoads:
                # a nonintersection is where two roads meet,
                # but don't overlap
                nonIntersection = False                
                if (xRoad.start()[0] <= yRoad.start()[0] and
                    yRoad.start()[0] <= xRoad.end()[0] and
                    yRoad.start()[1] <= xRoad.start()[1] and
                    xRoad.start()[1] <= yRoad.end()[1]):
                    if (xRoad.start() == yRoad.start() or
                        xRoad.start() == yRoad.end() or
                        xRoad.end() == yRoad.start() or
                        xRoad.end() == yRoad.end()):
                        nonIntersection = True
                    self.addIntersection((yRoad.start()[0],
                                          xRoad.start()[1]),
                                         nonIntersection)
                        
    def drawIntersections(self):
        for intersection in self.intersections:
            intersection.draw(WIN)
    
    def drawRoads(self):
        for road in self.xAxisRoads:
            road.draw(WIN)
        for road in self.yAxisRoads:
            road.draw(WIN)
        self.drawIntersections()

    def createWindow(self, newDims):
        WIN = pygame.display.set_mode(newDims, pygame.RESIZABLE)
        pygame.display.set_caption("Jam")
        print("Window size: ", end="")
        print(WIN.get_size())

    def drawGridLines(self):
        w, h = pygame.display.get_surface().get_size()
        if self.displayGridLines:
            for x in range(0, w, 32):
                pygame.draw.rect(WIN,
                                 c.WHITE,
                                 pygame.Rect((x - 1, 0), (1, h)))
            for y in range(0, h, 32):
                pygame.draw.rect(WIN,
                                 c.WHITE,
                                 pygame.Rect((0, y - 1), (w, 1)))

    def drawWindow(self):
        WIN.fill(c.BLACK)
        self.drawRoads()
        for gridObj in self.grid:
            gridObj.draw(WIN)
        if self.displayGridLines:
            self.drawGridLines()
        pygame.display.update()

    def addGridObject(self, pos = (0, 0), color = c.BLUE, size = (1, 1)):
        obj = go.GridObject(pos, color, size)
        self.grid.append(obj)
        for i in range(1, size[0]):
            for j in range(1, size[1]):
                self.cache[(i, j)] = c.GRIDOBJ, obj

    def addVehicle(self, pos, color = c.GREEN):
        vehic = v.Vehicle(pos, color)
        self.grid.append(vehic)

    def addBuilding(self, pos, color = c.GREY):
        build = b.Building(pos, color)
        self.grid.append(build)
        self.cache[pos] = c.BUILDING, build
        self.buildings.append(build)

    def addParking(self, pos, orientation = 0, color = c.YELLOW):
        park = p.Parking(pos, orientation, color)
        self.grid.append(park)
        self.cache[pos] = c.PARKING, park
        self.spots.append(park)

    def addRoad(self, start, end, color = c.DARKGREY):
        road = r.Road(start, end, color)
        if road.vertical is None:
            print("Can't add a road which isn't aligned to an axis")
        else:
            if road.vertical:
                self.yAxisRoads.append(road)
                x = start[0]
                for y in range(start[1], end[1]):
                    self.cache[(x - 1, y)] = c.ROAD, road
                    self.cache[(x, y)] = c.ROAD, road
            else:
                self.xAxisRoads.append(road)
                y = start[1]
                for x in range(start[0], end[0]):
                    self.cache[(x, y - 1)] = c.ROAD, road
                    self.cache[(x, y)] = c.ROAD, road

    def addIntersection(self, pos, isNonintersection):
        intersect = i.Intersection(pos, isNonintersection)
        self.intersections.append(intersect)
        x, y = pos[0] // 32, pos[1] // 32
        self.cache[(x, y)] = c.INTERSECTION, intersect
        self.cache[(x - 1, y)] = c.INTERSECTION, intersect
        self.cache[(x, y - 1)] = c.INTERSECTION, intersect
        self.cache[(x - 1, y - 1)] = c.INTERSECTION, intersect        

    def initGrid(self):
        self.addRoad((1, 0), (1, 10))
        self.addRoad((5, 0), (5, 10))
        self.addRoad((9, 0), (9, 10))
        self.addRoad((0, 1), (10, 1))
        self.addRoad((0, 5), (10, 5))
        self.addRoad((0, 9), (10, 9))
        self.addBuilding((10, 0))
        self.addBuilding((9, 10))
        self.addBuilding((0, 10))
        self.addParking((2, 10))
        self.addParking((5, 10))
        self.addParking((6, 3))
        self.addParking((10, 2))
        self.addVehicle((0, 0), c.RED)
        self.addVehicle((6, 4), c.BLUE)
        self.addVehicle((7, 9), c.GREEN)

    def handleKeypress(self, key):
        if key == pygame.K_g:
            self.displayGridLines = not self.displayGridLines
        if key == pygame.K_EQUALS and self.tickInterval > 10:
            self.tickInterval -= 10
        if key == pygame.K_MINUS:
            self.tickInterval += 10
        if key == pygame.K_0:
            self.tickInterval = 60

    def step(self):
        vehicLocs = {}
        for gridObj in self.grid:
            if isinstance(gridObj, v.Vehicle):
                vehicLocs[gridObj.pos] = True
        for gridObj in self.grid:
            gridObj.step(self.cache, vehicLocs, self.buildings, self.spots)

    def main(self):
        clock = pygame.time.Clock()
        done = False
        frame = 0
        self.initGrid()
        self.findIntersections()
        while not done:
            frame += 1
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    newDims = event.size
                    self.createWindow(newDims)
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    self.handleKeypress(event.key)
            if frame % self.tickInterval == 0:
                self.step()
            self.drawWindow()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.main()
