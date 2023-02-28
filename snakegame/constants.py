import os

from snakegame import util


# Data directories
FONT_DIRECTORY = os.path.join('.', 'data', 'font')
FRUIT_IMAGE_DIRECTORY = os.path.join('.', 'data', 'images')


# Colors
GREEN_1 = (96, 138, 1)
GREEN_2 = (72, 105, 1)
LIGHT_GREEN_1 = (111, 161, 1)
LIGHT_GREEN_2 = (118, 245, 160)
DARK_GREEN = (22, 50, 0)


# System display dimensions
SYSTEM_DISPLAY_WIDTH, SYSTEM_DISPLAY_HEIGHT = util.get_system_display_dimensions()


# Game
GAME_NAME = "SNAKE GAME"
GAME_PIXEL_DIMENSION = SYSTEM_DISPLAY_HEIGHT // 100 * 2
GAME_FPS = 60
FONT = os.path.join(FONT_DIRECTORY, 'Jump and Play.ttf')


# Window
WINDOW_DIMENSION = SYSTEM_DISPLAY_HEIGHT * 0.7 // GAME_PIXEL_DIMENSION * GAME_PIXEL_DIMENSION
WINDOW_DIMENSIONS = (WINDOW_DIMENSION, WINDOW_DIMENSION)
WINDOW_ICON_IMAGE_PATH = os.path.join(FRUIT_IMAGE_DIRECTORY, 'fruit.png')
