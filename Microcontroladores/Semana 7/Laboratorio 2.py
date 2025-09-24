from machine import Pin, Timer
import time

led_verde = Pin(13, Pin.OUT)
led_amarillo = Pin(21, Pin.OUT)
led_rojo = Pin(48, Pin.OUT)
btn = Pin(42, Pin.IN, Pin.PULL_UP)

peaton = False
estado_actual = 0
tiempo_peaton = 0
ciclo_contador = 0
TIEMPO_PEATON_ROJO = 8

DURACION_ROJO = 6
DURACION_AMARILLO = 2
DURACION_VERDE = 6

def apagar_todos():
    led_verde.off()
    led_amarillo.off()
    led_rojo.off()

def encender_verde():
    apagar_todos()
    led_verde.on()

def encender_amarillo():
    apagar_todos()
    led_amarillo.on()

def encender_rojo():
    apagar_todos()
    led_rojo.on()

def boton_irq(pin):
    global peaton
    if not peaton:
        peaton = True
        print("¡Peatón detectado! Activando semáforo...")

btn.irq(trigger=Pin.IRQ_FALLING, handler=boton_irq)

t = Timer(0)

def ciclo(timer):
    """Función principal del ciclo del semáforo"""
    global peaton, estado_actual, tiempo_peaton, ciclo_contador
    
    if peaton:
        encender_rojo()
        tiempo_peaton += 1
        print(f"Modo peatón activo - Tiempo restante: {TIEMPO_PEATON_ROJO - tiempo_peaton + 1}s")
        
        if tiempo_peaton >= TIEMPO_PEATON_ROJO:
            peaton = False
            tiempo_peaton = 0
            estado_actual = 1
            ciclo_contador = 0
            print("Fin del modo peatón.")
    
    else:
        if estado_actual == 0:
            encender_rojo()
            if ciclo_contador == 0:
                print("Semáforo: ROJO (6s)")
            ciclo_contador += 1
            
            if ciclo_contador >= DURACION_ROJO:
                estado_actual = 1
                ciclo_contador = 0
                
        elif estado_actual == 1:
            encender_amarillo()
            if ciclo_contador == 0:
                print("Semáforo: AMARILLO (2s) - Preparando verde")
            ciclo_contador += 1
            
            if ciclo_contador >= DURACION_AMARILLO:
                estado_actual = 2
                ciclo_contador = 0
                
        elif estado_actual == 2:
            encender_verde()
            if ciclo_contador == 0:
                print("Semáforo: VERDE (6s)")
            ciclo_contador += 1
            
            if ciclo_contador >= DURACION_VERDE:
                estado_actual = 3
                ciclo_contador = 0
                
        elif estado_actual == 3:
            encender_amarillo()
            if ciclo_contador == 0:
                print("Semáforo: AMARILLO (2s) - Preparando rojo")
            ciclo_contador += 1
            
            if ciclo_contador >= DURACION_AMARILLO:
                estado_actual = 0
                ciclo_contador = 0

t.init(period=1000, mode=Timer.PERIODIC, callback=ciclo)

encender_rojo()
print("Semáforo iniciado. Presiona el botón para activar el paso de peatones.")
print("Ciclo: Rojo (6s) → Amarillo (2s) → Verde (6s) → Amarillo (2s) → Rojo...")
print("Modo peatón: Rojo fijo por 8 segundos.")

while True:
    time.sleep(1)