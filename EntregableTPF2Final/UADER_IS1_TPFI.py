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
    print("\n--- Obtener Datos Específicos ---")
    data_response = interface.get_data()
    print("Datos recuperados:", data_response)

    print("\n--- Obtener CUIT Específico ---")
    cuit_response = interface.get_cuit()
    print("CUIT recuperado:", cuit_response)

    print("\n--- Obtener y Actualizar ID de Secuencia ---")
    seq_id_response = interface.get_seq_id()
    print("ID de secuencia actualizado:", seq_id_response)


