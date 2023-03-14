# Intro Screen
import pygame
import colors


def introScreen():
    from main import display

    font = pygame.font.Font(None, 36)
    text = "Hi"
    # text = "The Adventures of Cedybedy"
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


def startMenu():
    # Either move this function to a separate module or rename this module
    from main import display, main
    BLACK = colors.BLACK
    WHITE = colors.WHITE

    font = pygame.font.Font(None, 20)
    titleFont = pygame.font.Font(None, 38)
    start_button = font.render("START", True, WHITE)
    options_button = font.render("OPTIONS", True, WHITE)
    quit_button = font.render("QUIT", True, WHITE)

    # titleText = "The Adventures of Cedybedy"
    titleText = "Hi"
    title = titleFont.render(titleText, True, WHITE)

    start_button_rect = start_button.get_rect(center=(display.get_width() / 2, 100))
    options_button_rect = options_button.get_rect(center=(display.get_width() / 2, 150))
    quit_button_rect = quit_button.get_rect(center=(display.get_width() / 2, 200))
    TITLE = title.get_rect(center=(display.get_width() / 2, 50))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    characterSelection()
                elif options_button_rect.collidepoint(event.pos):
                    print("OPTIONS")
                elif quit_button_rect.collidepoint(event.pos):
                    quit()
        display.fill(BLACK)

        display.blit(start_button, start_button_rect)
        display.blit(options_button, options_button_rect)
        display.blit(quit_button, quit_button_rect)
        display.blit(title, TITLE)
        pygame.display.update()


def characterSelection():  # Replicate StartMenu and add more buttons and such

    from main import display, main
    BLACK = colors.BLACK
    WHITE = colors.WHITE

    font = pygame.font.Font(None, 20)
    play_button = font.render("PLAY", True, WHITE)
    back_button = font.render("BACK", True, WHITE)


    play_button_rect = play_button.get_rect(center=(display.get_width() - play_button.get_width(), play_button.get_height()))
    back_button_rect = back_button.get_rect(center=(back_button.get_width(), back_button.get_height()))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    main()
                elif back_button_rect.collidepoint(event.pos):
                    startMenu()
        display.fill(BLACK)

        display.blit(play_button, play_button_rect)
        display.blit(back_button, back_button_rect)
        pygame.display.update()
