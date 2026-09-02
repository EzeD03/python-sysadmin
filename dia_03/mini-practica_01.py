def es_ip_valida(ip):
    partes = ip.split(".")
    if len(partes) == 4:
        for parte in partes:
            if not parte.isnumeric():
                return False
        return True
    else:
        return False

ip = input("Ingrese una dirección IP: ")
if es_ip_valida(ip):
    print("La dirección IP es válida.")
else:
    print("La dirección IP no es válida.")

print(es_ip_valida("192.168.1.a"))