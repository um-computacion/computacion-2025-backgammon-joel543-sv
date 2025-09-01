# assets/piece_gen.py

import pygame
from pygame_ui.config import COLORS

def draw_pieces(surface, board_state):
    """
    board_state: lista de 24 elementos, cada uno es una tupla (cantidad, color)
    Ejemplo: [(3, "red"), (0, None), (2, "blue"), ...]
    """
    margin = 50
    point_width = 30
    point_height = 150
    spacing = 10
    radius = 12

    for i, (count, color) in enumerate(board_state):
        if count == 0 or color is None:
            continue

        x = margin + i * (point_width + spacing) + point_width // 2

        # Determinar si está en la mitad superior o inferior
        if i < 12:
            base_y = margin + point_height + 10
            direction = 1
        else:
            base_y = surface.get_height() - margin - point_height - 10
            direction = -1

        for j in range(count):
            y = base_y + direction * j * (radius * 2 + 2)
            pygame.draw.circle(surface, COLORS[color], (x, y), radius)
            pygame.draw.circle(surface, COLORS["border"], (x, y), radius, 2)
