from machine import Pin
from time import sleep

# === Mapeo de pines a segmentos ===
segments = {
    "a": Pin(13, Pin.OUT),
    "b": Pin(14, Pin.OUT),
    "c": Pin(21, Pin.OUT),
    "d": Pin(47, Pin.OUT),
    "e": Pin(48, Pin.OUT),
    "f": Pin(45, Pin.OUT),
    "g": Pin(42, Pin.OUT)
}

# === Definición de los dígitos (segmentos que se encienden) ===
digits = {
    0: ["a","b","c","e","f","g"],
    1: ["e","a"],
    2: ["a","b","d","f","g"]
}

# === Función para mostrar un número ===
def show_digit(num):
    # Apagar todos los segmentos
    for seg in segments.values():
        seg.value(0)
    # Encender los segmentos necesarios
    for seg in digits[num]:
        segments[seg].value(1)

# === Bucle contador 1 → 9 ===
while True:
    for i in range(0, 3):
        show_digit(i)
        sleep(1)
