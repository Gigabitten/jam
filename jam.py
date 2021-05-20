import pygame
import consts
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
        self.stepNum = 0
        # ticks per frame
        self.tickInterval = 60
        self.xAxisRoads = []
        self.yAxisRoads = []
        self.intersections = []

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
            for x in range(0, w, consts.TILESIZE):
                pygame.draw.rect(WIN,
                                 consts.WHITE,
                                 pygame.Rect((x - 1, 0), (1, h)))
            for y in range(0, h, consts.TILESIZE):
                pygame.draw.rect(WIN,
                                 consts.WHITE,
                                 pygame.Rect((0, y - 1), (w, 1)))

    def drawWindow(self):
        WIN.fill(consts.BLACK)
        self.drawRoads()
        for gridObj in self.grid:
            gridObj.draw(WIN)
        if self.displayGridLines:
            self.drawGridLines()
        pygame.display.update()

    def addGridObject(self, pos = (0, 0), color = consts.BLUE, size = (1, 1)):
        self.grid.append(go.GridObject(pos, color, size))

    def addVehicle(self, pos, color = consts.GREEN):
        self.grid.append(v.Vehicle(pos, color))

    def addBuilding(self, pos, color = consts.GREY):
        self.grid.append(b.Building(pos, color))

    def addParking(self, pos, color = consts.YELLOW):
        self.grid.append(p.Parking(pos, color))

    def addRoad(self, start, end, color = consts.DARKGREY):
        road = r.Road(start, end, color)
        if road.vertical is None:
            print("Can't add a road which isn't aligned to an axis")
        else:
            if road.vertical:
                self.yAxisRoads.append(road)
            else:
                self.xAxisRoads.append(road)

    def addIntersection(self, pos, isNonintersection):
        self.intersections.append(i.Intersection(pos, isNonintersection))

    def initGrid(self):
        self.addRoad((0, 5), (10, 5))
        self.addRoad((5, 0), (5, 10))        

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
        for gridObj in self.grid:
            gridObj.step()

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
