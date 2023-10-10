import pytest
from src.problem1 import analizar_lista

# Pruebas unitarias
@pytest.mark.parametrize("entrada, esperado", [
    ([], 0),                    # Lista vacía
    ([1, 2, 3], 1),             # Lista no vacía, todos positivos
    ([-1, -2, -3], 2),          # Lista no vacía, al menos un negativo
    ([0, -2, 8,4,6,9,1], 2),    # Lista no vacía, al menos un negativo
    ([1] * 101, 4),             # Lista no vacía, más de 100 elementos, todos positivos
    ([-1] * 101, 5),            # Lista no vacía, más de 100 elementos, al menos uno negativo
    ([0], 1),                   # Lista no vacía, todos positivos (incluyendo cero)
])
def test_analizar_lista(entrada, esperado):
    assert analizar_lista(entrada) == esperado

if __name__ == "__main__":
    pytest.main()