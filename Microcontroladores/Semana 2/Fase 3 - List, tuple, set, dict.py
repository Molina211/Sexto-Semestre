# =============================
# FASE 3: List, tuple, set, dict
# =============================

frutas = ['manzana', 'banana', 'cereza']
print(frutas)
frutas.append('naranja')         
frutas.insert(1, 'kiwi')         
frutas.remove('banana')          
frutas.pop(0)                   
frutas.sort()                    
frutas.reverse()                 
print(frutas)
print(len(frutas))               

coordenadas = (10, 20, 30)
print(coordenadas)
x, y, z = coordenadas            
print(x, y, z)

colores = {'rojo', 'verde', 'azul'}
colores.add('amarillo')         
colores.remove('rojo')          
colores.discard('negro')         
print('verde' in colores)        
otros_colores = {'rosa', 'azul'}
union = colores.union(otros_colores)
interseccion = colores.intersection(otros_colores)
print(union)
print(interseccion)

persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print(persona['nombre'])         
persona['edad'] = 31             
persona['profesion'] = 'Ingeniero' 
del persona['ciudad']            
print(persona.keys())            
print(persona.values())         
print(persona.items())

frutas = ["Manzana", "Banano", "Fresa", "Mango", "Uva"]

frutas.sort()
print("Frutas ordenadas alfabéticamente:", frutas)

frutas.insert(0, "Papaya")  
frutas.append("Sandía")     

frutas.remove("Banano")  

del frutas[2]  

print("Lista final de frutas:", frutas)

ciudades = set()
for i in range(5):
    ciudad = input(f"Ingrese el nombre de la ciudad {i+1}: ").strip()
    ciudades.add(ciudad)

nueva_ciudad = input("Ingrese otra ciudad para agregar: ").strip()
ciudades.add(nueva_ciudad)

otras_ciudades = {"Bogotá", "Lima", "Quito"}

print("Unión de conjuntos:", ciudades.union(otras_ciudades))
print("Intersección de conjuntos:", ciudades.intersection(otras_ciudades))

ciudad_a_eliminar = input("Ingrese una ciudad para eliminar: ").strip()
if ciudad_a_eliminar in ciudades:
    ciudades.remove(ciudad_a_eliminar)
    print(f"La ciudad '{ciudad_a_eliminar}' fue eliminada.")
else:
    print(f"La ciudad '{ciudad_a_eliminar}' no está en el conjunto.")

print("Conjunto final de ciudades:", ciudades)

estudiantes = {
    "Ana": [4.5, 3.8, 4.0],
    "Luis": [3.0, 3.5, 4.2],
    "Sofía": [4.8, 4.6, 5.0]
}

nuevo_estudiante = input("Ingrese el nombre de un nuevo estudiante: ").strip()
calificaciones = []
for i in range(3):
    nota = float(input(f"Ingrese la calificación {i+1} para {nuevo_estudiante}: "))
    calificaciones.append(nota)
estudiantes[nuevo_estudiante] = calificaciones

promedios = {nombre: sum(notas)/len(notas) for nombre, notas in estudiantes.items()}

mejor_estudiante = max(promedios, key=promedios.get)
print(f"El mejor estudiante es {mejor_estudiante} con un promedio de {promedios[mejor_estudiante]:.2f}")

eliminar = input("Ingrese el nombre del estudiante a eliminar: ").strip()
if eliminar in estudiantes:
    del estudiantes[eliminar]
    print(f"El estudiante '{eliminar}' ha sido eliminado.")
else:
    print(f"El estudiante '{eliminar}' no existe.")

print("\nLista de estudiantes y sus calificaciones:")
for nombre, notas in estudiantes.items():
    print(f"{nombre}: {notas}")
