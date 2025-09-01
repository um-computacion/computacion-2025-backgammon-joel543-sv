# pygame_ui/utils.py

from pygame_ui.config import POINT_POSITIONS, PIECE_RADIUS

def get_point_from_mouse(mouse_pos):
    """Convierte la posición del mouse en el índice de punto del tablero."""
    mx, my = mouse_pos
    for i, (px, py) in enumerate(POINT_POSITIONS):
        dx = mx - px
        dy = my - py
        distance_squared = dx**2 + dy**2
        if distance_squared <= PIECE_RADIUS**2 * 4:  # tolerancia de clic
            return i + 1  # puntos van del 1 al 24
    return None

def distance(p1, p2):
    """Distancia euclidiana entre dos puntos."""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def center_text(text_surface, rect):
    """Centra un texto dentro de un rectángulo."""
    text_rect = text_surface.get_rect(center=rect.center)
    return text_rect

def color_for_player(color_name):
    """Devuelve el color RGB según el nombre del jugador."""
    from pygame_ui.config import COLORS
    return COLORS.get(color_name, (255, 255, 255))
