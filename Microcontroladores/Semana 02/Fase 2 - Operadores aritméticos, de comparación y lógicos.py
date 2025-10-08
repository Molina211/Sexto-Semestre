# =============================
# FASE 2: Operadores aritméticos, de comparación y lógicos
# =============================

a = 10
b = 3
print(a + b)      
print(a - b)      
print(a * b)      
print(a / b)      
print(a // b)     
print(a % b)      
print(a ** b)     

x = 5
y = 10
print(x == y)     
print(x != y)     
print(x < y)     
print(x >= 5)     

edad = 20
es_estudiante = True
print(edad > 18 and es_estudiante)   
print(edad < 18 or es_estudiante)    
print(not es_estudiante)

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2 if num2 != 0 else 'No se puede dividir por cero'}")
print(f"Módulo: {num1 % num2 if num2 != 0 else 'No se puede calcular módulo con cero'}")

if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num1 < num2:
    print("El primer número es menor que el segundo.")
else:
    print("Ambos números son iguales.")

edad = int(input("Ingresa tu edad: "))
es_estudiante = input("¿Eres estudiante? (True/False): ").strip().capitalize()

if es_estudiante == "True":
    es_estudiante = True
elif es_estudiante == "False":
    es_estudiante = False
else:
    print("Respuesta inválida, se asumirá como False.")
    es_estudiante = False

if edad < 18 or es_estudiante:
    print("Tienes acceso al descuento ✅")
else:
    print("No tienes acceso al descuento ❌")

n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))

promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio}")

if promedio >= 10:
    print("El promedio es mayor o igual a 10 ✅")
else:
    print("El promedio es menor que 10 ❌")

if n1 > 0 and n2 > 0 and n3 > 0:
    print("Todos los números son positivos ✅")
else:
    print("No todos los números son positivos ❌")

if (n1 % 2 == 0) or (n2 % 2 == 0) or (n3 % 2 == 0):
    print("Al menos uno de los números es par ✅")
else:
    print("Ninguno de los números es par ❌")
