# Changelog

Todas las modificaciones importantes en este proyecto se documentan aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/), y este proyecto utiliza [versionado semántico](https://semver.org/lang/es/).

---

## [1.0.0] - 2025-08-31
### Añadido
- Lógica completa del juego en `core/`: tablero, dados, jugadores, reglas.
- Pruebas unitarias con cobertura superior al 90%.
- Interfaz por consola (`cli`) funcional.
- Interfaz gráfica básica con `pygame`.
- Archivo `requirements.txt` con dependencias externas.
- Documentación inicial: `README.md`, `CHANGELOG.md`, docstrings en módulos principales.

### Cambiado
- Refactor en `Board.move_checker` para simplificar condiciones de movimiento y captura.
- Separación de responsabilidades entre `Game`, `Player` y `Board` siguiendo principios SOLID.

### Corregido
- Error en `Dice.use_move` que no eliminaba correctamente valores repetidos.
- Ajuste en `Player.move_checker` para evitar duplicación de fichas en `home`.

---

## [0.1.0] - 2025-08-15
### Añadido
- Estructura inicial del proyecto con carpetas `core/`, `tests/`, `cli/`.
- Implementación básica de `Board`, `Checker`, `Dice` y `Player`.
- Primeros tests unitarios para `Dice` y `Board`.
