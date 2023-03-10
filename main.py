import pygame
import sys
from pygame.locals import *
from user_character import UserCharacter

# Variables
WINDOW_WIDTH = 400  # 1000
WINDOW_HEIGHT = 300  # 800

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

# Main Game Loop
def main():
    # Initiate PyGame
    pygame.init()
    # Window size
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('The Adventures of Cedybedy')  # Window title
    clock = pygame.time.Clock()
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
main()
