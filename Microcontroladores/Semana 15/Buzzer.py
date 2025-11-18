from machine import Pin, PWM, I2C, ADC
from ssd1306 import SSD1306_I2C
import utime
import urandom

# ===============================
# CONFIGURACIÓN DEL OLED
# ===============================
i2c = I2C(0, scl=Pin(13), sda=Pin(14))
devices = i2c.scan()
if len(devices) == 0:
    print("ERROR: No se encontró ninguna pantalla OLED")
else:
    print("Pantalla detectada en:", hex(devices[0]))

oled = SSD1306_I2C(128, 64, i2c, addr=devices[0])

def mostrar(linea1="", linea2=""):
    oled.fill(0)
    oled.text(linea1, 0, 10)
    oled.text(linea2, 0, 35)
    oled.show()

def pantalla_apagada():
    """Apaga la pantalla (negro total)"""
    oled.fill(0)
    oled.show()

def dibujar_linea(x0, y0, x1, y1):
    """Dibuja una línea gruesa usando píxeles"""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    while True:
        oled.pixel(x0, y0, 1)
        oled.pixel(x0 + 1, y0, 1)
        oled.pixel(x0, y0 + 1, 1)
        
        if x0 == x1 and y0 == y1:
            break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def mostrar_chulo():
    """Muestra un chulo grande (✓)"""
    oled.fill(0)
    dibujar_linea(40, 30, 52, 45)
    dibujar_linea(52, 45, 85, 15)
    oled.text("CORRECTO", 25, 52)
    oled.show()

def mostrar_x():
    """Muestra una X grande"""
    oled.fill(0)
    dibujar_linea(35, 15, 90, 45)
    dibujar_linea(90, 15, 35, 45)
    oled.text("INCORRECTO", 15, 52)
    oled.show()

def mostrar_advertencia():
    """Muestra advertencia de puerta abierta"""
    oled.fill(0)
    oled.text("CIERRE LA", 25, 15)
    oled.text("PUERTA", 30, 30)
    oled.text("PRIMERO!", 25, 45)
    oled.show()

# ===============================
# CONFIGURACIÓN DEL TECLADO
# ===============================
row_gpios = [36, 35, 0, 45]
row_pins = [Pin(g, Pin.OUT) for g in row_gpios]

col_gpios = [40, 39, 38, 37]
col_pins = [Pin(g, Pin.IN, Pin.PULL_DOWN) for g in col_gpios]

keys = [
    ["1", "4", "7", "*"],
    ["2", "5", "8", "0"],
    ["3", "6", "9", "#"],
    ["A", "B", "C", "D"]
]

# ===============================
# CONFIGURACIÓN DEL BOTÓN ROJO
# ===============================
boton_rojo = Pin(21, Pin.IN, Pin.PULL_UP)

# ===============================
# CONFIGURACIÓN DEL SENSOR PIR
# ===============================
pir = Pin(5, Pin.IN)   # PIR en GPIO 5
alarma_activa = False

# ===============================
# CONFIGURACIÓN DEL BUZZER (ALARMA)
# ===============================
buzzer = PWM(Pin(6))         # Cambia el pin si usas otro
buzzer.freq(1600)
buzzer.duty(0)               # Silenciado por defecto

# Frecuencias y tiempos de la alarma
ALARMA_BUZZ_FREQ_HIGH = 1600
ALARMA_BUZZ_FREQ_LOW  = 700
ALARMA_BUZZ_MS = 250         # Duración de cada tono (ms)

# Estados internos del buzzer
buzzer_on = False
_buzzer_last_toggle = utime.ticks_ms()
_buzzer_state = 0  # 0 = HIGH, 1 = LOW

def iniciar_alarma_buzzer():
    global buzzer_on, _buzzer_state, _buzzer_last_toggle
    buzzer.duty(600)  # volumen (ajusta si es necesario)
    buzzer.freq(ALARMA_BUZZ_FREQ_HIGH)
    buzzer_on = True
    _buzzer_state = 0
    _buzzer_last_toggle = utime.ticks_ms()

