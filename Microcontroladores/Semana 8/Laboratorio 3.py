from machine import Pin, ADC, Timer

# Configuración ADC para LM35 en GPIO34
adc = ADC(Pin(3))
adc.atten(ADC.ATTN_11DB)   # Rango 0-3.3V
adc.width(ADC.WIDTH_12BIT) # Resolución de 12 bits (0-4095)

# LED en GPIO2
led = Pin(18, Pin.OUT)
led.value(1)
