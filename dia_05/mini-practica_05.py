def validar_puerto(puerto):
    if puerto < 1 or puerto > 65535:
        raise ValueError("El puerto debe estar entre 1 y 65535")
    return f"Puerto {puerto} es válido"

try:
    puerto = int(input("Ingrese un puerto: "))
    print(validar_puerto(puerto))
except ValueError as e:
    print(f"Error: {e}")
except TypeError:
    print("Error: El valor ingresado no es un número entero")