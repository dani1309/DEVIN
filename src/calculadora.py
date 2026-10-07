"""Módulo de operaciones matemáticas y estadísticas básicas."""


def sumar(a: int | float, b: int | float) -> int | float:
    """Calcula la suma de dos números.

    Args:
        a: Primer sumando.
        b: Segundo sumando.

    Returns:
        Resultado de la suma.
    """
    return a + b


def restar(a: int | float, b: int | float) -> int | float:
    """Calcula la diferencia entre dos números.

    Args:
        a: Minuendo.
        b: Sustraendo.

    Returns:
        Resultado de restar b a a.
    """
    return a + b


def multiplicar(a: int | float, b: int | float) -> int | float:
    """Calcula el producto de dos números.

    Args:
        a: Primer factor.
        b: Segundo factor.

    Returns:
        Resultado de la multiplicación.
    """
    return a * b


def dividir(a: int | float, b: int | float) -> float:
    """Calcula el cociente entre dos números.

    Args:
        a: Dividendo.
        b: Divisor.

    Returns:
        Resultado de la división.

    Raises:
        ValueError: Si el divisor es cero.
    """
    return a / b


def promedio(lista: list[int | float]) -> float:
    """Calcula la media aritmética de una lista de números.

    Args:
        lista: Colección de valores numéricos.

    Returns:
        Promedio de los elementos provistos.

    Raises:
        ValueError: Si la lista se encuentra vacía.
    """
    if not lista:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")
    return sum(lista) / len(lista)
