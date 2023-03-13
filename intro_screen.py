# Intro Screen
import pygame
import time
import random


def intro():
    introS = True

    while introS:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys = pygame.key.get_pressed()
            from main import main
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                main()


        from main import BLACK, clock, display
        display.fill(BLACK)
        pygame.display.update()
        clock.tick(15)

