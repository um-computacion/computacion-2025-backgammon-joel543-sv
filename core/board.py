"""
    Representa el tablero de Backgammon, incluyendo las posiciones de fichas,
    el manejo de movimientos y las reglas básicas del juego.

    Attributes:
        points (list[list[str]]): Lista de 24 puntos del tablero, cada uno con fichas.
        bar (dict[str, list[str]]): Fichas capturadas por cada jugador.
        borne_off (dict[str, list[str]]): Fichas retiradas del tablero por cada jugador.
    """


class Board:
    def __init__(self):
        # 24 puntos numerados del 1 al 24
        self.points = {i: [] for i in range(1, 25)}
        self.bar = {"white": [], "black": []}
        self.home = {"white": [], "black": []}
        self.setup_initial_positions()

    def setup_initial_positions(self):
        # Posiciones estándar de Backgammon (pueden ajustarse)
        self.points[1] = [Checker("black") for _ in range(2)]
        self.points[6] = [Checker("white") for _ in range(5)]
        self.points[8] = [Checker("white") for _ in range(3)]
        self.points[12] = [Checker("black") for _ in range(5)]
        self.points[13] = [Checker("white") for _ in range(5)]
        self.points[17] = [Checker("black") for _ in range(3)]
        self.points[19] = [Checker("black") for _ in range(5)]
        self.points[24] = [Checker("white") for _ in range(2)]

    def can_place_checker(self, point, color):
        checkers = self.points[point]
        return (
            len(checkers) == 0 or
            checkers[0].color == color or
            len(checkers) == 1  # permite captura
        )

    def place_checker(self, point, checker):
        checkers = self.points[point]
        if len(checkers) == 1 and checkers[0].color != checker.color:
            captured = self.points[point].pop()
            self.bar[captured.color].append(captured)
        self.points[point].append(checker)
        checker.position = point

    def remove_checker(self, point, checker):
        if checker in self.points[point]:
            self.points[point].remove(checker)

    def move_checker(self, checker, steps):
        if checker.on_bar:
            entry = checker.get_entry_point()
            if self.can_place_checker(entry, checker.color):
                self.place_checker(entry, checker)
                checker.on_bar = False
            else:
                print("No se puede reingresar desde la barra.")
        else:
            new_pos = checker.position + steps if checker.color == "white" else checker.position - steps
            if 1 <= new_pos <= 24:
                if self.can_place_checker(new_pos, checker.color):
                    self.remove_checker(checker.position, checker)
                    self.place_checker(new_pos, checker)
                else:
                    print("Movimiento inválido.")
            else:
                self.remove_checker(checker.position, checker)
                self.home[checker.color].append(checker)
                checker.home = True

    def all_checkers_home(self, color):
        return len(self.home[color]) == 15
