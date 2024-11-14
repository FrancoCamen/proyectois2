import unittest
import logging
from logger.logger import Logger
from corporate_data import CorporateData
from corporate_log import CorporateLog
import json
from interface import Interface
import uuid
import traceback

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
    try:
        print("\n--- Se esta ejecuanto el metodo getData... ---")
        Logger.add_to_log("info", interface.get_data())
        print("\n--- Se registro la ejecucion dentro de un log (./logger/logs/app.log). ---")

        print("\n--- Se esta ejecuanto el metodo getCuit... ---")
        Logger.add_to_log("info", interface.get_cuit())
        print("\n--- Se registro la ejecucion dentro de un log (./logger/logs/app.log). ---")

        print("\n--- Se esta ejecuanto el metodo getSeqId... ---")
        Logger.add_to_log("info", interface.get_seq_id())
        print("\n--- Se registro la ejecucion dentro de un log (./logger/logs/app.log). ---")

        # Función para leer y mostrar el contenido del archivo de log
        def display_log_contents(file_path):
            try:
                print("\n--- Listado de logs generaods... ---")
                with open(file_path, "r") as log_file:
                    for line in log_file:
                        print(line.strip())  # Mostrar cada línea sin el salto de línea extra
            except FileNotFoundError:
                print(f"El archivo {file_path} no existe.")
            except Exception as e:
                print(f"Error al leer el archivo {file_path}: {e}")

        display_log_contents("./logger/logs/app.log")

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        print("\n--- Ocurrio un error en la ejecucion y fue capturado en un log (./logger/logs/app.log). ---")
    


