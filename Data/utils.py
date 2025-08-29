import json

def cargar_json(nombre_archivo):
    try:
        archivo = open(nombre_archivo, 'r')
        datos = json.load(archivo)
        archivo.close()
        return datos
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")
        return None
    except:
        print(f"Error al leer {nombre_archivo}.")
        return None

def validar_config(config):
    if "w_teoria" not in config or "w_practica" not in config or "w_asistencia" not in config or "umbral" not in config:
        print("Faltan campos en la configuración.")
        return False
    
    suma_pesos = config["w_teoria"] + config["w_practica"] + config["w_asistencia"]
    
    if abs(suma_pesos - 1.0) > 0.000001:
        print("Los pesos no suman 1.0.")
        return False
    
    return True