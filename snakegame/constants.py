import os

import pygame

from snakegame import util


# Data directories
FONT_DIRECTORY = os.path.join('.', 'data', 'fonts')
FRUIT_IMAGE_DIRECTORY = os.path.join('.', 'data', 'images', 'fruits')
MENU_IMAGE_DIRECTORY = os.path.join('.', 'data', 'images', 'menu')
MUSIC_DIRECTORY = os.path.join('.', 'data', 'sounds')


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


# Musics
INITIAL_VOLUME = 5
SOUNDS = {
    "click": os.path.join(MUSIC_DIRECTORY, 'click.wav'),
    "menu": os.path.join(MUSIC_DIRECTORY, 'menu.ogg'),
    "scroll": os.path.join(MUSIC_DIRECTORY, 'scrolling.wav')
}


# Window
WINDOW_DIMENSION = SYSTEM_DISPLAY_HEIGHT * 0.7 // GAME_PIXEL_DIMENSION * GAME_PIXEL_DIMENSION
WINDOW_DIMENSIONS = (WINDOW_DIMENSION, WINDOW_DIMENSION)
WINDOW_ICON_IMAGE_PATH = os.path.join(FRUIT_IMAGE_DIRECTORY, 'apple.png')


# Events
ANIMATED_TEXT_EVENT = pygame.USEREVENT + 0
ANIMATED_TEXT_MILLISECONDS = 50

ANIMATED_FONT_EVENT = pygame.USEREVENT + 1
ANIMATED_FONT_MILLISECONDS = 600

IMAGE_EVENT = pygame.USEREVENT + 2
IMAGE_MILLISECONDS = 800


# Text
TEXT_SIZE = GAME_PIXEL_DIMENSION * 3


# Button
BUTTON_SIZE = GAME_PIXEL_DIMENSION * 3


# Main Menu
MAIN_MENU_TITLE = GAME_NAME
MAIN_MENU_BUTTON_ALIGNMENT = 2
MAIN_MENU_IMAGES = [
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_1.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_2.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_3.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_4.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_5.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_6.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_7.png')
]


# Options Menu
OPTIONS_MENU_TITLE = "OPTIONS"
OPTIONS_MENU_BUTTON_ALIGNMENT = 3
VOLUME_BAR_SIZE = GAME_PIXEL_DIMENSION * 3


# Credits Menu
CREDITS_MENU_TITLE = "CREDITS"
CREDITS_MENU_BUTTON_ALIGNMENT = 3
CREDITS = "> DEVELOPED AND ILLUSTRATED BY RENALDO SILVA <"
CREDITS_SIZE = GAME_PIXEL_DIMENSION


# Difficulty Menu
EASY_MENU_TITLE = "EASY DIFFICULTY"
MEDIUM_MENU_TITLE = "MEDIUM DIFFICULTY"
HARD_MENU_TITLE = "HARD DIFFICULTY"
NEUTRAL_MENU_TITLE = "WILL GIVE UP?"
DIFFICULTY_MENU_BUTTON_ALIGNMENT = 3


# Pause Menu
PAUSE_MENU_TITLE = "PAUSE"
PAUSE_MENU_BUTTON_ALIGNMENT = 3
