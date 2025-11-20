# main.py - Caja fuerte + WiFi + Envío a API (archivo único)
from machine import Pin, PWM, I2C, ADC
import utime
import urandom
import dht
import urequests
import network

# ---------------------------
# CONFIG: cambia según tu red
# ---------------------------
WIFI_SSID = "LAPTOP_RE_GOD"
WIFI_PASS = "123456789"
API_BASE   = "http://172.20.10.3:8000"   # NO uses 127.0.0.1: usa la IP real de tu PC
API_SENSOR_ENDPOINT = API_BASE + "/esp32/sensores"

# ---------------------------
# FUNCIONES DE RED (WiFi)
# ---------------------------
def conectar_wifi(ssid, password, timeout_s=20):
    wlan = network.WLAN(network.STA_IF)
    try:
        if not wlan.active():
            wlan.active(True)
        # Si ya está conectado no intentamos reconectar
        if wlan.isconnected():
            return wlan
        wlan.connect(ssid, password)
    except Exception as e:
        print("Warning: excepción al iniciar WiFi:", e)

    t0 = utime.ticks_ms()
    while not wlan.isconnected():
        if utime.ticks_diff(utime.ticks_ms(), t0) > timeout_s * 1000:
            raise OSError("Tiempo de conexión WiFi excedido")
        print("Conectando WiFi...")
        utime.sleep(0.5)
    print("WiFi conectada:", wlan.ifconfig())
    return wlan

# Intento de conexión con reintentos suaves
wlan = None
for intento in range(1, 4):
    try:
        wlan = conectar_wifi(WIFI_SSID, WIFI_PASS, timeout_s=10)
        break
    except Exception as e:
        print("Intento", intento, "falló:", e)
        utime.sleep(1 + intento)
if wlan is None or not wlan.isconnected():
    print("No fue posible conectar WiFi. El sistema seguirá funcionando localmente.")
else:
    print("WiFi OK")

# ===============================
# CONFIGURACIÓN DEL OLED
# ===============================
# IMPORTANTE: si tu módulo I2C comparte pines con WiFi en tu placa, ajusta pines I2C.
try:
    i2c = I2C(0, scl=Pin(13), sda=Pin(14))
    devices = i2c.scan()
    if len(devices) == 0:
        print("ERROR: No se encontró ninguna pantalla OLED")
        oled = None
    else:
        from ssd1306 import SSD1306_I2C
        oled = SSD1306_I2C(128, 64, i2c, addr=devices[0])
        print("Pantalla detectada en:", hex(devices[0]))
except Exception as e:
    print("OLED no inicializada:", e)
    oled = None

def mostrar(linea1="", linea2=""):
    if oled is None:
        return
    try:
        oled.fill(0)
        oled.text(linea1, 0, 10)
        oled.text(linea2, 0, 35)
        oled.show()
    except Exception:
        pass

def pantalla_apagada():
    if oled is None:
        return
    oled.fill(0)
    oled.show()

# Funciones gráficas pequeñas (si falla el OLED no rompe)
def dibujar_linea(x0, y0, x1, y1):
    if oled is None:
        return
    dx = abs(x1 - x0); dy = abs(y1 - y0)
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
            err -= dy; x0 += sx
        if e2 < dx:
            err += dx; y0 += sy

def mostrar_chulo():
    if oled is None:
        return
    oled.fill(0); dibujar_linea(40,30,52,45); dibujar_linea(52,45,85,15); oled.text("CORRECTO",25,52); oled.show()

def mostrar_x():
    if oled is None:
        return
    oled.fill(0); dibujar_linea(35,15,90,45); dibujar_linea(90,15,35,45); oled.text("INCORRECTO",15,52); oled.show()

def mostrar_advertencia():
    if oled is None:
        return
    oled.fill(0); oled.text("CIERRE LA",25,15); oled.text("PUERTA",30,30); oled.text("PRIMERO!",25,45); oled.show()

# ===============================
# HARDWARE: TECLADO 4x4 (pins)
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

# Botón rojo para cerrar
boton_rojo = Pin(21, Pin.IN, Pin.PULL_UP)

# Sensor PIR
pir = Pin(4, Pin.IN)
alarma_activa = False

