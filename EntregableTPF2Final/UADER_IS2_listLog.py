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

    def display_corporate_logs(log_list):
        print("\n--- Listar Logs Corporativos ---")
        for i, log in enumerate(log_list, start=1):
            print(f"\nLog {i}:")
            print(f"  CPU ID      : {log.get('CPUid')}")
            print(f"  Session ID  : {log.get('sessionid')}")
            print(f"  Log ID      : {log.get('id')}")
            print(f"  Method      : {log.get('method')}")
            print(f"  Timestamp   : {log.get('timestamp')}")
        print("\n--- Fin del Listado ---\n")

    log_list = interface.list_corporate_log()
    display_corporate_logs(log_list)