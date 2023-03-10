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

# Window size
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800


# Drawing
# pygame.draw.rect(screen, GREEN, (0, 250, 400, 100))


# Main Game Loop
def main():
    # Initiate PyGame
    pygame.init()
    # Window size
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('The Epic Adventures of Cedybedy')  # Window title
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
        
        if character.pos[0] < 15:
            character.pos[0] = 15
        elif character.pos[0] + character.width > WINDOW_WIDTH:
            character.pos[0] = WINDOW_WIDTH - character.width
        if character.pos[1] < 15:
            character.pos[1] = 15
        elif character.pos[1] + character.height > WINDOW_HEIGHT:
            character.pos[1] = WINDOW_HEIGHT - character.height

        display.fill((255, 255, 255))
        # ^ clears the screen every move
        character.draw(display)
        pygame.display.update()


# Run
main()
