# Intro Screen
import pygame


def introScreen():
    from main import display
    font = pygame.font.Font(None, 36)
    text = "Hi"
    text_render = font.render(text, True, (255, 255, 255))
    text_width, text_height = font.size(text)
    text_x = (display.get_width() // 2) - (text_width // 2)
    text_y = (display.get_height() // 2) - (text_height // 2)

    intro_time = 7000
    intro_timer = pygame.time.get_ticks()
    skip_intro = False

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    skip_intro = True
        if (pygame.time.get_ticks() - intro_timer) > intro_time or skip_intro:
            running = False

        display.fill((0, 0, 0))
        display.blit(text_render, (text_x, text_y))
        pygame.display.flip()
