#import pygame 
from game import *

pygame.init()

pygame.display.set_caption('Hex Wars')
clock = pygame.time.Clock()
fps = 60

gameDisp = pygame.display.set_mode((1024, 768), pygame.HWSURFACE|pygame.DOUBLEBUF)

def quitfunc():
    pygame.quit()
    quit()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitfunc()

    update()
    draw(gameDisp)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()