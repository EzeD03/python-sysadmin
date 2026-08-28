logs = [
    "10:00 INFO sistema iniciado",
    "10:05 ERROR no se pudo conectar a la base de datos",
    "10:10 INFO usuario autenticado",
    "10:15 WARNING memoria baja",
    "10:20 INFO proceso completado",
    "10:25 ERROR fallo en la carga de datos",
    "10:30 INFO sistema detenido",
    "10:35 ERROR error desconocido",
    "10:40 INFO reinicio del sistema"
]

errores = 0

for log in logs:
    if log.split()[1] == "ERROR":
        errores += 1

print(f"Cantidad de errores: {errores}")

if errores > 1:
    i = 3
    while i > 1:
        print("Reconectando...")
        i -= 1