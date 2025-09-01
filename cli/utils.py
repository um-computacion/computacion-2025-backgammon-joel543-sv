# utils.py

def is_valid_point(point):
    """Verifica si el punto está dentro del rango válido del tablero."""
    return point == -1 or (1 <= point <= 24)

def parse_point(value):
    """Convierte 'bar' en -1, y números en enteros."""
    value = value.strip().lower()
    if value == "bar":
        return -1
    try:
        point = int(value)
        if is_valid_point(point):
            return point
    except ValueError:
        pass
    return None

def get_direction(player_color):
    """Devuelve la dirección de movimiento según el color del jugador."""
    return 1 if player_color == "white" else -1

def format_move(move):
    """Formatea un movimiento para mostrarlo en consola."""
    origin, target = move
    origin_str = "bar" if origin == -1 else str(origin)
    return f"{origin_str}→{target}"
