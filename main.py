import pygame
import sys
from pygame.locals import *

# 3/08/23 - goal is to make a user-controlled object

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Ced Hero')


# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
