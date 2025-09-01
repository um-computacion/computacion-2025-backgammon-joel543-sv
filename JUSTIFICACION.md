# JUSTIFICACION.md

## 🧩 Resumen del diseño general

Este proyecto implementa una versión simplificada del juego Backgammon utilizando programación orientada a objetos en Python. El diseño se basa en la separación de responsabilidades mediante clases específicas para cada componente del juego: tablero, fichas, dados, jugadores y lógica principal. Se priorizó la claridad, la modularidad y la posibilidad de realizar testing unitario sobre cada parte del sistema.

---

## 🧱 Justificación de las clases elegidas

- **Board**: Encapsula la lógica del tablero, incluyendo puntos, barra y borne-off. Permite validar y aplicar movimientos.
- **Checker**: Representa una ficha individual, con su color y posición. Facilita el seguimiento del estado de cada ficha.
- **Dice**: Simula las tiradas de dados y genera los movimientos disponibles. Separa la aleatoriedad del resto de la lógica.
- **Player**: Modela a cada jugador, incluyendo sus fichas, barra y zona de retiro. Permite verificar condiciones de victoria.
- **Game**: Coordina el flujo del juego, turnos, reglas y condiciones de finalización. Actúa como controlador principal.

Esta división permite cumplir con los principios de diseño SOLID y facilita el mantenimiento y la extensión del proyecto.

---

## 🧬 Justificación de atributos

- `Board.points`: Lista de listas que representa los 24 puntos del tablero. Permite acceder y modificar fichas por posición.
- `Dice.values`, `is_double`, `moves`: Capturan el estado de la tirada actual y los movimientos disponibles.
- `Player.checkers`, `bar`, `borne_off`: Permiten seguir el estado de cada ficha y aplicar reglas específicas.
- `Game.current_player`, `winner`: Controlan el flujo del juego y permiten verificar el estado final.

Cada atributo fue elegido para representar directamente una parte del estado del juego, evitando redundancias y facilitando el testing.

---

## 🧠 Decisiones de diseño relevantes

- Uso de **docstrings en estilo Google** para facilitar la documentación automática.
- Separación entre lógica de juego (`Game`) y lógica de presentación (no incluida en esta versión).
- Inclusión de `__init__.py` vacío para definir `core/` como paquete, con posibilidad de agregar interfaz pública.
- Registro de prompts utilizados con IA en archivos separados para garantizar trazabilidad y transparencia.

---

## ⚠️ Excepciones y manejo de errores

Se definieron y manejaron las siguientes situaciones:

- Movimiento inválido (`Board.is_valid_move`): retorna `False` sin modificar el estado.
- Uso de movimiento no disponible (`Dice.use_move`): retorna `False` y no altera la lista.
- Verificación de ganador (`Player.has_won`): evita errores al acceder a listas vacías.

No se definieron clases de excepción personalizadas, pero se dejó espacio para incluirlas si se extiende el proyecto.

---

## 🧪 Estrategias de testing y cobertura

Se implementaron pruebas unitarias para:

- `Board.move_checker`: Verifica que los movimientos válidos se apliquen correctamente.
- `Dice.roll` y `use_move`: Aseguran que la lógica de dobles y consumo de movimientos funcione.
- `Player.has_won`: Verifica la condición de victoria.
- `Game.switch_turn` y `apply_move`: Validan el flujo de turnos y la integración entre componentes.

Se busca alcanzar al menos un **90% de cobertura** en la lógica central (`core/`), priorizando funciones con ramificaciones lógicas.

---

## 🧭 Referencias a principios SOLID

- **S (Single Responsibility)**: Cada clase tiene una responsabilidad clara y única.
- **O (Open/Closed)**: Las clases están abiertas a extensión (por herencia o composición) sin modificar su código base.
- **L (Liskov Substitution)**: Las clases no violan expectativas al ser utilizadas como instancias de sus tipos.
- **I (Interface Segregation)**: No se imponen métodos innecesarios; cada clase expone solo lo necesario.
- **D (Dependency Inversion)**: Se favorece la interacción entre clases mediante atributos y métodos bien definidos, evitando acoplamientos rígidos.

---

## 📎 Anexos

### 📐 Diagrama UML de clases

(Insertar imagen o enlace al diagrama UML generado. Puede incluir clases, atributos, métodos y relaciones.)

---

## 📈 Evolución del diseño

Este archivo se actualiza periódicamente para reflejar decisiones tomadas durante el desarrollo. Cada cambio queda registrado en el historial de Git para garantizar trazabilidad.

