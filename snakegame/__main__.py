import pygame

from snakegame import constants, util
from snakegame.game.game import Game
from snakegame.game.basic_piece import BasicPiece


pygame.init()


# Load
icon = util.load_image(constants.WINDOW_ICON_IMAGE_PATH)

# Window
window = pygame.display.set_mode(constants.WINDOW_DIMENSIONS)
pygame.display.set_caption(constants.GAME_NAME)
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()

# Basic game features
basic_piece = BasicPiece(window, clock)

# Game
game = Game(basic_piece)
