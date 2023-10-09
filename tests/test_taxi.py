import pytest
from src.problem1 import calcular_tarifa

# Define la prueba unitaria y utiliza el decorador @pytest.mark.parametrize
@pytest.mark.parametrize("distancia_km, resultado", [(5.0, 12928.57), (3.5, 10250.0), (10.25, 22303.57), (0.0, 4000.0), (22.3, 43821.43)])
def test_calcular_tarifa(distancia_km, resultado):
    assert calcular_tarifa(distancia_km) == resultado
