# Gameplay Screen

import pygame
from pygame.locals import *
from colors import *
from character_selection_screen import characterSelection as character_selection
from user_character import Player

# After character selection > *map selection*
# Displays the controllable character and map background

clock = pygame.time.Clock()


def main(display):
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