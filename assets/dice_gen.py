# assets/dice_gen.py

import pygame
from pygame_ui.config import COLORS

def draw_die(surface, x, y, value, size=50):
    pygame.draw.rect(surface, COLORS["white"], (x, y, size, size), border_radius=8)
    pygame.draw.rect(surface, COLORS["border"], (x, y, size, size), 2, border_radius=8)

    dot_radius = 5
    cx, cy = x + size // 2, y + size // 2

    # Posiciones relativas de los puntos
    offsets = {
        1: [(0, 0)],
        2: [(-15, -15), (15, 15)],
        3: [(-15, -15), (0, 0), (15, 15)],
        4: [(-15, -15), (-15, 15), (15, -15), (15, 15)],
        5: [(-15, -15), (-15, 15), (0, 0), (15, -15), (15, 15)],
        6: [(-15, -15), (-15, 0), (-15, 15), (15, -15), (15, 0), (15, 15)]
    }

    for dx, dy in offsets[value]:
        pygame.draw.circle(surface, COLORS["black"], (cx + dx, cy + dy), dot_radius)

def draw_dice(surface, dice_values, position=(600, 100), spacing=60):
    """
    dice_values: lista de valores [int, int]
    position: coordenadas (x, y) del primer dado
    """
    x, y = position
    for i, value in enumerate(dice_values):
        draw_die(surface, x + i * spacing, y, value)
