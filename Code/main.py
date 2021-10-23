import pygame
import sys

import Engine

pygame.init()

WIDTH = 448
HEIGHT = 448
DIMENSION = 7

SQ_SIZE = HEIGHT // DIMENSION

MAX_FPS = 15
IMAGES = {}


def load_images():  # loads images in images dic adn add their file path
    chips = ["Rc", "Yc"]
    for chip in chips:
        IMAGES[chip] = pygame.transform.scale(pygame.image.load('../Images/' + chip + '.png'), (SQ_SIZE, SQ_SIZE))


"""
main method controls graphic and determines user input
"""


def main():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("blue"))
    ge = Engine.Game()
    running = True

    load_images()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                location = pygame.mouse.get_pos()  # x y location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                move = [col, row]
                print(move)
                ge.open_rows()

                if move[0 - 1] in ge.available_cols:
                    ge.make_move(move)
                    ge.makes_chips_drop()
                    ge.check_for_win()
                else:
                    move = []

            elif event.type == pygame.KEYDOWN:  # resets the board in its original state
                if event.key == pygame.K_r:
                    ge.board = [
                        ["--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--"]
                    ]

        clock.tick(MAX_FPS)
        pygame.display.flip()
        draw_game_state(screen, ge)


def draw_game_state(screen, ge):
    draw_board(screen)
    draw_pieces(screen, ge.board)


"""
draws the board
"""


def draw_board(screen):
    x_cord = 32
    y_cord = 32
    for i in range(0, 42):
        pygame.draw.circle(screen, (255, 255, 255), [x_cord, y_cord], 30)
        x_cord += 64

        if x_cord > 448:  # switches row when end is reached
            x_cord = 32
            y_cord += 64


def draw_pieces(screen, board):
    for r in range(0, 6):
        for c in range(DIMENSION):
            chip = board[r][c]
            if chip != "--":
                screen.blit(IMAGES[chip], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
