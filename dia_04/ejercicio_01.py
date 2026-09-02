try:
    with open("saludo.txt", "w") as archivo:
        archivo.write("¡Hola, mundo!")
        archivo.write("¡Hola, Cami!")
        archivo.write("¡Hola, Eze!")
except Exception as e:
    print(f"Ocurrió un error al escribir en el archivo: {e}")

try:
    with open("saludo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")