# nuevo: duración del evento PIR en ms y timestamp del último evento
PIR_ACTIVE_MS = 1000  # 2 segundos
pir_last_motion = 0
# Después de las variables PIR
tiempo_ultimo_cierre = 0

# LEDs estado
led_estado_abierto = Pin(15, Pin.OUT)
led_estado_cerrado = Pin(16, Pin.OUT)
led_estado_abierto.value(0); led_estado_cerrado.value(1)

# Vibrador
vib = Pin(11, Pin.OUT)
vib.value(0)
def vibrar(segundos=0.5):
    vib.value(1); utime.sleep(segundos); vib.value(0)

# ===============================
# BUZZER (PWM)
# ===============================
try:
    buzzer = PWM(Pin(6))
    buzzer.freq(1600)
    buzzer.duty(0)
except Exception as e:
    print("Buzzer PWM init error:", e)
    buzzer = None

ALARMA_BUZZ_FREQ_HIGH = 1600
ALARMA_BUZZ_FREQ_LOW  = 700
ALARMA_BUZZ_MS = 250

buzzer_on = False
alarm_type = None
_buzzer_last_toggle = utime.ticks_ms()
_buzzer_state = 0
_buzzer_pattern_index = 0

TEMP_PATTERN = [
    (2000, 100), (0,100),
    (2000,100), (0,100),
    (2000,100), (0,600),
]

# Nuevo: intervalo mínimo entre envíos/activaciones de alarma (1 minuto)
ALARM_SEND_INTERVAL_MS = 60_000
last_alarm_sent_at = 0

def iniciar_alarma_buzzer(tipo="pir"):
    global buzzer_on, alarm_type, _buzzer_state, _buzzer_last_toggle, _buzzer_pattern_index
    alarm_type = tipo
    buzzer_on = True
    if buzzer:
        buzzer.duty(600)
    _buzzer_last_toggle = utime.ticks_ms()
    if tipo == "pir":
        _buzzer_state = 0
        if buzzer:
            buzzer.freq(ALARMA_BUZZ_FREQ_HIGH)
    else:
        _buzzer_pattern_index = 0
        if buzzer:
            f,_ = TEMP_PATTERN[0]
            if f==0:
                buzzer.duty(0)
            else:
                buzzer.freq(f); buzzer.duty(600)
    # Nota: dejar envío a la API fuera de aquí para controlar frecuencia (last_alarm_sent_at)

def detener_alarma_buzzer():
    global buzzer_on, alarm_type
    if buzzer:
        buzzer.duty(0)
    buzzer_on = False
    alarm_type = None
    # Nota: no enviar aquí para evitar múltiples POSTs; enviar sólo al iniciar la alarma (controlado)

def actualizar_alarma_buzzer():
    global _buzzer_state, _buzzer_last_toggle, _buzzer_pattern_index
    # Si no está activado o no hay tipo o no hay hardware, no hacemos nada
    if not buzzer_on or alarm_type is None or buzzer is None:
        return
    ahora = utime.ticks_ms()
    # Patrón para alarma PIR: alterna entre dos frecuencias rápido
    if alarm_type == "pir":
        if utime.ticks_diff(ahora, _buzzer_last_toggle) >= ALARMA_BUZZ_MS:
            _buzzer_state = 1 - _buzzer_state
            try:
                buzzer.freq(ALARMA_BUZZ_FREQ_HIGH if _buzzer_state == 0 else ALARMA_BUZZ_FREQ_LOW)
                buzzer.duty(600)
            except Exception:
                pass
            _buzzer_last_toggle = ahora
    # Patrón para temp y remoto: sigue TEMP_PATTERN
    elif alarm_type in ("temp", "remote"):
        freq, dur = TEMP_PATTERN[_buzzer_pattern_index]
        if utime.ticks_diff(ahora, _buzzer_last_toggle) >= dur:
            _buzzer_pattern_index = (_buzzer_pattern_index + 1) % len(TEMP_PATTERN)
            freq, dur = TEMP_PATTERN[_buzzer_pattern_index]
            try:
                if freq == 0:
                    buzzer.duty(0)
                else:
                    buzzer.freq(freq); buzzer.duty(600)
            except Exception:
                pass
            _buzzer_last_toggle = ahora

# ===============================
# DHT22 sensor (temperatura)
# ===============================
dht_sensor = dht.DHT22(Pin(3))
temp_alarma = False
_TEMP_CHECK_MS = 2000
_last_temp_check = utime.ticks_ms()

