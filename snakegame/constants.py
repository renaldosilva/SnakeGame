import os

import pygame

from snakegame import util


# Data directories
FONT_DIRECTORY = os.path.join('.', 'data', 'fonts')
FRUIT_IMAGE_DIRECTORY = os.path.join('.', 'data', 'images', 'fruits')
MENU_IMAGE_DIRECTORY = os.path.join('.', 'data', 'images', 'menu')
LOADING_IMAGE_DIRECTORY = os.path.join('.', 'data', 'images', 'loading')
MUSIC_DIRECTORY = os.path.join('.', 'data', 'sounds')
RECORD_DIRECTORY = os.path.join('.', 'data')


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
RECORD = os.path.join(RECORD_DIRECTORY, 'record.txt')


# Musics
INITIAL_VOLUME = 5
SOUNDS = {
    "click": os.path.join(MUSIC_DIRECTORY, 'click.wav'),
    "main_menu": os.path.join(MUSIC_DIRECTORY, 'main_menu.ogg'),
    "pause_menu": os.path.join(MUSIC_DIRECTORY, 'pause_menu.ogg'),
    "scroll": os.path.join(MUSIC_DIRECTORY, 'scrolling.wav'),
    "time_tick": os.path.join(MUSIC_DIRECTORY, "time_tick.ogg")
}


# Window
WINDOW_DIMENSION = SYSTEM_DISPLAY_HEIGHT * 0.7 // GAME_PIXEL_DIMENSION * GAME_PIXEL_DIMENSION
WINDOW_DIMENSIONS = (WINDOW_DIMENSION, WINDOW_DIMENSION)
WINDOW_ICON_IMAGE_PATH = os.path.join(FRUIT_IMAGE_DIRECTORY, 'apple.png')


# Events
ANIMATED_TEXT_EVENT = pygame.USEREVENT
ANIMATED_TEXT_MILLISECONDS = 50

ANIMATED_FONT_EVENT = pygame.USEREVENT + 1
ANIMATED_FONT_MILLISECONDS = 600

IMAGE_EVENT = pygame.USEREVENT + 2
IMAGE_MILLISECONDS = 800

TIMER_EVENT = pygame.USEREVENT + 3
TIMER_MILLISECONDS = 1000


# Text
TEXT_SIZE = GAME_PIXEL_DIMENSION * 3


# Button
BUTTON_SIZE = int(GAME_PIXEL_DIMENSION * 2.6)


# default alignments
TOP_ALIGNMENT = 1
CENTER_ALIGNMENT = 2
BOTTOM_ALIGNMENT = 3


# Main Menu
MAIN_MENU_TITLE = GAME_NAME
MAIN_MENU_IMAGES = [
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_1.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_2.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_3.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_4.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_5.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_6.png'),
    os.path.join(MENU_IMAGE_DIRECTORY, 'main', 'snake_menu_7.png')
]


# Loading
LOADING_TITLE = "LOADING..."
LOADING_SECONDS = 4
LOADING_IMAGE_LISTS = [
    [
        os.path.join(LOADING_IMAGE_DIRECTORY, 'list1', 'test_1.png')
    ],
    [
        os.path.join(LOADING_IMAGE_DIRECTORY, 'list2', 'test_2.png')
    ]
]


# Options Menu
OPTIONS_MENU_TITLE = "OPTIONS"
VOLUME_BAR_SIZE = GAME_PIXEL_DIMENSION * 3


# Record Menu
RECORD_MENU_TITLE = "RECORD"


# Credits Menu
CREDITS_MENU_TITLE = "CREDITS"
CREDITS = "> DEVELOPED AND ILLUSTRATED BY RENALDO SILVA <"
CREDITS_SIZE = GAME_PIXEL_DIMENSION


# Pause Menu
PAUSE_MENU_TITLE = "PAUSE"


# Confirmation Menu
CONFIRMATION_MENU_TITLE = "CONFIRM"
CONFIRMATION_MENU_DIMENSIONS = int(WINDOW_DIMENSION * 0.9), int(WINDOW_DIMENSION * 0.7)

# Timer
TIMER_SECONDS = 3
TIMER_SIZE = GAME_PIXEL_DIMENSION * 3
