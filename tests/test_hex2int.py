import pytest
from src.problem1 import hex2int

# Define la prueba unitaria y utiliza el decorador @pytest.mark.parametrize
@pytest.mark.parametrize("entrada, resultado", [("A", 10), ("5", 5), ("f", 15), ("G", -1), ("AB", -1), ("45",-1),])
def test_hex2int(entrada, resultado):
    assert hex2int(entrada) == resultado
