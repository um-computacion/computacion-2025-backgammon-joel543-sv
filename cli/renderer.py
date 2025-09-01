# renderer.py

def render_board(board):
    print("\n🧩 Estado del tablero:")

    # Supongamos que board.points es una lista de 24 elementos
    # Cada punto es una lista de fichas, ej: ['white', 'white', 'black']
    top_row = board.points[:12]
    bottom_row = board.points[12:]

    def format_point(index, point):
        count_white = point.count('white')
        count_black = point.count('black')
        return f"{index+1:>2}:W{count_white}-B{count_black}"

    print("\n🔼 Parte superior (Puntos 1–12):")
    for i, point in enumerate(top_row):
        print(format_point(i, point), end=" | ")
    print("\n")

    print("🔽 Parte inferior (Puntos 13–24):")
    for i, point in enumerate(bottom_row, start=12):
        print(format_point(i, point), end=" | ")
    print("\n")

    # Mostrar barra
    print("📍 Barra:")
    print(f"White: {len(board.bar['white'])} fichas")
    print(f"Black: {len(board.bar['black'])} fichas")

    # Mostrar borne (fichas retiradas)
    print("🏁 Borne:")
    print(f"White: {len(board.borne_off['white'])} fichas")
    print(f"Black: {len(board.borne_off['black'])} fichas")
