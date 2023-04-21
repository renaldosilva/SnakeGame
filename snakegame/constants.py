import os

import pygame

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
FONTS = [
    os.path.join(FONT_DIRECTORY, 'Jump and Play.ttf'),
    os.path.join(FONT_DIRECTORY, 'Old Typewriter.ttf'),
    os.path.join(FONT_DIRECTORY, 'Type Keys Filled.ttf')
]


# Window
WINDOW_DIMENSION = SYSTEM_DISPLAY_HEIGHT * 0.7 // GAME_PIXEL_DIMENSION * GAME_PIXEL_DIMENSION
WINDOW_DIMENSIONS = (WINDOW_DIMENSION, WINDOW_DIMENSION)
WINDOW_ICON_IMAGE_PATH = os.path.join(FRUIT_IMAGE_DIRECTORY, 'fruit.png')


# Events
ANIMATED_TEXT_EVENT = pygame.USEREVENT + 0
ANIMATED_TEXT_MILLISECONDS = 50

ANIMATED_FONT_EVENT = pygame.USEREVENT + 1
ANIMATED_FONT_MILLISECONDS = 600

IMAGE_EVENT = pygame.USEREVENT + 2
IMAGE_MILLISECONDS = 600


# Text
TEXT_SIZE = GAME_PIXEL_DIMENSION * 3


# Button
BUTTON_SIZE = GAME_PIXEL_DIMENSION * 3


# Main Menu
MAIN_MENU_TITLE = GAME_NAME
MAIN_MENU_IMAGES = [
    os.path.join(FRUIT_IMAGE_DIRECTORY, 'snake_menu_1.png'),
    os.path.join(FRUIT_IMAGE_DIRECTORY, 'snake_menu_2.png')
]


# Options Menu
OPTIONS_MENU_TITLE = "OPTIONS"


# Volume bar
VOLUME_BAR_SIZE = GAME_PIXEL_DIMENSION * 3


# Credits Menu
CREDITS_MENU_TITLE = "CREDITS"
CREDITS = "> DEVELOPED AND ILLUSTRATED BY RENALDO SILVA <"
CREDITS_SIZE = GAME_PIXEL_DIMENSION