def check_temp_sensor():
    global temp_alarma, _last_temp_check, last_alarm_sent_at
    ahora = utime.ticks_ms()
    if utime.ticks_diff(ahora, _last_temp_check) < _TEMP_CHECK_MS:
        return
    _last_temp_check = ahora
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        if temp is None:
            return
        # si hay supresión remota, ignorar alertas de temperatura
        if remote_disabled_until != 0 and utime.ticks_diff(remote_disabled_until, ahora) > 0:
            return
        if temp >= 30 or temp <= 0:
            if not temp_alarma:
                # comprobar intervalo entre envíos/activaciones
                if utime.ticks_diff(ahora, last_alarm_sent_at) >= ALARM_SEND_INTERVAL_MS:
                    temp_alarma = True
                    last_alarm_sent_at = ahora
                    print("[ALERTA TEMP]", temp)
                    mostrar("ALERTA TEMP", "{} C".format(temp))
                    iniciar_alarma_buzzer("temp")
                    try:
                        enviar_api()
                    except Exception as e:
                        print("enviar_api error (temp):", e)
                else:
                    # Ignorar nueva activación por intervalo
                    # print("Ignorar alerta temp: intervalo activo")
                    pass
        else:
            if temp_alarma:
                temp_alarma = False
                print("[OK TEMP]", temp)
                mostrar("Sistema activo", "Ingrese clave")
                detener_alarma_buzzer()
    except Exception as e:
        print("DHT error:", e)

# ===============================
# LDR
# ===============================
ldr = ADC(Pin(12))
ldr.atten(ADC.ATTN_11DB)
UMBRAL_LUZ = 700
def leer_luz():
    try:
        return ldr.read()
    except:
        return 0
def puerta_fisica_cerrada():
    return leer_luz() > UMBRAL_LUZ

# ===============================
# SERVO
# ===============================
servo = PWM(Pin(7))
servo.freq(50)
def mover_servo(grados):
    min_duty = 20
    max_duty = 120
    duty = int(min_duty + (grados / 180) * (max_duty - min_duty))
    try:
        servo.duty(duty)
    except:
        pass

# ===============================
# GENERAR CÓDIGO (0-9 + A-D)
# ===============================
def generar_codigo():
    pool = "0123456789ABCD"
    codigo = ""
    for _ in range(4):
        idx = urandom.getrandbits(8) % len(pool)
        codigo += pool[idx]
    print("Codigo generado:", codigo)
    mostrar("Nuevo codigo", "Ingrese clave")
    return codigo

codigo_correcto = generar_codigo()
codigo_ingresado = ""
cerradura_abierta = False

# Nuevo: tiempo desde la última tecla pulsada (evita que PIR suene mientras se escribe)
KEY_GRACE_MS = 10_000  # 10 segundos
last_key_time = utime.ticks_ms()

# Nuevo: polling de comandos del servidor
COMMAND_CHECK_MS = 2000  # ms entre consultas al servidor para recibir acciones
_last_command_check = utime.ticks_ms()  # ← inicializar para evitar NameError

# Nuevo: tiempo de supresión cuando se recibe OFF desde el servidor (5 minutos)
SUPPRESSION_MS = 5 * 60 * 1000  # 5 minutos en ms
remote_disabled_until = 0       # tick(ms) hasta cuando está suprimido (0 = no suprimido)
last_server_buzzer = None       # estado anterior leído del servidor

# ===============================
# FUNCIONES DE SISTEMA (abrir/cerrar/verificaciones)
# ===============================
def abrir_cerradura():
    global cerradura_abierta
    print("Abriendo cerradura")
    mostrar_chulo()
    utime.sleep(1.2)
    pantalla_apagada()
    mover_servo(47)
    led_estado_abierto.value(1); led_estado_cerrado.value(0)
    cerradura_abierta = True
    print("Cerradura abierta")
    # nuevo: enviar evento a la API al abrir la cerradura
    try:
        enviar_api()
    except Exception as e:
        print("enviar_api error (abrir):", e)

