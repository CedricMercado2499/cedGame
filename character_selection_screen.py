# Character Selection Screen
import pygame
from colors import *
from start_screen import startMenu


# To Do: Make the interface look better
# Add more characters // make a separate file for characters

# Surface can create different shapes, while drawing rectangles only draw rectangles
# Surfaces are better?
# I want to make the buttons filled red, text is white (test)
# Surfaces are similar to screen size, but it can be any size, and you can have multiple surfaces


def characterSelection():
    from main import display

    font = pygame.font.SysFont("fresansbold.tff", 20)
    play_text = font.render("PLAY", True, WHITE)
    back_text = font.render("BACK", True, WHITE)
    titleText = "Hi"
    title_text = font.render(titleText, True, WHITE)
    TITLE = title_text.get_rect(center=(display.get_width() / 2, 50))


    play_button = play_text.get_rect(center=(display.get_width() - play_text.get_width(), play_text.get_height()))
    back_button = back_text.get_rect(center=(back_text.get_width(), back_text.get_height()))

    # Griddy
    GRID_ROWS = 2  # Rows
    GRID_COLS = 4  # Columns
    GRID_SIZE = 50  # Shape of each square
    GRID_MARGIN = 10  # Space between each square
    grid = []

    characterList = ["Cedric", "Mohamed", "David", "Jacob", "Fernando", "Roberto", "Munashe", "Varun"]
    character_font = pygame.font.SysFont("fresansbold.tff", 12)

    for row in range(GRID_ROWS):
        grid_row = []
        for column in range(GRID_COLS):
            # Grid XY
            x = column * (GRID_SIZE + GRID_MARGIN) + GRID_MARGIN + 80
            y = row * (GRID_SIZE + GRID_MARGIN) + GRID_MARGIN + 100
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            grid_row.append(rect)
        grid.append(grid_row)

    def draw_grid():  # Draws the grid of characters
        for ROW in range(GRID_ROWS):
            for COL in range(GRID_COLS):
                square = grid[ROW][COL]
                character_text = character_font.render(characterList[ROW * GRID_COLS + COL], True, BLACK)
                character_rect = character_text.get_rect(center=square.center)

                if square.collidepoint(mouse_pos):
                    # If cursor is over a square... highlights
                    pygame.draw.rect(display, YELLOW, square)
                elif selected == (ROW, COL):  # selects
                    pygame.draw.rect(display, GREEN, square)
                else:
                    pygame.draw.rect(display, GRAY, square)

                pygame.draw.rect(display, BLACK, square, 1)
                display.blit(character_text, character_rect)



    running = True
    selected = None
    while running:
        mouse_pos = pygame.mouse.get_pos()  # Gets mouse position

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Click
                    for row in range(GRID_ROWS):
                        for col in range(GRID_COLS):
                            if grid[row][col].collidepoint(mouse_pos):
                                selected = (row, col)
                                selection = (characterList[row * GRID_COLS + col])

                                # print(selected)
                                # print(selection)

                    if play_button.collidepoint(event.pos):
                        if selected is not None:
                            return selection
                        else:
                            pass  # If no character is selected, don't show play button... something like that
                    if back_button.collidepoint(event.pos):  # Back button returns to start menu
                        startMenu()

                elif event.button == 3:  # Right click will unselect any selected character
                    # Is this even needed?
                    selected = None

                # Change button color when hovered
            if play_button.collidepoint(mouse_pos):
                play_text = font.render("PLAY", True, YELLOW)
            else:
                play_text = font.render("PLAY", True, WHITE)

            if back_button.collidepoint(mouse_pos):
                back_text = font.render("BACK", True, YELLOW)
            else:
                back_text = font.render("BACK", True, WHITE)

        # Drawing the screen
        display.fill(BLACK)
        draw_grid()
        display.blit(title_text, TITLE)
        display.blit(play_text, play_button)
        display.blit(back_text, back_button)
        pygame.display.flip()
