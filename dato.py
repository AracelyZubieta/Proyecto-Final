def validar_datos(edad, peso, talla):
   
    if edad <= 0 or peso <= 0 or talla <= 0:
        return False
    return True
