# pygame_ui/event_handler.py

import pygame
from pygame_ui.utils import get_point_from_mouse
from core.dice import Dice

selected_point = None  # Punto de origen seleccionado por el jugador

def handle_events(game, dice):
    global selected_point
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        # Tirar dados con barra espaciadora
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice.roll()

        # Clic del mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked_point = get_point_from_mouse(mouse_pos)

            if clicked_point is not None:
                if selected_point is None:
                    selected_point = clicked_point
                else:
                    move = (selected_point, clicked_point)
                    success = game.make_move(game.current_player, move)
                    if not success:
                        print(f"❌ Movimiento inválido: {move}")
                    selected_point = None  # Reiniciar selección

    return True
