from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Configuración del I2C (ajusta si tus pines son diferentes)
i2c = I2C(0, scl=Pin(7), sda=Pin(15))
oled = SSD1306_I2C(128, 64, i2c)

# --- Funciones para cada pantalla ---

def pantalla_inicio():
    oled.fill(0)
    oled.text("== MENU PRINCIPAL ==", 0, 0)
    oled.text("> Estado del Sistema", 0, 20)
    oled.text("> Sensores", 0, 35)
    oled.text("> Configuracion", 0, 50)
    oled.show()

def pantalla_estado():
    oled.fill(0)
    oled.text("== ESTADO SISTEMA ==", 0, 0)
    oled.text("CPU: 73%", 0, 20)
    oled.text("Temp: 28.5 C", 0, 35)
    oled.text("Voltaje: 3.3V", 0, 50)
    oled.show()

def pantalla_sensores():
    oled.fill(0)
    oled.text("== SENSORES ACTIVOS ==", 0, 0)
    oled.text("Sensor 1: OK", 0, 20)
    oled.text("Sensor 2: OK", 0, 35)
    oled.text("Sensor 3: OFF", 0, 50)
    oled.show()

def pantalla_config():
    oled.fill(0)
    oled.text("== CONFIGURACION ==", 0, 0)
    oled.text("Modo: AUTO", 0, 20)
    oled.text("Brillo: Medio", 0, 35)
    oled.text("WiFi: Conectado", 0, 50)
    oled.show()

# --- Lógica principal del menú ---
pantallas = [pantalla_inicio, pantalla_estado, pantalla_sensores, pantalla_config]
indice = 0

while True:
    # Llamar a la función de la pantalla actual
    pantallas[indice]()
    
    # Esperar unos segundos antes de cambiar
    time.sleep(3)
    
    # Pasar a la siguiente pantalla (cíclicamente)
    indice = (indice + 1) % len(pantallas)
