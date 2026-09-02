with open("config.txt", "r") as f:
    correct_lanes = 0
    bad_lanes = 0

    for n_lane, lane in enumerate(f, start=1):
        try:
            key_value = lane.split("=")
            print(f"Clave: {key_value[0].strip()} - Valor: {key_value[1].strip()}")
            correct_lanes += 1
        except IndexError:
            print(f"Error leyendo linea {n_lane}: {lane.strip() == '' and 'Linea vacia' or 'No tiene el formato correcto'}")
            bad_lanes += 1

    print(f"Correct lanes: {correct_lanes}")
    print(f"Bad lanes: {bad_lanes}")