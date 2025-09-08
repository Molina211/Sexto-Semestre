# =============================
# FASE 6: Funciones
# =============================
def calcular_area_rectangulo(ancho, alto):
	return ancho * alto

ancho = float(input("Introduce el ancho del rectángulo: "))
alto = float(input("Introduce el alto del rectángulo: "))
print(f"El área del rectángulo es: {calcular_area_rectangulo(ancho, alto)}")

def analizar_lista(lista):
	promedio = sum(lista) / len(lista) if lista else 0
	mayor = max(lista) if lista else None
	menor = min(lista) if lista else None
	cantidad = len(lista)
	return promedio, mayor, menor, cantidad

entrada = input("Introduce una lista de números separados por coma: ")
numeros = [float(x) for x in entrada.split(",") if x.strip()]
promedio, mayor, menor, cantidad = analizar_lista(numeros)
print(f"Promedio: {promedio}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Cantidad: {cantidad}")

usuarios = {}
siguiente_id = 1

def registrar_usuario(nombre, edad, ciudad):
	global siguiente_id
	usuarios[siguiente_id] = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
	print(f"Usuario registrado con ID: {siguiente_id}")
	siguiente_id += 1

def mostrar_usuarios():
	if not usuarios:
		print("No hay usuarios registrados.")
	else:
		for uid, datos in usuarios.items():
			print(f"ID: {uid} - Nombre: {datos['nombre']}, Edad: {datos['edad']}, Ciudad: {datos['ciudad']}")

def buscar_usuario(uid):
	return usuarios.get(uid, "Usuario no encontrado.")

def eliminar_usuario(uid):
	if uid in usuarios:
		del usuarios[uid]
		print("Usuario eliminado.")
	else:
		print("Usuario no encontrado.")

while True:
	print("\n--- Menú de usuarios ---")
	print("1. Registrar usuario")
	print("2. Mostrar usuarios")
	print("3. Buscar usuario por ID")
	print("4. Eliminar usuario por ID")
	print("5. Salir")
	opcion = input("Elige una opción: ")
	if opcion == "1":
		nombre = input("Nombre: ")
		edad = input("Edad: ")
		ciudad = input("Ciudad: ")
		registrar_usuario(nombre, edad, ciudad)
	elif opcion == "2":
		mostrar_usuarios()
	elif opcion == "3":
		uid = int(input("ID de usuario: "))
		print(buscar_usuario(uid))
	elif opcion == "4":
		uid = int(input("ID de usuario a eliminar: "))
		eliminar_usuario(uid)
	elif opcion == "5":
		print("Saliendo del sistema.")
		break
	else:
		print("Opción no válida.")