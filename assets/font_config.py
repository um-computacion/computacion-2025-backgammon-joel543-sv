# pygame_ui/font_config.py

import pygame

pygame.font.init()

# Tamaños estándar
FONT_SIZES = {
    "title": 36,
    "subtitle": 28,
    "body": 20,
    "small": 16
}

# Fuentes por tipo
FONTS = {
    "title": pygame.font.SysFont("Arial", FONT_SIZES["title"], bold=True),
    "subtitle": pygame.font.SysFont("Arial", FONT_SIZES["subtitle"]),
    "body": pygame.font.SysFont("Arial", FONT_SIZES["body"]),
    "small": pygame.font.SysFont("Arial", FONT_SIZES["small"])
}
