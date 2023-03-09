# User character
import pygame


class UserCharacter:
    def __init__(self, pos):
        self.pos = pos
        self.width = 30
        self.height = 30
        self.color = (0, 0, 0)
        self.dirX = 0
        self.dirY = 0

    def move(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos[0] -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pos[0] += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.pos[1] -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.pos[1] += 1


    def draw(self, display):
        pygame.draw.rect(display, self.color, (*self.pos, self.width, self.height))
