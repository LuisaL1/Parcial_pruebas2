def calcular_recarga(monto, premium):

    if monto < 1000:
        return {
            "valida": False
        }

    return {
        "valida": True
    }
def calcular_recarga(monto, premium):

    if monto < 1000 or monto > 50000:
        return {
            "valida": False
        }

    return {
        "valida": True
    }
