# Examen
Logica y resultados:

Lee config_evaluacion.json con campos w_teoria, w_practica, w_asistencia, y umbral.
Valida que existan todos los campos y que los pesos sumen 1.0 (con tolerancia para errores de punto flotante).
Carga campers.json con datos de campers (teoria, practica, asistencia, nota_final, estado).
Crea respaldo de campers.json en campers_backup.json.
Para cada camper con notas completas:
Calcula nota_final = teoria * w_teoria + practica * w_practica + asistencia * w_asistencia.
Actualiza estado a "Aprobado" si nota_final >= umbral, o "Riesgo" si no (según reglas del ERP, asumidas como cambio a "Riesgo" si no aprueba).


Guarda cambios en campers.json.
Muestra resumen con cantidad de campers recalculados, aprobados y en riesgo.

Implementada lógica para recalcular notas finales usando pesos configurables y umbral dinámico desde config_evaluacion.json.

Actualiza estados en campers.json sin crear ni eliminar campers.

Genera respaldo campers_backup.json antes de modificar.

Valida suma de pesos y presencia de campos.

Ejecuta con python main.py recalibrar_aprobacion, mostrando resumen, por ejemplo:
Cantidad de campers recalculados: 2
Cuántos aprobaron: 1
Cuántos quedaron en riesgo: 1



