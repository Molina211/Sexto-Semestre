from machine import Pin, ADC
import utime

print("="*50)
print("SISTEMA PIR + LDR → UNA SOLA ALARMA")
print("="*50)

# Sensor PIR
pir_pin = Pin(4, Pin.IN)

# LDR (usar ADC real: 32,33,34,35,36,39)
ldr = ADC(Pin(5))
ldr.atten(ADC.ATTN_11DB)

# Alarma en GPIO 2 (válido y seguro)
alarma = Pin(1, Pin.OUT)
alarma.value(0)

# Umbral de oscuridad
UMBRAL_LUZ = 2500

print("\nCalibrando PIR... (4 segundos)\n")
utime.sleep(4)
print("Sistema listo.\n")

while True:
    valor_ldr = ldr.read()
    oscuro = valor_ldr > UMBRAL_LUZ
    movimiento = pir_pin.value() == 1

    print("LDR:", valor_ldr, "| Oscuro:", oscuro, "| Movimiento:", movimiento)

    # Activación ALARMA SOLO si se cumplen ambos
    if oscuro and movimiento:
        alarma.value(1)
        print("ALARMA ACTIVADA")
    else:
        alarma.value(0)
        print("ALARMA APAGADA")

    utime.sleep_ms(100)

