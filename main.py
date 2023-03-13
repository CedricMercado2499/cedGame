import pygame
import sys
from pygame.locals import *
from user_character import UserCharacter
import intro_screen
# Variables
WINDOW_WIDTH = 400  # 1000
WINDOW_HEIGHT = 300  # 800
clock = pygame.time.Clock()
global display
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# making display global does not affect other modules
# I want to be able to access display on every module
# or find another way to display different visuals

# Colors     R    G    B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (3, 248, 252)


# Drawing
# pygame.draw.rect(screen, GREEN, (0, 250, 400, 100))
# Background ^


def main():
    # Initiate PyGame
    pygame.init()
    # Window size
    pygame.display.set_caption('The Adventures of Cedybedy')  # Window title
    display.fill(WHITE)  # Screen color

    # Character Object
    character = UserCharacter([170, 270])

    while True:
        clock.tick(300)
        events = pygame.event.get()
        for event in events:  # Event handler
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        character.move(events)

        display.fill((255, 255, 255))
        # ^ clears the screen every move
        # print(character.pos)  # Prints character coords
        character.draw(display)  # Draws character
        pygame.display.update()  # Updates


# Run

intro_screen.intro()
#main()
