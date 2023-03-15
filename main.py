# Imports
import pygame
import sys
from pygame.locals import *
from colors import *

# Screen Imports
from intro_screen import introScreen as intro
from start_screen import startMenu as start
from character_selection_screen import characterSelection as character_selection
from user_character import Player

# Variables
WINDOW_WIDTH = 400  # 1000
WINDOW_HEIGHT = 300  # 800
clock = pygame.time.Clock()

# Window size
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# To Do:
# Include a menu tab, that's opened by ESCAPE
# Give the option to quit to menu, or change characters
# gotta use a boolean called is_menu = True

# Create a separate file and include main(), rename it to gameplay or something


def main():
    name = character_selection()  # Character selected is returned
    # Character Object
    # Will have to move this into a new screen called gameplay
    # Along with other code related to character

    player = Player(([100, 100]), name)


    # Setting up a name above the character
    # font = pygame.font.Font(None, 15)
    # selection_render = font.render(name, True, BLACK)

    while True:
        clock.tick(250)  # This is basically game speed, the higher, the faster * Might include in options

        for event in pygame.event.get():  # Event handler
            if event.type == QUIT:
                pygame.quit()
                quit()

        player.update()  # Updates the sprite (in my cup)

        display.fill(WHITE)  # Clears the screen after every move

        player.draw(display)  # Draws the character sprite (in my cup)

        pygame.display.update()  # Updates screen


# Main Loop

pygame.init()  # Starts up Pygame

# Window Title
pygame.display.set_caption('Hi')
# pygame.display.set_caption('The Adventures of Cedybedy')


# Intro Screen > Start Screen > Character Selection > main/gameplay
intro()
start()
main()
