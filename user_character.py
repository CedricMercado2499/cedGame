# User character
import pygame
from colors import *
from pygame.sprite import Sprite


# Concept: if user_name is something
# function call of that character
# Example: if user_name == "Cedric": give Cedric abilities/visual

# Use Pygame.sprite
# Implement physics (velocity)
# Ways to organize code, separate blocks into functions

class Player(Sprite):

    def __init__(self, pos, user_name):
        super().__init__()  # Just in case there's multiple players

        self.pos = pos  # Position
        self.width = 30
        self.height = 30
        self.color = BLACK

        self.user_name = user_name

        if user_name == "Mohamed" or user_name == "Munashe":
            self.skin = BLACK
        else:
            self.skin = SKIN_WHITE

        # Character Movement Booleans
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.jumping = False
        self.falling = False

        # Jumping
        self.jump_velocity = 0
        self.gravity = 0.25

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos[0] -= 0.7
            self.left, self.right, self.up, self.down = True, False, False, False

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pos[0] += 0.7
            self.left, self.right, self.up, self.down = False, True, False, False

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.left, self.right, self.up, self.down = False, False, True, False

        if keys[pygame.K_SPACE]:
            if self.jumping:
                self.jump_velocity = -7  # Change this to inc/dec jump
                self.jumping = False

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.left, self.right, self.up, self.down = False, False, False, True

        if keys[pygame.K_ESCAPE]:  # Change character
            from main import main
            main()

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

        # Gravity V2
        self.jump_velocity += self.gravity
        self.pos[1] += self.jump_velocity
        if self.pos[1] + self.height > WINDOW_HEIGHT:
            self.pos[1] = WINDOW_HEIGHT - self.height
            self.jumping = True
            # if character is on the floor, jump
            # must change when applying platforms

    # import main.py width
    def draw(self, display):
        headX = self.pos[0] + 5
        headY = self.pos[1] - 20
        headPos = (headX, headY)

        eyeX = 0
        eyeY = 0

        if self.right:
            eyeX = self.pos[0] + 20
            eyeY = self.pos[1] - 15
        if self.left:
            eyeX = self.pos[0]
            eyeY = self.pos[1] - 15
        if self.up:
            eyeX = self.pos[0] + 10
            eyeY = self.pos[1] - 25
        if self.down:
            eyeX = self.pos[0] + 10
            eyeY = self.pos[1] - 5

        eyePos = (eyeX, eyeY)

        font = pygame.font.SysFont("fresansbold.tff", 15)
        character_text = font.render(self.user_name, True, BLACK)
        character_rect = character_text.get_rect(
            center=(self.pos[0] + character_text.get_width() // 2.5, (self.pos[1] - character_text.get_height() * 3)))

        # Draw Body
        pygame.draw.rect(display, self.color, (*self.pos, self.width, self.height))
        # Draw Head
        pygame.draw.rect(display, self.skin, (*headPos, self.width - 10, self.height - 10))
        display.blit(character_text, character_rect)
        if self.up or self.down or self.left or self.right:
            # Draw eyes
            pygame.draw.rect(display, (100, 100, 100), (*eyePos, self.width - 20, self.height - 20))

    def update(self):
        self.move()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]