import pygame

from snakegame import constants
from snakegame.game.game import Game
from snakegame.game.basic_piece import BasicPiece


# Load
icon = pygame.image.load(constants.WINDOW_ICON_IMAGE_PATH)

# Window
pygame.display.set_caption(constants.GAME_NAME)
pygame.display.set_icon(icon)
canvas = pygame.display.set_mode(constants.WINDOW_DIMENSIONS)

# Clock
clock = pygame.time.Clock()

# Basic game features
basic_piece = BasicPiece(canvas, clock)

# Game
game = Game(basic_piece)




