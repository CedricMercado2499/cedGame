import pygame
import sys
from pygame.locals import *
from user_character import UserCharacter
import intro_screen
# Variables
WINDOW_WIDTH = 400  # 1000
WINDOW_HEIGHT = 300  # 800
clock = pygame.time.Clock()

# Window size
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
# Should I make separate file for colours?


# Drawing
# pygame.draw.rect(screen, GREEN, (0, 250, 400, 100))
# Background ^


def main():
    user_name = intro_screen.characterSelection()
    # Character Object
    character = UserCharacter([170, 270], user_name)
    # Will have to move this into a new screen called gameplay
    # Along with other code related to character

    font = pygame.font.Font(None, 15)
    selection_render = font.render(user_name, True, BLACK)
    selection_display = selection_render.get_rect(center=(selection_render.get_width(), selection_render.get_height()))


    while True:
        clock.tick(300)

        for event in pygame.event.get():  # Event handler
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        character.move()
        display.fill((255, 255, 255))
        # ^ clears the screen every move
        display.blit(selection_render, selection_display)

        character.draw(display)  # Draws character
        pygame.display.update()  # Updates screen


# Run

pygame.init()
pygame.display.set_caption('Hi')

# pygame.display.set_caption('The Adventures of Cedybedy')

intro_screen.introScreen()
intro_screen.startMenu()
main()
