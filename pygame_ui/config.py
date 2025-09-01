# pygame_ui/config.py

# Dimensiones de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Posición del tablero en pantalla
BOARD_POS = (50, 50)

# Colores
COLORS = {
    "white": (240, 240, 240),
    "black": (30, 30, 30),
    "text": (255, 255, 255),
    "button": (70, 130, 180),
    "border": (200, 200, 200),
    "background": (20, 20, 20)
}

# Fuente
FONT_PATH = "assets/font.ttf"  # Asegurate de tener esta fuente en assets

# Posición de los dados
DICE_POS = (650, 200)

# Radio de las fichas
PIECE_RADIUS = 15

# Posiciones de los 24 puntos del tablero (simplificadas)
# Se pueden ajustar según el diseño del tablero
POINT_POSITIONS = [
    (60 + i * 40, 80) if i < 12 else (60 + (i - 12) * 40, 400)
    for i in range(24)
]
