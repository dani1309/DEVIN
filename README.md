# demo-devin

Repositorio de práctica diseñado para demostraciones académicas y pruebas de evaluación con agentes de inteligencia artificial para desarrollo de software.

## Estructura del proyecto

```text
demo-devin/
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── calculadora.py
├── tests/
│   ├── __init__.py
│   └── test_calculadora.py
└── .github/
    └── workflows/
        └── tests.yml
```

## Instalación

1. Crear un entorno virtual:
   ```bash
   python -m venv .venv
   ```

2. Activar el entorno virtual:
   - **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS:**
     ```bash
     source .venv/bin/activate
     ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de pruebas

Para ejecutar la suite de pruebas unitarias:

```bash
pytest
```

O en modo detallado:

```bash
pytest -v
```

## Estado actual

El repositorio contiene intencionalmente fallos en la implementación del código que provocan que la suite de pruebas no pase en su totalidad.

**Objetivo de la demostración:** Corregir el código fuente en `src/calculadora.py` para que todas las pruebas pasen satisfactoriamente, **sin alterar en ningún caso las aserciones ni el código de `tests/test_calculadora.py`**.