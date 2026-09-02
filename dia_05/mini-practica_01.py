def pedir_entero():
    
    print("Bienvenido al programa de validación de números enteros.")

    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return print(f"El número {numero} es Entero.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

pedir_entero()