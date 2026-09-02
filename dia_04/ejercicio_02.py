try:
    with open("../notas-proyecto.md", "r") as a:
        i = 0
        for linea in a:
            i += 1
        print(f"El archivo tiene {i} líneas.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
