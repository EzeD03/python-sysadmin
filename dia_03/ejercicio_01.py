usuarios = [
    {"nombre": "jperez", "activo": True, "intentos_fallidos": 2},
    {"nombre": "mgomez", "activo": False, "intentos_fallidos": 5},
    {"nombre": "agarcia", "activo": True, "intentos_fallidos": 0},
    {"nombre": "lrodriguez", "activo": False, "intentos_fallidos": 3},
    {"nombre": "jlopez", "activo": True, "intentos_fallidos": 1},
    {"nombre": "sfernandez", "activo": False, "intentos_fallidos": 4},
    {"nombre": "mramirez", "activo": True, "intentos_fallidos": 0},
    {"nombre": "cjimenez", "activo": False, "intentos_fallidos": 2},
    {"nombre": "dtorres", "activo": True, "intentos_fallidos": 1}
]

def usuarios_a_revisar(usuarios):
    usuarios_revisados = []
    for usuario in usuarios:
        if usuario["activo"] and usuario["intentos_fallidos"] > 0:
            usuarios_revisados.append(usuario["nombre"])
    return usuarios_revisados

print(usuarios_a_revisar(usuarios))