import pytest
from src.calculadora import dividir, multiplicar, promedio, restar, sumar


# --- Pruebas de sumar ---
def test_sumar_enteros_positivos():
    assert sumar(10, 5) == 15


def test_sumar_negativos_y_decimales():
    assert sumar(-4, -6) == -10
    assert pytest.approx(sumar(1.5, 2.3)) == 3.8


# --- Pruebas de restar ---
def test_restar_enteros_positivos():
    assert restar(5, 3) == 2


def test_restar_negativos_y_decimales():
    assert restar(-2, -5) == 3
    assert pytest.approx(restar(10.5, 2.5)) == 8.0


# --- Pruebas de multiplicar ---
def test_multiplicar_positivos():
    assert multiplicar(4, 5) == 20


def test_multiplicar_negativos_y_cero():
    assert multiplicar(-3, 6) == -18
    assert multiplicar(10, 0) == 0
    assert pytest.approx(multiplicar(2.5, 2.0)) == 5.0


# --- Pruebas de dividir ---
def test_dividir_casos_validos():
    assert dividir(10, 2) == 5.0
    assert pytest.approx(dividir(7, 2)) == 3.5
    assert dividir(-15, 3) == -5.0


def test_dividir_por_cero():
    with pytest.raises(ValueError, match="No es posible dividir por cero"):
        dividir(5, 0)


# --- Pruebas de promedio ---
def test_promedio_casos_validos():
    assert promedio([1, 2, 3, 4, 5]) == 3.0
    assert pytest.approx(promedio([-2.0, 2.0, 6.0])) == 2.0


def test_promedio_lista_vacia():
    with pytest.raises(
        ValueError, match="No se puede calcular el promedio de una lista vacía."
    ):
        promedio([])
