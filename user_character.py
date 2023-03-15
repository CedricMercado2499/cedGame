# User character
import pygame
from colors import *
from pygame.sprite import Sprite


# Concept: if user_name is something
# function call of that character
# Example: if user_name == "Cedric": give Cedric abilities/visual

# Create different surfaces for character (head/body/etc) yesno?
# Create more attributes for different characters (body types)

def open_options():  # Work-In-Progress, Options Menu isn't created, currently goes back to character selection
    from main import main
    main()


class Player(Sprite):

    def __init__(self, pos, user_name):
        super().__init__()  # 'super' -> just in case there's multiple characters in play

        self.pos = pos  # Position
        self.width = 30
        self.height = 30

        self.shirt_color = BLACK  # Don't need

        self.user_name = user_name

        match user_name:  # Basically a switch statement, way cleaner than multiple if-else statements
            case 'Mohamed':
                self.skin = SKIN_BLACK
                self.width = 40
                self.height = 50
            case 'Munashe':
                self.skin = SKIN_BLACK
                self.width = 40
                self.height = 45
            case 'Cedric':
                self.skin = SKIN_ASIAN
                self.width = 37
                self.height = 45
                # self.jump_height = -10
            case 'Roberto':
                self.skin = SKIN_ASIAN
                self.width = 35
                self.height = 35
            case 'Varun':
                self.skin = SKIN_BROWN
                self.width = 35
                self.height = 44
            case 'Fernando':
                self.skin = SKIN_ASIAN
                self.width = 40
                self.height = 40
            case 'David':
                self.skin = SKIN_WHITE
                self.width = 30
                self.height = 50
            case 'Jacob':
                self.skin = SKIN_WHITE
                self.width = 30
                self.height = 44
            case other:
                self.skin = GRAY
                self.width = 30
                self.height = 30

        # Character Movement Booleans
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.jumping = False
        self.falling = False

        # # Dash -> Work in progress
        # self.dashing = False
        # self.dash_timer = 0
        # self.dash_cd = 1000

        # Jumping
        self.jump_velocity = 0
        self.gravity = 0.5
        self.jump_cd = 500  # 0.5 seconds cooldown
        self.jump_timer = 0
        self.jump_height = -10


        # Player Model
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.skin)
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
        from main import WINDOW_HEIGHT
        # Gravity V2
        self.jump_velocity += self.gravity
        self.pos[1] += self.jump_velocity
        # jump_cd = 3000
        # jump_timer = pygame.time.get_ticks()
        if self.pos[1] + self.height > WINDOW_HEIGHT:
            self.pos[1] = WINDOW_HEIGHT - self.height
            self.jumping = True
            # if character is on the floor, jump
            # must change when applying platforms
        # Movement Functions

    def move_left(self, speed=0.7):
        self.pos[0] -= speed
        self.left, self.right, self.up, self.down = True, False, False, False

    def move_right(self, speed=0.7):
        self.pos[0] += speed
        self.left, self.right, self.up, self.down = False, True, False, False

    def look_up(self):
        self.left, self.right, self.up, self.down = False, False, True, False

    def look_down(self):
        self.left, self.right, self.up, self.down = False, False, False, True

    def do_jump(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.jump_timer >= self.jump_cd:
            self.jump_velocity = self.jump_height
            self.jumping = False
            self.jump_timer = current_time

    def draw(self, display):  # Drawing Player Model
        headPos = (self.rect.x + 5, self.rect.y - 20)
        eyePos = (self.rect.x, self.rect.y)

        if self.right:
            eyePos = (self.rect.x + 18, self.rect.y - 12.5)
        if self.left:
            eyePos = (self.rect.x + 2, self.rect.y - 12.5)
        if self.up:
            eyePos = (self.rect.x + 10, self.rect.y - 25)
        if self.down:
            eyePos = (self.rect.x + 10, self.rect.y)

        font = pygame.font.SysFont("fresansbold.tff", 15)
        character_text = font.render(self.user_name, True, BLACK)
        character_rect = character_text.get_rect(
            center=(self.rect.x + character_text.get_width() // 2.5, (self.rect.y - character_text.get_height() * 3)))

        shirtPos = (self.pos[0], self.pos[1] + (self.height / 3))
        # Draw Body
        pygame.draw.rect(display, self.skin, (*self.pos, self.width, self.height))
        pygame.draw.rect(display, self.shirt_color, (*shirtPos, self.width, self.height - (self.height / 3)))

        # # Draw Head
        # pygame.draw.rect(display, self.skin, (*headPos, self.width - 10, self.height - 10))
        # display.blit(character_text, character_rect)
        # if self.up or self.down or self.left or self.right:
        #     # Draw eyes
        #     pygame.draw.rect(display, self.skin, (*eyePos, self.width - 20, self.height - 25))

    # add a circle

    def update(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.update_position()
        self.apply_gravity()
