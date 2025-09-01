# assets/board_gen.py

import pygame
from pygame_ui.config import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS

def draw_board(surface):
    surface.fill(COLORS["background"])

    # Dimensiones del tablero
    margin = 50
    point_width = 30
    point_height = 150
    spacing = 10

    # Dibujar 12 triángulos arriba y 12 abajo
    for i in range(12):
        x = margin + i * (point_width + spacing)
        
        # Triángulos superiores
        top_triangle = [
            (x, margin),
            (x + point_width, margin),
            (x + point_width // 2, margin + point_height)
        ]
        pygame.draw.polygon(surface, COLORS["white"] if i % 2 == 0 else COLORS["black"], top_triangle)

        # Triángulos inferiores
        bottom_triangle = [
            (x, SCREEN_HEIGHT - margin),
            (x + point_width, SCREEN_HEIGHT - margin),
            (x + point_width // 2, SCREEN_HEIGHT - margin - point_height)
        ]
        pygame.draw.polygon(surface, COLORS["black"] if i % 2 == 0 else COLORS["white"], bottom_triangle)

    # Línea divisoria central
    pygame.draw.rect(surface, COLORS["border"], (SCREEN_WIDTH // 2 - 5, margin, 10, SCREEN_HEIGHT - 2 * margin))
