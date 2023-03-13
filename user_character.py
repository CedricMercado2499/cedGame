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

        self.left = False
        self.right = False
        self.jump = False


    def move(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos[0] -= 0.7
            self.left = True
            self.right = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pos[0] += 0.7
            self.right = True
            self.left = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.pos[1] -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.pos[1] += 1

        # idk if this is okay, but it works
        # Border
        from main import WINDOW_HEIGHT, WINDOW_WIDTH
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] + self.width > WINDOW_WIDTH:
            self.pos[0] = WINDOW_WIDTH - self.width
        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] + self.height > WINDOW_HEIGHT:
            self.pos[1] = WINDOW_HEIGHT - self.height

        # Gravity??
        if self.pos[1] < WINDOW_HEIGHT - self.height:
            self.pos[1] += 0.5

    # import main.py width
    def draw(self, display):
        headX = self.pos[0] + 5
        headY = self.pos[1] - 20
        headPos = (headX, headY)

        if self.right:
            eyeX = self.pos[0] + 20
        elif not self.right:
            eyeX = self.pos[0]

        eyeY = self.pos[1] - 15
        eyePos = (eyeX, eyeY)

        pygame.draw.rect(display, self.color, (*self.pos, self.width, self.height))
        pygame.draw.rect(display, (100, 100, 100), (*headPos, self.width-10, self.height-10))
        pygame.draw.rect(display, (100, 100, 100), (*eyePos, self.width-20, self.height-20))