def detener_alarma_buzzer():
    global buzzer_on
    buzzer.duty(0)
    buzzer_on = False

def actualizar_alarma_buzzer():
    """Alterna la frecuencia cada ALARMA_BUZZ_MS sin bloquear."""
    global _buzzer_state, _buzzer_last_toggle
    if not buzzer_on:
        return
    ahora = utime.ticks_ms()
    if utime.ticks_diff(ahora, _buzzer_last_toggle) >= ALARMA_BUZZ_MS:
        _buzzer_state = 1 - _buzzer_state
        buzzer.freq(ALARMA_BUZZ_FREQ_HIGH if _buzzer_state == 0 else ALARMA_BUZZ_FREQ_LOW)
        _buzzer_last_toggle = ahora

# ===============================
# CONFIGURACIÓN DEL SENSOR LDR
# ===============================
ldr = ADC(Pin(12))
ldr.atten(ADC.ATTN_11DB)

# Umbral de luz (ajusta según tu sensor)
UMBRAL_LUZ = 700

def leer_luz():
    """Lee el valor del sensor LDR"""
    return ldr.read()

def puerta_fisica_cerrada():
    """Verifica si la puerta física está cerrada (poca luz)"""
    nivel_luz = leer_luz()
    # Retorna True si hay POCA LUZ (puerta cerrada)
    return nivel_luz > UMBRAL_LUZ

# ===============================
# CONFIGURACIÓN DEL SERVO
# ===============================
servo = PWM(Pin(7))
servo.freq(50)

def mover_servo(grados):
    min_duty = 20
    max_duty = 120
    duty = int(min_duty + (grados / 180) * (max_duty - min_duty))
    servo.duty(duty)

# ===============================
# GENERAR CÓDIGO ALEATORIO
# ===============================
def generar_codigo():
    codigo = ""
    for _ in range(4):
        codigo += str(urandom.getrandbits(4) % 10)
    print("Codigo generado:", codigo)
    mostrar("Nuevo codigo", "Ingrese clave")
    return codigo

codigo_correcto = generar_codigo()
codigo_ingresado = ""
cerradura_abierta = False

# ===============================
# FUNCIONES DEL SISTEMA
# ===============================
def abrir_cerradura():
    global cerradura_abierta
    print("Codigo correcto - Abriendo cerradura...")
    mostrar_chulo()
    utime.sleep(1.5)
    
    pantalla_apagada()
    
    mover_servo(140)
    cerradura_abierta = True
    
    print("Cerradura abierta. Cierre la puerta y presione boton.")

def cerrar_cerradura():
    global cerradura_abierta
    print("Cerrando cerradura...")
    mover_servo(47)
    cerradura_abierta = False
    utime.sleep(0.5)
    
    pantalla_apagada()
    utime.sleep(1)
    
    global codigo_correcto
    codigo_correcto = generar_codigo()
    
    print("Cerradura cerrada.")

def verificar_boton():
    """Verifica si se presionó el botón rojo - SOLO funciona si puerta está CERRADA"""
    global cerradura_abierta
    
    # Solo procesar si el botón está presionado Y la cerradura está abierta
    if boton_rojo.value() == 0 and cerradura_abierta:
        nivel_luz_actual = leer_luz()
        
        # Determinar estado de la puerta
        if nivel_luz_actual < UMBRAL_LUZ:
            estado = "ABIERTA (MUCHA LUZ)"
        else:
            estado = "CERRADA (POCA LUZ)"
        
        print("\n[BOTON] Presionado | Luz: {} | Umbral: {} | Puerta: {}".format(
            nivel_luz_actual, UMBRAL_LUZ, estado
        ))
        
        # SOLO cerrar si la puerta está físicamente CERRADA
        if puerta_fisica_cerrada():
            cerrar_cerradura()
        else:
            mostrar_advertencia()
            utime.sleep(2)
            pantalla_apagada()
        
        # Esperar a que suelte el botón
        while boton_rojo.value() == 0:
            utime.sleep_ms(10)
        utime.sleep_ms(200)
        
