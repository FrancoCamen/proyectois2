import json
from interface import Interface
import uuid

# Datos generados
if __name__ == "__main__":
    config_data = {
        "session_id": str(uuid.uuid4()),
        "cpu_id": str(uuid.getnode()),
        "sede_id": "UADER-FCyT-IS2",
    }

    # Guardar los datos en un archivo JSON
    with open("config.json", "w") as file:
        json.dump(config_data, file)

    # Cargar los datos JSON y pasarlos a Interface
    with open("config.json") as file:
        config_data = json.load(file)

    interface = Interface(config_data)

    # Ejecutar y mostrar los resultados de cada método
    print("\n--- Listar Datos Corporativos ---")
    data_list = interface.list_corporate_data()
    print("Listado de datos corporativos:", data_list)

    