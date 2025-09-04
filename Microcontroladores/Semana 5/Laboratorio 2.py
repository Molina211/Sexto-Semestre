from machine import Pin
from time import sleep

# Definir pines
amarillo = Pin(13, Pin.OUT)
rojo = Pin(21, Pin.OUT)

amarillo.value(0)
rojo.value(0)

puertaPrincipal = Pin(45, Pin.IN, Pin.PULL_UP)
puertaTrasera = Pin(37, Pin.IN, Pin.PULL_UP)
patio = Pin(41, Pin.IN, Pin.PULL_UP)

if puertaPrincipal.value()==1:
    amarillo.value(1)