# Character Selection Screen
import pygame
from colors import *
from start_screen import startMenu

# IMPORTANT
# **Going back to Character Selection from gameplay should hover the current character picked


# To Do: Make the interface look better
# Add more characters // make a separate file for characters

# Surface can create different shapes, while drawing rectangles only draw rectangles
# Surfaces are better?
# I want to make the buttons filled red, text is white (test)
# Surfaces are similar to screen size, but it can be any size, and you can have multiple surfaces


# Character Selection: With the interface, you can navigate with WASD within the character list
# Next steps: If player chooses the change character...
# from gameplay > open_options highlight used character

def characterSelection():
    from main import display

    font = pygame.font.SysFont("fresansbold.tff", 20)
    titleText = "Hi"
    title_text = font.render(titleText, True, WHITE)
    TITLE = title_text.get_rect(center=(display.get_width() / 2, 50))


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


                if not confirm_quit:
                    if selected == (ROW, COL):  # selects
                        pygame.draw.rect(display, GREEN, square)
                    else:
                        pygame.draw.rect(display, GRAY, square)
                else:
                    pygame.draw.rect(display, GRAY, square)

                pygame.draw.rect(display, BLACK, square, 1)
                display.blit(character_text, character_rect)

        if confirm_selection:

            play_text = font.render("PLAY", True, RED)
        else:
            play_text = font.render("PLAY", True, WHITE)
        if confirm_quit:  # Change
            back_text = font.render("BACK", True, RED)
        else:
            back_text = font.render("BACK", True, WHITE)

        play_button = play_text.get_rect(center=(display.get_width() - play_text.get_width(), play_text.get_height()))
        back_button = back_text.get_rect(center=(back_text.get_width(), back_text.get_height()))
        display.blit(play_text, play_button)
        display.blit(back_text, back_button)

    running = True

    selected = (0, 0)
    selection = characterList[0]
    back_selected = False
    confirm_selection = False
    confirm_quit = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if selection is not None:
                    if not confirm_selection and not confirm_quit:
                        if event.key == pygame.K_w:  # Up
                            if selected[0] > 0:
                                selected = (selected[0] - 1, selected[1])
                        if event.key == pygame.K_s:  # Down
                            if selected[0] < GRID_ROWS - 1:
                                selected = (selected[0] + 1, selected[1])
                        if event.key == pygame.K_a:  # Left
                            if selected[1] > 0:
                                selected = (selected[0], selected[1] - 1)
                        if event.key == pygame.K_d:  # Right
                            if selected[1] < GRID_COLS - 1:
                                selected = (selected[0], selected[1] + 1)

                    if event.key == pygame.K_ESCAPE:
                        if confirm_selection:  # Handles confirm_selection
                            confirm_selection = False

                        elif not confirm_quit:
                            confirm_quit = True
                        else:
                            confirm_quit = False

                    elif event.key == pygame.K_RETURN:
                        if not confirm_selection:   # Handles confirm_selection
                            confirm_selection = True
                        else:                   # Handles confirm_selection
                            return selection

                        if confirm_quit:
                            back_selected = True

                    selection = (characterList[selected[0] * 4 + selected[1]])

                else:
                    selected = (0, 0)
                    selection = characterList[0]

            if back_selected:
                selected = (0, 0)
                selection = characterList[0]
                if event.key == pygame.K_RETURN:
                    back_selected  = False
                    confirm_selection = False
                    if confirm_quit:  # Resets if either is selected
                        confirm_quit = False

                        startMenu()
                else:
                    pass





        # Drawing the screen
        display.fill(BLACK)
        draw_grid()
        display.blit(title_text, TITLE)
        pygame.display.flip()
