# Integración Continua con CircleCI

Este proyecto utiliza **CircleCI** como herramienta de integración continua para garantizar la estabilidad del código y la calidad del desarrollo en cada etapa.

---

## ⚙️ ¿Qué hace CircleCI?

- Ejecuta pruebas unitarias automáticamente con cada **commit** o **pull request**.
- Verifica que el código siga funcionando correctamente antes de integrarlo.
- Genera reportes de cobertura y calidad en tiempo real.
- Permite detectar errores de forma temprana y mantener el proyecto confiable.

---

## 🧪 Pruebas automatizadas

Las pruebas se ejecutan con `pytest` y se mide la cobertura con `coverage`. El archivo de configuración (`.circleci/config.yml`) incluye los siguientes pasos:

1. Instalación de dependencias desde `requirements.txt`
2. Ejecución de tests con `pytest`
3. Generación de reporte de cobertura
4. (Opcional) Envío de métricas a [Coveralls.io](https://coveralls.io/) o [CodeClimate](https://codeclimate.com/)

---

## 📁 Archivos involucrados

- `.circleci/config.yml`: Configura el flujo de trabajo de CI.
- `requirements.txt`: Define las dependencias necesarias para testing.
- `tests/`: Contiene los archivos de prueba unitaria.
- `core/`: Contiene la lógica principal que se testea.

---

## 📊 Control de calidad

Se integran herramientas como:

- **Coveralls.io**: Para visualizar la cobertura de código en tiempo real.
- **CodeClimate**: Para analizar la calidad del código, detectar duplicaciones y complejidad innecesaria.

Los resultados se muestran como badges en el `README.md` del proyecto.

---

## ✅ Beneficios

- Asegura que el código esté siempre testeado antes de integrarse.
- Facilita el trabajo colaborativo y la revisión de cambios.
- Mejora la trazabilidad y la confianza en el desarrollo.

---

## 🔗 Recursos

- [CircleCI Docs](https://circleci.com/docs/)
- [Pytest](https://docs.pytest.org/)
- [Coverage.py](https://coverage.readthedocs.io/)
- [CodeClimate](https://codeclimate.com/)
- [Coveralls](https://coveralls.io/)
