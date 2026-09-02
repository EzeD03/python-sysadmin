try:
    with open("nombres.txt", "r") as a:
        nombres = []
        for linea in a:
            nombres.append(linea.strip())
        with open("nombres_ordenados.txt", "w") as b:
            for nombre in sorted(nombres):
                b.write(nombre + "\n")
except Exception as e:
    print(f"Ocurrió un error al procesar los archivos: {e}")