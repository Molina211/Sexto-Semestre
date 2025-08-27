# =============================
# FASE 1: Recolección de datos
# =============================

nombre1 = input('Ingrese su nombre: ')
edad1 = input('Ingrese su edad: ')

print('Hola,', nombre1)
print(f'Tienes {edad1} años')

texto = 'Hola Python'
print(texto.upper())      
print(texto.lower())      
print(len(texto))         
print(texto[0])           

numero = 10
pi = 3.1416
es_mayor = True
print(type(numero))       
print(type(pi))           
print(type(es_mayor))     

numero_str = '50'
numero_int = int(numero_str)
print(numero_int + 10)   

nombre2 = input("Ingresa tu nombre: ")
edad2 = int(input("Ingresa tu edad: "))

edad_proxima = edad2 + 1

print(f"Hola {nombre2}, el próximo año tendrás {edad_proxima} años")

nombre_completo = input("Ingresa tu nombre completo: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
ciudad = input("Ingresa tu ciudad de residencia: ")

anio_actual = 2025
edad3 = anio_actual - anio_nacimiento

mensaje = f"Hola {nombre_completo}, tienes {edad3} años y vives en {ciudad}"
print(mensaje.upper())

print(f"Tu nombre tiene {len(nombre_completo)} caracteres en total.")

from datetime import date

nombre3 = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
anio = int(input("Ingresa tu año de nacimiento: "))
mes = int(input("Ingresa tu mes de nacimiento (1-12): "))
dia = int(input("Ingresa tu día de nacimiento: "))

hoy = date.today()
fecha_nacimiento = date(anio, mes, dia)
edad = hoy.year - fecha_nacimiento.year

if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

print(f"Hola, {apellido}, {nombre3}. Naciste el {dia}/{mes}/{anio} y tienes {edad} años.")

nombre_completo = f"{nombre3} {apellido}"
cantidad_letras = sum(1 for c in nombre_completo if c.isalpha()) 
cantidad_espacios = nombre_completo.count(" ")

print(f"Tu nombre completo tiene {cantidad_letras} letras y {cantidad_espacios} espacios.")
