linea_simulada = "usuario=admin accion=login resultado=fallido"

linea_reformada= linea_simulada.split()

usuario = linea_reformada[0].split("=")

accion = linea_reformada[1].split("=")

resultado = linea_reformada[2].split("=")

print(f"Usuario: {usuario[1]} - Acción: {accion[1]} - Resultado: {resultado[1]}")