def cerrar_cerradura():
    global cerradura_abierta, codigo_correcto, tiempo_ultimo_cierre
    print("Cerrando cerradura")
    mover_servo(140)
    cerradura_abierta = False
    utime.sleep(0.5)
    led_estado_cerrado.value(1); led_estado_abierto.value(0)
    pantalla_apagada()
    utime.sleep(0.5)
    codigo_correcto = generar_codigo()
    tiempo_ultimo_cierre = utime.ticks_ms()  # ← Registrar tiempo
    print("Cerradura cerrada, nuevo codigo:", codigo_correcto)
    try:
        enviar_api()
    except Exception as e:
        print("enviar_api error (cerrar):", e)

def verificar_boton():
    if boton_rojo.value() == 0 and cerradura_abierta:
        if puerta_fisica_cerrada():
            cerrar_cerradura()
        else:
            mostrar_advertencia(); utime.sleep(2); pantalla_apagada()
        while boton_rojo.value() == 0:
            utime.sleep_ms(10)
        utime.sleep_ms(200)

def verificar_pir():
    global alarma_activa, pir_last_motion, codigo_ingresado, tiempo_ultimo_cierre, last_alarm_sent_at

    # Si la cerradura está abierta, NO activar alarma
    if cerradura_abierta:
        if alarma_activa:
            alarma_activa = False
            detener_alarma_buzzer()
        pir_last_motion = 0
        return

    ahora = utime.ticks_ms()

    # Delay de 5 segundos después de cerrar la puerta
    if tiempo_ultimo_cierre > 0:
        tiempo_transcurrido = utime.ticks_diff(ahora, tiempo_ultimo_cierre)
        if tiempo_transcurrido < 5000:
            if alarma_activa:
                alarma_activa = False
                detener_alarma_buzzer()
            return

    # Si hay supresión remota activa, no procesar PIR
    if remote_disabled_until != 0 and utime.ticks_diff(remote_disabled_until, ahora) > 0:
        if alarma_activa:
            alarma_activa = False
            detener_alarma_buzzer()
        pir_last_motion = 0
        return

    raw = pir.value()

    # Si se ha usado el teclado recientemente, ignorar PIR
    if utime.ticks_diff(ahora, last_key_time) < KEY_GRACE_MS:
        if alarma_activa:
            alarma_activa = False
            detener_alarma_buzzer()
        pir_last_motion = 0
        return

    # Si el código correcto ya fue ingresado, desactivar alarma
    if alarma_activa and codigo_ingresado == codigo_correcto:
        alarma_activa = False
        detener_alarma_buzzer()
        mostrar("Sistema activo", "Ingrese clave")
        pir_last_motion = 0
        return

    nivel_luz = leer_luz()
    oscuro = nivel_luz > UMBRAL_LUZ
    movimiento = raw == 1

    # LÓGICA: Alarma SOLO si oscuro Y movimiento. Además, solo permitir activación si pasó ALARM_SEND_INTERVAL_MS
    if oscuro and movimiento:
        if not alarma_activa:
            # comprobar intervalo entre activaciones/envíos
            if utime.ticks_diff(ahora, last_alarm_sent_at) >= ALARM_SEND_INTERVAL_MS:
                alarma_activa = True
                pir_last_motion = ahora
                last_alarm_sent_at = ahora
                print("[ALARMA ON] Oscuro: SI | Movimiento: SI | Luz:", nivel_luz)
                mostrar("ALERTA!", "Movimiento")
                iniciar_alarma_buzzer("pir")
                try:
                    enviar_api()
                except Exception as e:
                    print("enviar_api error (pir):", e)
            else:
                # Ignorar activación por intervalo
                # print("Ignorar PIR: intervalo activo")
                pass
    else:
        if alarma_activa:
            alarma_activa = False
            pir_last_motion = 0
            print("[ALARMA OFF] Oscuro:", oscuro, "| Movimiento:", movimiento, "| Luz:", nivel_luz)
            detener_alarma_buzzer()
            mostrar("Sistema activo", "Ingrese clave")

