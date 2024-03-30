import pygame

from snakegame import constants, util
from snakegame.game.game import Game
from snakegame.game.basic_piece import BasicPiece
from snakegame.game.window_manager import WindowManager
from snakegame.menu.score_manager import ScoreManager
from snakegame.menu.sound_manager import SoundManager

pygame.init()

# Window
window = pygame.display.set_mode(constants.WINDOW_DIMENSIONS)
pygame.display.set_caption(constants.GAME_NAME)
icon = util.load_image(constants.WINDOW_ICON_IMAGE_PATH)
pygame.display.set_icon(icon)

# Managers
sound_manager = SoundManager()
score_manager = ScoreManager()
window_manager = WindowManager(window)

# Clock
clock = pygame.time.Clock()

# Basic game features
basic_piece = BasicPiece(window_manager, clock)

# Game
game = Game(basic_piece, sound_manager, score_manager)
