servidores = {"web01": "192.168.1.10", "db01": "192.168.1.20"}

def obtener_ip(nombre_servidor):

    print(f"Obteniendo la IP del servidor '{nombre_servidor}'...")

    try:
        return print(f"La IP del servidor '{nombre_servidor}' es: {servidores[nombre_servidor]}")
    except KeyError:
        return print(f"Error: El servidor '{nombre_servidor}' no existe en la lista de servidores.")
    finally:
        print("Fin de la función obtener_ip.")

obtener_ip(input("Ingrese el nombre del servidor: "))