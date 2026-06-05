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
def calcular_recarga(monto, premium):

    if monto < 1000 or monto > 50000:
        return {"valida": False}

    bonificacion = 0

    if monto >= 10000:
        bonificacion = 10

    return {
        "valida": True,
        "bonificacion": bonificacion
    }
def calcular_recarga(monto, premium):

    if monto < 1000 or monto > 50000:
        return {"valida": False}

    bonificacion = 0

    if monto >= 30000:
        bonificacion = 25

    elif monto >= 10000:
        bonificacion = 10

    return {
        "valida": True,
        "bonificacion": bonificacion
    }


