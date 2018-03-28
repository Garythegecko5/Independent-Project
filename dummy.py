import os
import pygame
from pygame.locals import *
# Defining Colors
# ALL CAPS VARIABLES SHOULD BE CONSTANTS
# Tuples Can Not Be Modified
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (51, 195, 255)
FPS = 30
pygame.display.set_caption('Animation')
pygame.init()
pygame.display.set_caption('Test')
size = (700, 500)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

points = 0


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(SKY_BLUE)

    pygame.display.flip()

    clock.tick(60)
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
pygame.quit()



