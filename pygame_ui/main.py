# pygame_ui/main.py

import pygame
from core.game import Game
from core.player import Player
from core.dice import Dice
from pygame_ui.renderer import render_game
from pygame_ui.event_handler import handle_events
from pygame_ui.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Backgammon - Pygame UI")
    clock = pygame.time.Clock()

    # Inicializar jugadores y juego
    player1 = Player("Jugador 1", color="white")
    player2 = Player("Jugador 2", color="black")
    game = Game(player1, player2)
    dice = Dice()

    running = True
    while running:
        screen.fill((30, 30, 30))  # Fondo oscuro

        # Capturar eventos
        running = handle_events(game, dice)

        # Dibujar estado actual
        render_game(screen, game, dice)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
