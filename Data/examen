import json
import shutil
import sys
from utilidades import cargar_json, validar_config

def recalibrar_aprobacion():
    datos = cargar_json("config_evaluacion.json")
    if datos is None:
        return
    
    if "config" not in datos or "campers" not in datos:
        print("Falta config o campers en config_evaluacion.json.")
        return
    
    if not validar_config(datos["config"]):
        return
    
    config = datos["config"]
    campers = datos["campers"]
    
    shutil.copy("config_evaluacion.json", "config_evaluacion_backup.json")
    
    total_recalculados = 0
    total_aprobados = 0
    total_riesgo = 0
    
    for camper in campers:
        if "teoria" in camper and "practica" in camper and "asistencia" in camper:
            nota_final = (
                camper["teoria"] * config["w_teoria"] +
                camper["practica"] * config["w_practica"] +
                camper["asistencia"] * config["w_asistencia"]
            )
            camper["nota_final"] = nota_final
            
            if nota_final >= config["umbral"]:
                camper["estado"] = "Aprobado"
                total_aprobados += 1
            else:
                camper["estado"] = "Riesgo"
                total_riesgo += 1
            
            total_recalculados += 1
    
    try:
        archivo = open("config_evaluacion.json", 'w')
        json.dump(datos, archivo, indent=4)
        archivo.close()
    except:
        print("Error al guardar config_evaluacion.json")
        return
    
    print("Resumen:")
    print(f"Campers recalculados: {total_recalculados}")
    print(f"Campers aprobados: {total_aprobados}")
    print(f"Campers en riesgo: {total_riesgo}")

if len(sys.argv) > 1 and sys.argv[1] == "recalibrar_aprobacion":
    recalibrar_aprobacion()
else:
    print("Uso: python main.py recalibrar_aprobacion")