servicios = [
    {"nombre": "nginx", "puerto": 80, "estado": "activo"},
    {"nombre": "mysql", "puerto": 3306, "estado": "inactivo"},
    {"nombre": "redis", "puerto": 6379, "estado": "activo"},
    {"nombre": "postgres", "puerto": 5432, "estado": "activo"},
    {"nombre": "mongodb", "puerto": 27017, "estado": "activo"}
]

i = 0

for servicio in servicios:
    if servicio["estado"] == "activo":
        i += 1

print(f"Number of active services: {i}")