from machine import Pin, PWM
from time import sleep

# === CONFIGURACIÓN DEL SERVO ===
servo_pin = 5  # Cambia este número según dónde conectaste el servo
servo = PWM(Pin(servo_pin), freq=50)  # Frecuencia estándar para servos (50 Hz)

# === FUNCIONES DE CONTROL ===

def mover_servo(grados):
    """
    Mueve el servo a un ángulo dado (0° a 180°)
    """
    # Convierte grados a ciclo de trabajo (duty)
    # Rango típico: 0.5ms (0°) a 2.5ms (180°)
    duty = int((grados / 180) * 100 + 25)
    servo.duty(duty)

# === PROGRAMA PRINCIPAL ===
print("\nIniciando control del servomotor...")
sleep(1)

while True:
    print("🔒 Cerradura cerrada (0°)")
    mover_servo(0)
    sleep(2)

    print("🔓 Abriendo cerradura (90°)...")
    mover_servo(90)
    sleep(3)

    print("🔄 Regresando a posición inicial (0°)...")
    mover_servo(0)
    sleep(3)
