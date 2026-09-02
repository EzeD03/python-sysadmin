def resumen_disco(porcentaje_uso):
    if porcentaje_uso > 90:
        return "CRITICO"
    
    if porcentaje_uso > 70:
        return "ADVERTENCIA"

    return "OK"

porcentaje_uso = float(input("Ingrese el porcentaje de uso del disco: "))
estado = resumen_disco(porcentaje_uso)
print(f"El estado del disco es: {estado}")