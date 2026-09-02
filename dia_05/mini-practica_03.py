def dividir_seguro():

    print("Bienvenido al programa de división segura.")
    try:
        resultado = float(input("Ingrese el primer número: ")) / float(input("Ingrese el segundo número: "))
        return print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        return print("Error: No se puede dividir por cero.")
    except TypeError:
        return print("Error: Ambos argumentos deben ser números.")
    except ValueError:
        return print("Error: Debe ingresar un número válido.")
    finally:
        print("Fin de la función dividir_seguro.")

dividir_seguro()