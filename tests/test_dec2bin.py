import pytest
from src.problem1 import decimal2binary

# Define la prueba unitaria y utiliza el decorador @pytest.mark.parametrize
@pytest.mark.parametrize("integer, resultado", [(10, "1010"), (7, "111"), (15, "1111"), (0, "0"), (23, "10111"), (14580, "11100011110100")])
def test_decimal2binary(integer, resultado):
    assert decimal2binary(integer) == resultado
