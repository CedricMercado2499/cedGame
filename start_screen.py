# Start Screen
import pygame
from colors import *

# To Do:
# Make options screen
# Make it so that when mouse.pos is on any button, the button is highlighted


def startMenu():
    # Either move this function to a separate module or rename this module
    from main import display, main

    # Fonts
    font = pygame.font.SysFont("fresansbold.tff", 20)
    titleFont = pygame.font.SysFont("fresansbold.tff", 38)

    # Render
    start_text = font.render("START", True, WHITE)
    options_text = font.render("OPTIONS", True, WHITE)
    quit_text = font.render("QUIT", True, WHITE)
    # titleText = "The Adventures of Cedybedy"
    titleText = "Hi"
    title_text = titleFont.render(titleText, True, WHITE)

    TITLE = title_text.get_rect(center=(display.get_width() / 2, 50))
    # Creates a space around the text that will act as a button
    start_button = start_text.get_rect(center=(display.get_width() / 2, 100))
    options_button = options_text.get_rect(center=(display.get_width() / 2, 150))
    quit_button = quit_text.get_rect(center=(display.get_width() / 2, 200))

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()  # Gets mouse position

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):  # If start_text is clicked, returns None (ends start_screen.py)
                    return None
                elif options_button.collidepoint(event.pos):  # NEED TO DO
                    pass
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()
                # Change button color when hovered
            if start_button.collidepoint(mouse_pos):
                start_text = font.render("START", True, RED)
            else:
                start_text = font.render("START", True, WHITE)

            if options_button.collidepoint(mouse_pos):
                options_text = font.render("OPTIONS", True, RED)
            else:
                options_text = font.render("OPTIONS", True, WHITE)

            if quit_button.collidepoint(mouse_pos):
                quit_text = font.render("QUIT", True, RED)
            else:
                quit_text = font.render("QUIT", True, WHITE)

        # Display screen and contents
        display.fill(BLACK)

        display.blit(title_text, TITLE)
        display.blit(start_text, start_button)
        display.blit(options_text, options_button)
        display.blit(quit_text, quit_button)

        pygame.display.update()
