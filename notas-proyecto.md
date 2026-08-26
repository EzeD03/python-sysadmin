# Notas del proyecto — Semana 7-8: Monitor de servicios/logs

## Qué quiero que el script responda
- ¿Qué servicios están corriendo en la VM y cuáles no?
- ¿Hubo errores en el log de autenticación (o el que elija) en la última hora?
- ¿Cuánto espacio libre queda en disco?

## Por qué esto sirve (en términos de soporte/sysadmin)
Un script así reemplaza una revisión manual repetitiva. En vez de entrar por SSH
y chequear servicio por servicio, el script hace el chequeo y avisa solo cuando
algo está mal — es el tipo de automatización que se espera de un rol de
soporte N2/SysAdmin trainee.

## Estado actual (Día 1)
Todavía no toca datos reales de la VM. Hoy solo se armó una versión simulada
con un diccionario de ejemplo, para probar la lógica antes de conectarla con
`os`/`subprocess` (eso arranca el Día 2-3).

## Dudas / pendientes
- ¿De qué manera puedo automatizar comandos para que hagan cuántas acciones necesarias sin que tenga que correr 70 comandos más?, ¿Algo que automatice mi labor al iniciar y quizás el de todo un día?.