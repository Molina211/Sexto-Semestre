from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# ===============================
# CONFIGURACIÓN DEL I2C
# ===============================
# Usa tus pines reales
# SCL = Pin 7
# SDA = Pin 15
i2c = I2C(0, scl=Pin(7), sda=Pin(15))

# Detección automática de dirección
devices = i2c.scan()
if len(devices) == 0:
    print("ERROR: No se encontró ninguna pantalla OLED")
else:
    print("Pantalla detectada en:", hex(devices[0]))

# Crear pantalla
oled = SSD1306_I2C(128, 64, i2c, addr=devices[0])

# ===============================
# FUNCIÓN: DIBUJAR GATITO
# ===============================
def gato_pixel():
    oled.fill(0)

    # Orejas
    oled.fill_rect(20, 10, 10, 10, 1)   # Izquierda
    oled.fill_rect(98, 10, 10, 10, 1)   # Derecha

    # Cabeza
    oled.fill_rect(25, 20, 80, 40, 1)

    # Ojos
    oled.fill_rect(45, 30, 10, 10, 0)   # Ojo izquierdo
    oled.fill_rect(75, 30, 10, 10, 0)   # Ojo derecho

    # Nariz
    oled.pixel(64, 45, 0)

    # Boca
    oled.line(60, 48, 64, 50, 0)
    oled.line(64, 50, 68, 48, 0)

    # Bigotes (izquierda)
    oled.line(40, 45, 20, 45, 0)
    oled.line(40, 48, 20, 50, 0)

    # Bigotes (derecha)
    oled.line(88, 45, 108, 45, 0)
    oled.line(88, 48, 108, 50, 0)

    # Texto
    oled.text("Miau!", 50, 58, 0)

    # Mostrar en pantalla
    oled.show()


# ===============================
# PROGRAMA PRINCIPAL
# ===============================
print("Mostrando gatito en OLED...")

gato_pixel()

while True:
    time.sleep(1)  # Mantener programa vivo
