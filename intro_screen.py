# Intro Screen
import pygame
from colors import *

# Displaying Text:
# You need Font and Render (to create an object)
# Then you can display using display.blit(render, [coords])


def introScreen():
    from main import display

    # Intro text setup
    intro_font = pygame.font.SysFont("freesansbold.tff", 36)
    intro_text = "Hi"
    # intro_text = "The Adventures of Cedybedy"
    intro = intro_font.render(intro_text, True, WHITE)

    intro_time = 7000  # 7 Seconds
    intro_timer = pygame.time.get_ticks()  # Time in milliseconds

    # Skip text setup
    skip_font = pygame.font.SysFont("fresansbold.tff", 15)
    skip_text = "Press 'Esc' to skip"
    skip = skip_font.render(skip_text, True, (255, 255, 255))

    # bool variables
    skip_intro = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape skips the intro screen
                    skip_intro = True
        if (pygame.time.get_ticks() - intro_timer) > intro_time or skip_intro:  # After 7 seconds or 'esc' key is pressed
            running = False

        # Displaying the screen and contents
        display.fill(BLACK)
        display.blit(intro, ((display.get_width() // 2) - (intro.get_width() // 2), (display.get_height() // 2) - (intro.get_height() // 2)))
        display.blit(skip, (0, 0))

        pygame.display.update()