def check_server_commands():
    global _last_command_check, remote_disabled_until, last_server_buzzer
    ahora = utime.ticks_ms()
    if utime.ticks_diff(ahora, _last_command_check) < COMMAND_CHECK_MS:
        return
    _last_command_check = ahora
    try:
        url = API_BASE + "/esp32/buzzer"
        r = urequests.get(url, timeout=5)
        try:
            data = r.json()
        except Exception:
            data = None
        r.close()
        if not data or "buzzer" not in data:
            return
        server_buzzer = bool(data.get("buzzer"))

        # Si es la primera lectura, actúa según estado (pero no activar supresión por inicio)
        if last_server_buzzer is None:
            last_server_buzzer = server_buzzer
            if server_buzzer:
                # servidor quiere buzzer ON: activar inmediatamente
                if not buzzer_on:
                    iniciar_alarma_buzzer("remote")
            return

        # Detectar transiciones
        if last_server_buzzer and not server_buzzer:
            # transición True -> False: el usuario apagó; activar supresión 5 min
            remote_disabled_until = utime.ticks_add(ahora, SUPPRESSION_MS)
            # detener si estaba sonando
            if buzzer_on:
                detener_alarma_buzzer()
            print("[SERVER] Buzzer OFF recibido: supresión hasta", remote_disabled_until)
        elif not last_server_buzzer and server_buzzer:
            # transición False -> True: el usuario pidió ON -> cancelar supresión y activar
            remote_disabled_until = 0
            if not buzzer_on:
                iniciar_alarma_buzzer("remote")
            print("[SERVER] Buzzer ON recibido: supresión cancelada")

        # Si servidor mantiene ON y no estamos supresos, asegurar que esté activo
        if server_buzzer and (remote_disabled_until == 0 or utime.ticks_diff(remote_disabled_until, ahora) <= 0):
            if not buzzer_on:
                iniciar_alarma_buzzer("remote")

        last_server_buzzer = server_buzzer

    except Exception:
        # ignorar errores de red
        pass

# ===============================
# LECTURA TECLAS
# ===============================
def leer_tecla():
    global last_key_time
    for r in range(4):
        row_pins[r].value(1)
        for c in range(4):
            if col_pins[c].value() == 1:
                tecla = keys[r][c]
                while col_pins[c].value() == 1:
                    pass
                # registro de interacción con teclado para inhibir la alarma
                last_key_time = utime.ticks_ms()
                utime.sleep_ms(150)
                row_pins[r].value(0)
                return tecla
        row_pins[r].value(0)
    return None

# ===============================
# FUNCION: enviar datos a la API
# ===============================
def enviar_api():
    # Evitar enviar si no hay WiFi conectado
    try:
        if wlan is None or not wlan.isconnected():
            print("WiFi no conectado, envío API omitido.")
            return
    except Exception:
        pass

    # Si hay supresión remota activa, no enviar nada a la API
    ahora = utime.ticks_ms()
    if remote_disabled_until != 0 and utime.ticks_diff(remote_disabled_until, ahora) > 0:
        # suprimido: no enviar
        # opcional: podríamos enviar un log puntual, pero requisito dice no enviar nada
        return

    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
    except:
        temp = None
    payload = {
        "claveDinamica": codigo_correcto,
        "temperatura": temp,
        "alarmaBuzzer": bool(alarma_activa or temp_alarma),
    }
    try:
        print("Enviando a API:", payload)
        r = urequests.post(API_SENSOR_ENDPOINT, json=payload, timeout=5)
        r.close()
    except Exception as e:
        print("Error al enviar API:", e)

# ===============================
# INICIO: estado y loop principal
# ===============================
mover_servo(140)
mostrar("Sistema activo", "Ingrese clave")
print("Umbral LDR:", UMBRAL_LUZ)
print("Lista la caja fuerte. Ingrese clave.")

try:
    while True:
        verificar_boton()
        verificar_pir()
        check_temp_sensor()
        actualizar_alarma_buzzer()
        # nuevo: comprobar comandos del servidor (buzzer ON/OFF)
        check_server_commands()

        if not cerradura_abierta:
            tecla = leer_tecla()
            if tecla:
                if tecla == "#":
                    if codigo_ingresado == codigo_correcto:
                        abrir_cerradura()
                    else:
                        print("Codigo incorrecto:", codigo_ingresado)
                        mostrar_x()
                        vibrar(0.5)
                        utime.sleep(1.5)
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
                    mostrar("Clave:", "*" * len(codigo_ingresado))
        utime.sleep_ms(50)

except KeyboardInterrupt:
    print("Interrumpido - deteniendo buzzer")
    detener_alarma_buzzer()
except Exception as e:
    print("Error global:", e)
    try:
        detener_alarma_buzzer()
    except:
        pass




