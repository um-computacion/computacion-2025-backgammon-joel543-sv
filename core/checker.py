"""
    Representa una ficha de Backgammon, incluyendo su color y estado.

    Attributes:
        color (str): Color de la ficha ('X' o 'O').
        position (int | str): Posición actual de la ficha en el tablero (0–23, 'bar' o 'off').
    """


class Checker:
    def __init__(self, color, position=None):
        self.color = color  # "white" o "black"
        self.position = position  # 1–24 o "bar"
        self.on_bar = False
        self.home = False  # True si ya salió del tablero (victoria parcial)

    def move(self, steps, board):
        if self.on_bar:
            entry_point = self.get_entry_point()
            if board.can_place_checker(entry_point, self.color):
                self.position = entry_point
                self.on_bar = False
                board.place_checker(entry_point, self)
            else:
                print(f"No se puede reingresar desde la barra en {entry_point}")
        else:
            new_pos = self.position + steps if self.color == "white" else self.position - steps
            if 1 <= new_pos <= 24:
                if board.can_place_checker(new_pos, self.color):
                    board.remove_checker(self.position, self)
                    self.position = new_pos
                    board.place_checker(new_pos, self)
                else:
                    print(f"Movimiento inválido a {new_pos}")
            else:
                self.home = True  # Salió del tablero

    def capture(self):
        self.position = "bar"
        self.on_bar = True

    def get_entry_point(self):
        return 1 if self.color == "white" else 24

    def __str__(self):
        status = "Bar" if self.on_bar else f"P{self.position}"
        return f"{self.color.capitalize()} - {status}"
