
from app.service import calcular_recarga

def test_recarga_menor_a_1000():
    assert calcular_recarga(500, False)["valida"] == False

def test_recarga_mayor_a_50000():
    assert calcular_recarga(60000, False)["valida"] == False

def test_recarga_10000():

    resultado = calcular_recarga(10000, False)

    assert resultado["bonificacion"] == 10
def test_recarga_30000():

    resultado = calcular_recarga(30000, False)

    assert resultado["bonificacion"] == 25

def test_usuario_premium():

    resultado = calcular_recarga(30000, True)

    assert resultado["bonificacion"] == 30