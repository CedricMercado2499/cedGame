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
        self.up = False
        self.down = False

        self.jump = True
        self.fall = False


    def move(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos[0] -= 0.7
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pos[0] += 0.7
            self.right = True
            self.left = False
            self.up = False
            self.down = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.up = True
            self.down = False
            self.left = False
            self.right = False
        if keys[pygame.K_SPACE] and self.jump:
            for i in range(100):
                self.pos[1] -= 0.5  # Jump height
            self.jump = False
            self.fall = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # self.pos[1] += 1 # Let gravity do the work
            self.down = True
            self.up = False
            self.left = False
            self.right = False

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
        if self.pos[1] < WINDOW_HEIGHT - self.height and self.fall:
            self.pos[1] += 0.4
        elif self.pos[1] == WINDOW_HEIGHT - self.height:
            self.jump = True
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


        # Draw Body
        pygame.draw.rect(display, self.color, (*self.pos, self.width, self.height))
        # Draw Head
        pygame.draw.rect(display, (100, 100, 100), (*headPos, self.width-10, self.height-10))

        if self.up or self.down or self.left or self.right:
            # Draw eyes
            pygame.draw.rect(display, (100, 100, 100), (*eyePos, self.width - 20, self.height - 20))
