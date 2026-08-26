# Día 1 - versión simulada del corazón del script.
# Todavía no lee datos reales de la VM (eso viene con os/subprocess en el Día 2-3).
# Por ahora, el diccionario "estado_servicios" reemplaza a los datos reales.

estado_servicios = {
    "nginx": "activo",
    "cron": "detenido",
    "ssh": "activo",
    "mysql": "activo"
}

for servicio, estado in estado_servicios.items():
    alerta = estado == "detenido"
    print(f"Servicio: {servicio} | Estado: {estado} | ¿Alerta?: {alerta}")