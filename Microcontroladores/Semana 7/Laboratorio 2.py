from machine import Pin, Timer
import time

led_verde = Pin(38, Pin.OUT)
led_amarillo = Pin(40, Pin.OUT)
led_rojo = Pin(42, Pin.OUT)

btn = Pin(14, Pin.IN, Pin.PULL_UP)

peaton = False
estado = 0

def boton_irq(pin):
    global peaton
    peaton = True

btn.irq(trigger=Pin.IRQ_FALLING, handler=boton_irq)

t = Timer(0)

def ciclo(timer):
    global estado, peaton
    if peaton:
        led_verde.off()
        led_amarillo.off()
        led_rojo.on()
        time.sleep(5)
        peaton = False
        estado = 0
    else:
        if estado == 0:
            led_verde.on()
            led_amarillo.off()
            led_rojo.off()
        elif estado == 1:
            led_verde.off()
            led_amarillo.on()
            led_rojo.off()
        elif estado == 2:
            led_verde.off()
            led_amarillo.off()
            led_rojo.on()
        estado = (estado + 1) % 3

t.init(period=2000, mode=Timer.PERIODIC, callback=ciclo)

while True:
    time.sleep(1)
