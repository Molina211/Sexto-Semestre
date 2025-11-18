from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(4), freq=50)

# LÍMITES REALES DE TU SERVO
DUTY_MIN = 40     # posición 0°
DUTY_MAX = 130    # posición 180°

def mover_servo(grados):
    # Convierte grados (0–180) al rango de duty que tu servo acepta
    duty = DUTY_MIN + (grados / 180) * (DUTY_MAX - DUTY_MIN)
    servo.duty(int(duty))

print("→ Moviendo a posición inicial (0°)...")
mover_servo(0)
sleep(1)

print("→ Iniciando recorrido grande...")

# Recorrido desde 0° hasta 180°
for angulo in range(110, -1, -5):
    mover_servo(angulo)
    print("Ángulo:", angulo)
    sleep(0.05)

# Regreso desde 180° a 0°
print("→ Volviendo a 0°...")
for angulo in range(-1, 111, 5):
    mover_servo(angulo)
    print("Ángulo:", angulo)
    sleep(0.05)

print("✔ Recorrido completo")
