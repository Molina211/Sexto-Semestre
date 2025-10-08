from machine import Pin, ADC, Timer
import time

adc = ADC(Pin(4)) 
adc.atten(ADC.ATTN_11DB)   
adc.width(ADC.WIDTH_12BIT)  

VREF = 3.3 
data = [] 

def muestreo(timer):
    global data
    raw = adc.read()
    data.append(raw)
    if len(data) > 50:
        data.pop(0)

t = Timer(0)
t.init(period=100, mode=Timer.PERIODIC, callback=muestreo)

try:
    while True:
        time.sleep(2)
        if data:
            minimo = min(data)
            maximo = max(data)
            promedio = sum(data) / len(data)
            print("Mín:", minimo,
                  "Máx:", maximo,
                  "Promedio:", round(promedio, 2))
except KeyboardInterrupt:
    t.deinit()
    print("Detenido por el usuario")
