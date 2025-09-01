# pygame_ui/renderer.py

import pygame
from pygame_ui.config import (
    BOARD_POS, POINT_POSITIONS, PIECE_RADIUS,
    COLORS, DICE_POS, FONT_PATH
)
import os

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "..", "assets")

def load_image(name):
    return pygame.image.load(os.path.join(ASSETS_PATH, name))

# Cargar imágenes
board_img = load_image("board.png")
white_piece_img = load_image("white_piece.png")
black_piece_img = load_image("black_piece.png")
dice_faces = [load_image(f"dice_faces/{i}.png") for i in range(1, 7)]
font = pygame.font.Font(os.path.join(ASSETS_PATH, "font.ttf"), 24)

def render_game(screen, game, dice):
    # Dibujar tablero
    screen.blit(board_img, BOARD_POS)

    # Dibujar puntos y fichas
    for i, point in enumerate(game.board.points):
        x, y = POINT_POSITIONS[i]
        offset = 0
        for color in point:
            piece_img = white_piece_img if color == "white" else black_piece_img
            screen.blit(piece_img, (x, y - offset))
            offset += PIECE_RADIUS * 2

    # Dibujar barra
    render_bar(screen, game.board.bar)

    # Dibujar borne
    render_borne(screen, game.board.borne_off)

    # Dibujar dados
    render_dice(screen, dice.values)

    # Dibujar turno
    render_turn(screen, game.current_player.name)

def render_bar(screen, bar):
    x, y = 600, 250
    for i, color in enumerate(["white", "black"]):
        count = len(bar[color])
        text = font.render(f"{color.capitalize()} en barra: {count}", True, COLORS[color])
        screen.blit(text, (x, y + i * 30))

def render_borne(screen, borne):
    x, y = 600, 350
    for i, color in enumerate(["white", "black"]):
        count = len(borne[color])
        text = font.render(f"{color.capitalize()} borne: {count}", True, COLORS[color])
        screen.blit(text, (x, y + i * 30))

def render_dice(screen, values):
    for i, val in enumerate(values):
        dice_img = dice_faces[val - 1]
        screen.blit(dice_img, (DICE_POS[0] + i * 60, DICE_POS[1]))

def render_turn(screen, player_name):
    text = font.render(f"Turno de: {player_name}", True, COLORS["text"])
    screen.blit(text, (20, 20))
