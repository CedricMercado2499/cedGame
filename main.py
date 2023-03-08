import pygame
import sys
from pygame.locals import *

# 3/08/23 - goal is to make a user-controlled object

# Colors     R    G    B
BLACK   =  (  0,   0,   0)
WHITE   =  (255, 255, 255)
RED     =  (255,   0,   0)
GREEN   =  (  0, 255,   0)
BLUE    =  (  0,   0, 255)
SKYBLUE =  (  3, 248, 252)

pygame.init()
screen = pygame.display.set_mode((400, 300))  # Window size
screen.fill(WHITE)  # Screen color
pygame.display.set_caption('Ced Game')  # Window title

# Drawing
pygame.draw.rect(screen, GREEN, (0, 250, 400, 100))

# Main Game Loop
while True:
    for event in pygame.event.get(): # Event handler
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
