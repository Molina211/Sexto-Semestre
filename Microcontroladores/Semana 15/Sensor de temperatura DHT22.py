from machine import Pin
import dht
import utime

print("="*50)
print("SENSOR DHT22 + ALARMA DE TEMPERATURA")
print("="*50)

# Configuración de pines
sensor = dht.DHT22(Pin(3))  # DATA del DHT22
led = Pin(1, Pin.OUT)       # LED en GPIO 1

print("DHT22: GPIO 4")
print("LED:   GPIO 1\n")

while True:
    try:
        sensor.measure()                # Leer datos
        temp = sensor.temperature()     # °C
        hum = sensor.humidity()

        print("Temp:", temp, "°C | Humedad:", hum, "%")

        # -------------------------------
        #     CONDICIONES DE ALARMA
        # -------------------------------
        if temp >= 30:
            print("🔥 ALERTA: ¡Temperatura MUY ALTA!")
            led.value(1)

        elif temp <= 10:
            print("❄️ ALERTA: ¡Temperatura MUY BAJA!")
            led.value(1)

        else:
            print("👌 Temperatura normal")
            led.value(0)

        utime.sleep(0.5)
    except Exception as e:
        print("Error al leer el sensor:", e)
        utime.sleep(0.5)
    