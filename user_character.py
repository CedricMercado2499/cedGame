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

def open_options():  # Work-In-Progress, Options Menu isn't created, currently goes back to character selection
    from main import main
    main()


class Player(Sprite):

    def __init__(self, pos, user_name):
        super().__init__()  # Just in case there's multiple players

        self.pos = pos  # Position
        self.width = 30
        self.height = 30
        self.color = BLACK

        self.user_name = user_name

        if user_name == "Mohamed" or user_name == "Munashe":
            self.skin = SKIN_BLACK
        elif user_name == "Cedric" or user_name == "Roberto" or user_name == "Fernando":
            self.skin = SKIN_ASIAN
        elif user_name == "Varun":
            self.skin = SKIN_BROWN
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

    # Keybind Movement
    def update_position(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move_left()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move_right()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.look_up()

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.look_down()

        if keys[pygame.K_SPACE]:
            self.do_jump()

        if keys[pygame.K_ESCAPE]:  # Change character
            open_options()

        # Barrier
        from main import WINDOW_HEIGHT, WINDOW_WIDTH
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] + self.width > WINDOW_WIDTH:
            self.pos[0] = WINDOW_WIDTH - self.width
        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] + self.height > WINDOW_HEIGHT:
            self.pos[1] = WINDOW_HEIGHT - self.height

    def apply_gravity(self):
        from main import WINDOW_HEIGHT, WINDOW_WIDTH
        # Gravity V2
        self.jump_velocity += self.gravity
        self.pos[1] += self.jump_velocity
        # jump_cd = 3000
        # jump_timer = pygame.time.get_ticks()
        if self.pos[1] + self.height > WINDOW_HEIGHT:
            self.pos[1] = WINDOW_HEIGHT - self.height
            # if pygame.time.get_ticks() - jump_timer > jump_cd:
            self.jumping = True
            # if character is on the floor, jump
            # must change when applying platforms
        # Movement Functions

    def move_left(self):
        self.pos[0] -= 0.7
        self.left, self.right, self.up, self.down = True, False, False, False

    def move_right(self):
        self.pos[0] += 0.7
        self.left, self.right, self.up, self.down = False, True, False, False

    def look_up(self):
        self.left, self.right, self.up, self.down = False, False, True, False

    def look_down(self):
        self.left, self.right, self.up, self.down = False, False, False, True

    def do_jump(self):
        if self.jumping:
            self.jump_velocity = -7  # Change this to inc/dec jump
            self.jumping = False

    def draw(self, display):
        headPos = (self.rect.x + 5, self.rect.y - 20)
        eyePos = (self.rect.x, self.rect.y)

        if self.right:
            eyePos = (self.rect.x + 20, self.rect.y - 15)
        if self.left:
            eyePos = (self.rect.x, self.rect.y - 15)
        if self.up:
            eyePos = (self.rect.x + 10, self.rect.y - 25)
        if self.down:
            eyePos = (self.rect.x + 10, self.rect.y - 5)

        font = pygame.font.SysFont("fresansbold.tff", 15)
        character_text = font.render(self.user_name, True, BLACK)
        character_rect = character_text.get_rect(
            center=(self.rect.x + character_text.get_width() // 2.5, (self.rect.y - character_text.get_height() * 3)))

        # Draw Body
        pygame.draw.rect(display, self.color, (*self.pos, self.width, self.height))
        # Draw Head
        pygame.draw.rect(display, self.skin, (*headPos, self.width - 10, self.height - 10))
        display.blit(character_text, character_rect)
        if self.up or self.down or self.left or self.right:
            # Draw eyes
            pygame.draw.rect(display, (100, 100, 100), (*eyePos, self.width - 20, self.height - 20))

    def update(self):
        self.update_position()
        self.apply_gravity()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
