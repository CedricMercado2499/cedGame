# Imports
import pygame

# Screen Imports
from intro_screen import introScreen as intro
from start_screen import startMenu as start
from gameplay import main as gameplay

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


pygame.init()  # Starts up Pygame

# General Setup
pygame.display.set_caption('Hi')
# pygame.display.set_caption('The Adventures of Cedybedy')


# Intro Screen > Start Screen > Character Selection > Map Selection > Gameplay
intro()
start()
gameplay(display)
