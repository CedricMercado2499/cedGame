# Intro Screen
import pygame
import time
import random


def intro():
    from main import main, BLACK, display

    introS = True

    while introS:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_ESCAPE]:
                pass
            # *if 'escape' is pressed, skip intro*

        display.fill(BLACK)

        # First time implementing an image
        image = pygame.image.load("images\\testimage.png").convert()
        display.blit(image, (0, 0))
        # displays image^
        pygame.time.set_timer(main(), 5000)
        # doesn't even go for 5 seconds, only 1 second
        # doesn't even display the testimage
        # comment out set_timer to show the image

        pygame.display.update()

        # I want it to be able to display intro for a few seconds
        # Then run main
