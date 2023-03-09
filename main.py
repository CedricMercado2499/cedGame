import pygame
import sys
from pygame.locals import *
from user_character import UserCharacter

# 3/08/23 - goal is to make a user-controlled object
# 3/09/23 - goal is to implement borders and gravity
# Colors     R    G    B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (3, 248, 252)


# Drawing
# pygame.draw.rect(screen, GREEN, (0, 250, 400, 100))


# Main Game Loop
def main():
    # Initiate PyGame
    pygame.init()
    # Window size
    display = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Ced Game')  # Window title
    clock = pygame.time.Clock()
    display.fill(WHITE)  # Screen color

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
        character.draw(display)
        pygame.display.update()


# Run
main()
