"""
    Controla el flujo principal del juego de Backgammon, incluyendo turnos,
    tiradas de dados, movimientos de fichas y condiciones de victoria.

    Attributes:
        board (Board): Instancia del tablero de juego.
        dice (Dice): Instancia de los dados.
        players (dict[str, Player]): Diccionario con los jugadores ('X' y 'O').
        current_player (str): Identificador del jugador que tiene el turno actual.
        winner (str | None): Identificador del jugador ganador, si ya hay uno.
    """


class Game:
    def __init__(self):
        self.board = Board()
        self.dice = Dice()
        self.players = {
            "white": Player("white"),
            "black": Player("black")
        }
        self.current_turn = "white"

    def start(self):
        print("¡Comienza el juego de Backgammon!")
        while not self.is_game_over():
            self.play_turn()
            self.switch_turn()

    def play_turn(self):
        player = self.players[self.current_turn]
        print(f"\nTurno de {player.color}")
        moves = self.dice.roll()
        print(self.dice)

        for move in moves:
            checker = player.select_checker(self.board)
            if checker:
                self.board.move_checker(checker, move)
            else:
                print("No hay fichas disponibles para mover con ese valor.")

    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def is_game_over(self):
        for color in ["white", "black"]:
            if self.board.all_checkers_home(color):
                print(f"\n¡Victoria para {color.upper()}!")
                return True
        return False
