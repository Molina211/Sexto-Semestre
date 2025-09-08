# =============================
# FASE 4: Estructura de decisión if else elif y match
# =============================
temp = float(input("Ingrese la temperatura: "))

if temp > 80:
	estado = 'CRÍTICO'
elif 60 <= temp <= 80:
	estado = 'SEGURO'
else:
	estado = 'BAJO'

print(f"Estado (if/elif/else): {estado}")

estado_expr = (
	'CRÍTICO' if temp > 80 else
	'SEGURO' if 60 <= temp <= 80 else
	'BAJO'
)
print(f"Estado (expresión condicional): {estado_expr}")

def menu_control():
	comando = input("\nIngrese comando (encender, apagar, reporte, config [clave]=[valor]): ")
	match comando.split():
		case ['encender']:
			print("Sistema encendido.")
		case ['apagar']:
			print("Sistema apagado.")
		case ['reporte']:
			# Simulación de estado
			voltaje = 12.5
			corriente = 1.2
			temperatura = 75
			print("Reporte de estado:")
			if voltaje > 13:
				print("Voltaje: ALTO")
			elif voltaje < 11:
				print("Voltaje: BAJO")
			else:
				print("Voltaje: NORMAL")
			if corriente > 2:
				print("Corriente: CRÍTICA")
			else:
				print("Corriente: SEGURA")
			if temperatura > 80:
				print("Temperatura: CRÍTICA")
			elif temperatura < 60:
				print("Temperatura: BAJA")
			else:
				print("Temperatura: SEGURA")
		case ['config', param]:
			match param.split('='):
				case [clave, valor]:
					if clave == 'umbral':
						try:
							valor = float(valor)
							print(f"Umbral configurado a {valor}")
						except ValueError:
							print("Valor de umbral inválido (debe ser float).")
					elif clave == 'nombre':
						print(f"Nombre configurado a {valor}")
					elif clave == 'maximo':
						try:
							valor = int(valor)
							print(f"Máximo configurado a {valor}")
						except ValueError:
							print("Valor de máximo inválido (debe ser int).")
					else:
						print("Clave desconocida.")
				case _:
					print("Formato de configuración inválido.")
		case _:
			print("Comando inválido.")

menu_control()

def validar_paquete(paquete):
	match paquete:
		case {'tipo': 'sensor', 'id': id, 'datos': datos} if isinstance(datos, list) and datos:
			promedio = sum(datos) / len(datos)
			alerta = None
			if promedio > 25:
				alerta = "Temperatura alta"
			elif promedio < 15:
				alerta = "Temperatura baja"
			else:
				alerta = "Temperatura normal"
			return {
				'id': id,
				'promedio': promedio,
				'alerta': alerta
			}
		case {'tipo': 'cmd', 'accion': accion, 'target': target} if isinstance(target, dict) and 'id' in target and 'eje' in target:
			return {
				'accion': accion,
				'target_id': target['id'],
				'eje': target['eje']
			}
		case {'tipo': 'cmd'}:
			return "Error: Falta información en el paquete 'cmd'"
		case {'tipo': 'alarma', **resto}:
			return "Paquete de alarma recibido"
		case _:
			return "Paquete inválido"

# Ejemplo de uso:
paquete1 = {'tipo': 'sensor', 'id': 7, 'datos': [22.4, 22.6, 22.3]}
paquete2 = {'tipo': 'cmd', 'accion': 'calibrar', 'target': {'id': 7, 'eje': 'x'}}
paquete3 = {'tipo': 'cmd', 'accion': 'reset'}
paquete4 = {'tipo': 'alarma', 'nivel': 'alto'}
paquete5 = {'tipo': 'desconocido'}

print(validar_paquete(paquete1))
print(validar_paquete(paquete2))
print(validar_paquete(paquete3))
print(validar_paquete(paquete4))
print(validar_paquete(paquete5))