def verificar_pir():
    global alarma_activa

    movimiento = pir.value()
    luz = leer_luz()
    puerta_cerrada = luz > UMBRAL_LUZ

    # 🚫 Si la cerradura está abierta, NO activar alarma
    if cerradura_abierta:
        if alarma_activa:
            alarma_activa = False
            pantalla_apagada()
            detener_alarma_buzzer()   # Asegurarse que el buzzer pare
        return

    # ===============================
    #   ACTIVAR ALARMA
    # ===============================
    if movimiento == 1 and puerta_cerrada:
        if not alarma_activa:
            alarma_activa = True
            print("\n[ALERTA] Movimiento detectado con puerta cerrada!")
            mostrar("ALERTA!", "Movimiento")
            iniciar_alarma_buzzer()  # Inicia el sonido de alarma
    else:
        # ===============================
        #   DESACTIVAR ALARMA
        # ===============================
        if alarma_activa:
            alarma_activa = False
            print("[OK] Sin movimiento.")
            detener_alarma_buzzer()  # Detiene sonido cuando se apaga la alarma

            # 🟦 Mostrar pantalla normal si la cerradura sigue cerrada
            if not cerradura_abierta:
                mostrar("Sistema activo", "Ingrese clave")
            else:
                pantalla_apagada()


def leer_tecla():
    for r in range(4):
        row_pins[r].value(1)
        for c in range(4):
            if col_pins[c].value() == 1:
                tecla = keys[r][c]
                while col_pins[c].value() == 1:
                    pass
                utime.sleep_ms(200)
                row_pins[r].value(0)
                return tecla
        row_pins[r].value(0)
    return None

# ===============================
# INICIO DEL SISTEMA
# ===============================
mover_servo(47)
mostrar("Sistema activo", "Ingrese clave")
print("\n=== SISTEMA DE CERRADURA INTELIGENTE ===")
print("Umbral LDR: {}".format(UMBRAL_LUZ))
print("Valores < {} = Puerta ABIERTA (NO puede bloquearse)".format(UMBRAL_LUZ))
print("Valores > {} = Puerta CERRADA (puede bloquearse)".format(UMBRAL_LUZ))
print("\nSistema activo. Ingrese clave:\n")

# ===============================
# LOOP PRINCIPAL
# ===============================
mover_servo(47)
mostrar("Sistema activo", "Ingrese clave")
print("\n=== SISTEMA DE CERRADURA INTELIGENTE ===")
print("Umbral LDR: {}".format(UMBRAL_LUZ))
print("Valores < {} = Puerta ABIERTA (NO puede bloquearse)".format(UMBRAL_LUZ))
print("Valores > {} = Puerta CERRADA (puede bloquearse)".format(UMBRAL_LUZ))
print("\nSistema activo. Ingrese clave:\n")

try:
    while True:

        # Verificar botón rojo
        verificar_boton()

        # Verificar alarma PIR
        verificar_pir()

        # Actualiza sonido del buzzer (no bloqueante)
        actualizar_alarma_buzzer()

        # Solo leer teclado si la cerradura está cerrada
        if not cerradura_abierta:
            tecla = leer_tecla()

            if tecla:
                if tecla == "#":
                    if codigo_ingresado == codigo_correcto:
                        abrir_cerradura()
                    else:
                        print("Codigo incorrecto:", codigo_ingresado)
                        mostrar_x()
                        utime.sleep(2)
                        codigo_correcto = generar_codigo()
                    codigo_ingresado = ""
                    
                elif tecla == "*":
                    codigo_ingresado = ""
                    print("Codigo borrado")
                    mostrar("Codigo borrado", "")
                    utime.sleep(1)
                    mostrar("Ingrese clave", "")
                    
                else:
                    codigo_ingresado += tecla
                    oculto = "*" * len(codigo_ingresado)
                    print("Digitado:", oculto)
                    mostrar("Clave:", oculto)
    
        utime.sleep_ms(50)

except KeyboardInterrupt:
    print("Interrumpido por teclado - apagando buzzer y cerrando")
    detener_alarma_buzzer()
