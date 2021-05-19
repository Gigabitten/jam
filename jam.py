import pygame
import consts
import gridObject as go

WIN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Jam")
FPS = 60

class Game():
    def __init__(self):
        self.displayGridLines = True
        self.grid = []
        self.main()

    def create_window(self, newDims):
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

    def draw_window(self):
        WIN.fill(consts.BLACK)
        for gridObj in self.grid:
            gridObj.draw()
        if self.displayGridLines:
            self.drawGridLines()
        pygame.display.update()

    def initGrid(self):
        self.grid.append(go.GridObject(WIN, (1,10)))
        self.grid.append(go.GridObject(WIN, (5,8), consts.GREEN, (3,4)))

    def handleKeypress(self, key):
        if key == pygame.K_g:
            self.displayGridLines = not self.displayGridLines

    def main(self):
        clock = pygame.time.Clock()
        done = False
        self.initGrid()
        while not done:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    newDims = event.size
                    self.create_window(newDims)
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    self.handleKeypress(event.key)
            self.draw_window()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
