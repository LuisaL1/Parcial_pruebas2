
from app.service import calcular_recarga

def test_recarga_menor_a_1000():
    assert calcular_recarga(500, False)["valida"] == False

def test_recarga_mayor_a_50000():
    assert calcular_recarga(60000, False)["valida"] == False

def test_recarga_10000():

    resultado = calcular_recarga(10000, False)

    assert resultado["bonificacion"] == 10