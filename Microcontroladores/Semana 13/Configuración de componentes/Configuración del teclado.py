from machine import Pin
from time import sleep

# === CONFIGURACIÓN DE PINES ===
# Pines de las filas (salida) → invertidos para que correspondan correctamente
filas_pines = [46, 18, 17, 16]
# Pines de las columnas (entrada) → ya están en el orden correcto
columnas_pines = [15, 12, 11, 10]

# Inicialización de pines
filas = [Pin(pin, Pin.OUT) for pin in filas_pines]
columnas = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in columnas_pines]

# Mapa del teclado (4x4)
teclas = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

print("\nPresiona una tecla en el teclado matricial...\n")

while True:
    for f in range(4):
        # Activar una fila a la vez
        for i in range(4):
            filas[i].value(1 if i == f else 0)

        # Leer las columnas
        for c in range(4):
            if columnas[c].value() == 1:
                tecla = teclas[f][c]
                print("🔹 Tecla presionada:", tecla)
                print("   ➜ Fila GPIO:", filas_pines[f], "| Columna GPIO:", columnas_pines[c], "\n")
                sleep(0.3)
