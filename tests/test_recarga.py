def test_recarga_menor_a_1000():
    assert calcular_recarga(500, False)["valida"] == False