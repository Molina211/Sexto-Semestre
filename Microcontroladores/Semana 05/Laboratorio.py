from machine import Pin
from time import sleep

SMS = Pin(13, Pin.OUT)
alarmaSilenciosa = Pin(21, Pin.OUT)
alarmaSonora = Pin(48, Pin.OUT)

puertaDelantera = Pin(36, Pin.IN, Pin.PULL_UP)
puertaTrasera = Pin(38, Pin.IN, Pin.PULL_UP)
patio = Pin(41, Pin.IN, Pin.PULL_UP)

while True:
    
    SMS.value(0)
    alarmaSilenciosa.value(0)
    alarmaSonora.value(0)
    
    puertaD = (puertaDelantera.value()==0)
    puertaT = (puertaTrasera.value()==0)
    sensorP = (patio.value()==0)
    
    if (puertaD ^ puertaT) and not sensorP:
        alarmaSilenciosa.value(1)

    
    elif (puertaD ^ puertaT) and sensorP:
        alarmaSonora.value(1)

    
    elif (puertaD and puertaT and sensorP):
        alarmaSonora.value(1)
        SMS.value(1)

    sleep(0.1)