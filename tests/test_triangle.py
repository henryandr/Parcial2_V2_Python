import pytest
from src.problem1 import forman_triangulo

# Define la prueba unitaria y utiliza el decorador @pytest.mark.parametrize
@pytest.mark.parametrize("a, b, c, resultado", [(3, 4, 5, True), (5, 12, 13, True), (1, 2, 4, False), (7, 8, 15, False), (5, 5, 12, False)])
def test_forman_triangulo(a, b, c, resultado):
    assert forman_triangulo(a, b, c) == resultado
