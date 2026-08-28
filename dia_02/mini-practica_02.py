tiempos_de_respuesta = [120, 450, 89, 900, 230]

for i, tiempo in enumerate(tiempos_de_respuesta):
    if tiempo > 400:
        print(f"{i + 1 } posición - Latencia alta: {tiempo}")
    else:
        print(f"{i + 1 } posición - Latencia normal: {tiempo}")
