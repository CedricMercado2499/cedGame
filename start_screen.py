# Start Screen
import pygame
from colors import *

# To Do:
# Make options screen


def startMenu():
    from main import display

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

    selected_button = 0
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    selected_button = (selected_button - 1) % 3
                elif event.key == pygame.K_s:
                    selected_button = (selected_button + 1) % 3
                elif event.key == pygame.K_RETURN:
                    if selected_button == 0:
                        return "character"
                    elif selected_button == 1:
                        # Options
                        pass
                    elif selected_button == 2:
                        pygame.quit()
                        quit()
            # Change button color when hovered
            if selected_button == 0:
                start_text = font.render("START", True, RED)
            else:
                start_text = font.render("START", True, WHITE)

            if selected_button == 1:
                options_text = font.render("OPTIONS", True, RED)
            else:
                options_text = font.render("OPTIONS", True, WHITE)

            if selected_button == 2:
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
