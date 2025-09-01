# cli_game.py

from core.game import Game
from core.player import Player
from core.dice import Dice
from cli.renderer import render_board
from cli.input_handler import get_move_input

def main():
    print("🎲 Bienvenido al Backgammon CLI 🎲\n")

    # Inicializar jugadores
    player1 = Player("Jugador 1", color="white")
    player2 = Player("Jugador 2", color="black")

    # Inicializar juego
    game = Game(player1, player2)

    while not game.is_game_over():
        current_player = game.current_player
        print(f"\nTurno de {current_player.name}")

        # Tirar dados
        dice = Dice()
        dice.roll()
        print(f"Dados: {dice.values}")

        # Mostrar tablero
        render_board(game.board)

        # Obtener movimientos
        moves = get_move_input(current_player, dice.values, game.board)

        # Ejecutar movimientos
        for move in moves:
            success = game.make_move(current_player, move)
            if not success:
                print(f"Movimiento inválido: {move}")

        # Verificar victoria
        if game.has_won(current_player):
            print(f"\n🏆 {current_player.name} ha ganado el juego 🏆")
            break

        # Cambiar turno
        game.next_turn()

if __name__ == "__main__":
    main()
