# Calculadora de uso de recursos

memoria_usada = float(input("Cuanta memoria en MB está usando. "))
memoria_total = float(input("Cuanta memoria en MB tienes disponible. "))

print(((memoria_usada * 100) / memoria_total >= 90 and "Revisar sistema") or "Sistema en buenas condiciones")
