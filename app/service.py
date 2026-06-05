def calcular_recarga(monto, premium):

    if monto < 1000:
        return {
            "valida": False
        }

    return {
        "valida": True
    }
