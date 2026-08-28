disco_c = {"total_gb": 500, "usado_gb": 200, "libre_gb": 300}

if (disco_c["usado_gb"] / disco_c["total_gb"] * 100 ) > 80:
    print("Alerta: El disco C está casi lleno.")
else:
    print(f"El disco C tiene {disco_c['libre_gb']} GB de espacio libre.")