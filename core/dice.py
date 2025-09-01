"""
    Representa los dados utilizados en Backgammon, incluyendo la lógica de tiradas
    y generación de movimientos disponibles.

    Attributes:
        values (list[int]): Valores actuales de los dados (1 a 6).
        is_double (bool): Indica si la tirada fue doble (ambos dados iguales).
        moves (list[int]): Lista de movimientos disponibles para el turno actual.
    """


import random

class Dice:
    def __init__(self):
        self.values = []
        self.is_double = False
        self.moves = []

    def roll(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self.values = [die1, die2]
        self.is_double = die1 == die2

        if self.is_double:
            # Tirada doble: se repite el valor cuatro veces
            self.moves = [die1] * 4
        else:
            # Tirada normal: dos movimientos posibles
            self.moves = [die1, die2]

        return self.moves

    def use_move(self, value):
        if value in self.moves:
            self.moves.remove(value)
            return True
        return False

    def has_moves_left(self):
        return len(self.moves) > 0

    def reset(self):
        self.values = []
        self.is_double = False
        self.moves = []

    def __str__(self):
        tipo = "doble" if self.is_double else "normal"
        return f"Tirada: {self.values} | Movimientos disponibles: {self.moves} ({tipo})"
