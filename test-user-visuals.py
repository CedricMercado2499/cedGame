# File is completely isolated from the project (No other modules depend on this file)
# Trying to make better character visuals

# Imports
import pygame
import sys
from pygame.locals import *
from colors import *
from pygame.sprite import Sprite


# Note: Classes are used to create objects (I think)


class Player(Sprite):  # Player Block
    """
    Creates Player
    """
    # Player requirements: Visuals, movement

    def __init__(self, position):

        self.position = position  # Coordinates where player spawns

        # Size of character
        self.width = 30
        self.height = 30

        # Movement Booleans
        # Direction
        self.isRight = False
        self.isLeft = False
        self.isUp = False
        self.isDown = False
        # Actions
        self.isJumping = False
        self.isFalling = False

        # Character Attributes
        self.color = SKIN_WHITE

        # Creating character model
        self.character = pygame.Surface((self.width, self.height))  # Surface of character // Increase to add more shapes??? OR Insert your own photo
        self.character.fill(self.color)  # Color of character
        # Next steps: Character Rectangle with x & y, refer to user_character.py

        pass

    def draw_character(self):

        pass

    def move_character(self):

        pass

    def update_character(self):

        pass
    pass


class Screen:  # Screen Block
    """
    Creates Screen
    """

    def __init__(self, d_length, d_width, title):  # Width, Length, and Title
        self.d_length = d_length
        self.d_width = d_width
        self.title = title

    def startup(self):  # Creates the screen w/ title
        pygame.display.set_mode((self.d_length, self.d_width))
        pygame.display.set_caption(self.title)


# -------------------------------------------------------------------------------------------------------------------- #

# Running Block

clock = pygame.time.Clock()  # Clock variable // purpose unknown

# Created "Screen" objects
display = Screen(400, 300, "TESTING")
Screen.startup(display)

pygame.init()  # Pygame startup

while True:  # Constant loop // Game will run until QUIT
    clock.tick(250)  # I think this is the game speed, the higher, the faster

    USER = Player((200, 200))

    for event in pygame.event.get():  # Event handler
        if event.type == QUIT:  # "X" button top right of game window
            pygame.quit()  # Do I need 2 quits?
            quit()

    pygame.display.update()  # Updates screen
