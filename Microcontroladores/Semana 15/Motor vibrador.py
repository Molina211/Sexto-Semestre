from machine import Pin
import time

# Pin que controla la base del transistor
vib = Pin(11, Pin.OUT)   # Usa el GPIO que tengas conectado

print("Motor vibrador listo...")

while True:
    vib.value(1)     # Encender vibración
    time.sleep(0.5)  # Vibra medio segundo
    vib.value(0)     # Apagar vibración
    time.sleep(0.5)  # Pausa medio segundo
