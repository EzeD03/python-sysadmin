try:
    with open("log.txt", "a") as a:
        a.write("Se ha ejecutado el programa correctamente.\n")
        a.write("Se ha enviado un correo de notificación.\n")
        a.write("Se ha generado un informe de resultados.\n")
        a.write("Se ha realizado una copia de seguridad de los datos.\n")
        a.write("Se ha actualizado la base de datos con los nuevos registros.\n")
        a.write("Se ha cerrado la sesión del usuario de manera segura.\n")
        a.write("Se ha registrado un error en el sistema y se ha enviado una alerta al equipo de soporte.\n")
        a.write("Se ha completado la tarea programada y se ha enviado un correo de confirmación al usuario.\n")
        a.write("Se ha generado un informe de auditoría y se ha enviado al departamento de cumplimiento.\n")
        a.write("Se ha realizado una copia de seguridad de los archivos importantes y se ha almacenado en un lugar seguro.\n")
        a.write("Se ha actualizado el software del sistema y se ha reiniciado el servidor para aplicar los cambios.\n")
        a.write("Se ha registrado un intento de acceso no autorizado y se ha bloqueado la cuenta del usuario.\n")
        a.write("Se ha completado la migración de datos a la nueva plataforma y se ha verificado la integridad de los registros.\n")
        a.write("Se ha enviado un correo de seguimiento al cliente para confirmar la recepción del pedido.\n")
        a.write("Se ha generado un informe de rendimiento del sistema y se ha enviado al equipo de desarrollo para su análisis.\n")
        a.write("Se ha realizado una copia de seguridad de la base de datos y se ha almacenado en un servidor remoto para mayor seguridad.\n")
        a.write("Se ha actualizado la configuración del servidor y se ha reiniciado para aplicar los cambios.\n")
        a.write("Se ha registrado un error en la aplicación y se ha enviado un informe al equipo de desarrollo para su corrección.\n")
except Exception as e:
    print(f"Ocurrió un error al escribir en el archivo: {e}")

try:
    with open("log.txt", "r") as a:
        errores = ""
        for linea in a:
            if "error" in linea.lower():
                errores += linea
        print(f"Errores encontrados en el archivo:\n{errores}")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")