# input_handler.py

def get_move_input(player, dice_values, board):
    print(f"\n{player.name}, ingresa tus movimientos (ej: 6→3).")
    print("Separá múltiples movimientos con comas si tenés tirada doble.")

    while True:
        raw_input = input("Movimientos: ").strip()
        moves = raw_input.split(",")

        parsed_moves = []
        valid = True

        for move in moves:
            move = move.strip()
            if "→" not in move:
                print(f"❌ Formato inválido: {move}")
                valid = False
                break

            origin, target = move.split("→")
            origin = origin.strip().lower()
            target = target.strip().lower()

            # Convertir 'bar' a -1, por ejemplo
            origin_point = -1 if origin == "bar" else int(origin)
            target_point = int(target)

            parsed_moves.append((origin_point, target_point))

        if valid:
            return parsed_moves
        else:
            print("🔁 Intentá de nuevo con el formato correcto.")
