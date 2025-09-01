"""
    Representa a un jugador en el juego de Backgammon.

    Attributes:
        name (str): Identificador del jugador ('X' o 'O').
        checkers (list[Checker]): Lista de fichas pertenecientes al jugador.
        bar (list[Checker]): Fichas capturadas que están en la barra.
        borne_off (list[Checker]): Fichas que ya fueron retiradas del tablero.
    """


class Player:
    def __init__(self, color):
        self.color = color  # "white" o "black"
        self.checkers = [Checker(color) for _ in range(15)]
        self.bar = []    # Fichas capturadas
        self.home = []   # Fichas que ya salieron del tablero

    def has_checkers_on_bar(self):
        return len(self.bar) > 0

    def move_from_bar(self, board, dice_value):
        for checker in self.bar:
            entry_point = board.get_entry_point(self.color, dice_value)
            if board.can_place_checker(entry_point, self.color):
                board.place_checker(entry_point, checker)
                self.bar.remove(checker)
                print(f"{self.color} reingresa ficha desde la barra al punto {entry_point}")
                return True
        return False

    def select_checker(self, board, dice_value):
        # Selecciona una ficha que pueda moverse con ese valor
        for checker in self.checkers:
            if board.can_move_checker(checker, dice_value):
                return checker
        return None

    def move_checker(self, board, checker, dice_value):
        if checker in self.checkers:
            board.move_checker(checker, dice_value)
            if board.is_checker_home(checker):
                self.home.append(checker)
                self.checkers.remove(checker)
                print(f"{self.color} ha llevado una ficha a casa.")
        else:
            print("Ficha inválida para este jugador.")

    def has_won(self):
        return len(self.home) == 15
