from core.game import Game
from cli.cli_game import CLIGame

def main():
    print("🎲 Bienvenido al Backgammon en modo línea de comandos 🎲")
    game = Game()
    cli_interface = CLIGame(game)
    cli_interface.run()

if __name__ == "__main__":
    main()
