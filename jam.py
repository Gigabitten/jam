import pygame

WIN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Jam")

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREY = 127, 127, 127

FPS = 60

def create_window(newDims):
    WIN = pygame.display.set_mode(newDims, pygame.RESIZABLE)
    pygame.display.set_caption("Jam")
    print(WIN.get_size())

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    done = False
    while not done:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                newDims = event.size
                create_window(newDims)
            if event.type == pygame.QUIT:
                done = True
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()
        
