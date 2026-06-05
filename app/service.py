def calcular_bonificacion(monto):

    if monto >= 30000:
        return 25

    if monto >= 10000:
        return 10

    return 0


def calcular_recarga(monto, premium):

    if monto < 1000 or monto > 50000:
        return {
            "valida": False,
            "mensaje": "Monto invalido"
        }

    bonificacion = calcular_bonificacion(monto)

    if premium:
        bonificacion += 5

    return {
        "valida": True,
        "monto": monto,
        "bonificacion": bonificacion
    }