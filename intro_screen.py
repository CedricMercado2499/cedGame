# Intro Screen
import pygame
import colors

def introScreen():
    from main import display

    font = pygame.font.Font(None, 36)
    text = "Hi"
    text_render = font.render(text, True, (255, 255, 255))
    text_width, text_height = font.size(text)
    text_x = (display.get_width() // 2) - (text_width // 2)
    text_y = (display.get_height() // 2) - (text_height // 2)

    fontSkip = pygame.font.Font(None, 15)
    textSkip = "Press 'Esc' to skip"
    text_renderSkip = fontSkip.render(textSkip, True, (255, 255, 255))

    intro_time = 7000  # 7 Seconds
    intro_timer = pygame.time.get_ticks()
    skip_intro = False

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    skip_intro = True
        if (pygame.time.get_ticks() - intro_timer) > intro_time or skip_intro:
            running = False


        display.fill(colors.BLACK)
        display.blit(text_render, (text_x, text_y))
        display.blit(text_renderSkip, (0, 0))
        pygame.display.flip()
