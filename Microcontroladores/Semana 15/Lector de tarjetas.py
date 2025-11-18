from machine import Pin
import utime

try:
    from mfrc522 import MFRC522
except:
    print("ERROR: Falta mfrc522.py en el ESP32")
    raise

# ====== PINES ======
SCK  = 5
MOSI = 10
MISO = 11
RST  = 21
CS   = 4
IRQ_PIN = 2

# ===== UID VIRTUAL =====
VIRTUAL_UID = [0xAB, 0xCD, 0x12, 0x34]   # Puedes cambiarlo

# ====== Inicializar MFRC522 ======
rdr = MFRC522(
    sck=Pin(SCK),
    mosi=Pin(MOSI),
    miso=Pin(MISO),
    rst=Pin(RST),
    cs=Pin(CS)
)

print("MFRC522 inicializado correctamente")

# ====== IRQ ======
irq_flag = [False]

def irq_handler(pin):
    irq_flag[0] = True

irq_pin = Pin(IRQ_PIN, Pin.IN, Pin.PULL_UP)
irq_pin.irq(trigger=Pin.IRQ_FALLING, handler=irq_handler)

print("\n> Modo mixto: REAL + VIRTUAL")
print("> Si no hay tarjeta real, se usará una tarjeta virtual\n")

ultimo_uid = None

def uid_to_hex(uid):
    return " ".join("{:02X}".format(x) for x in uid)


while True:

    tarjeta_leida = False

    # ----- Intento por IRQ -----
    if irq_flag[0]:
        irq_flag[0] = False
        stat, tag_type = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            stat, uid = rdr.anticoll()
            if stat == rdr.OK:
                print("💳 UID REAL detectado (IRQ) →", uid_to_hex(uid))
                tarjeta_leida = True
                ultimo_uid = uid

    # ----- Intento por Polling -----
    if not tarjeta_leida:
        stat, tag_type = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            stat, uid = rdr.anticoll()
            if stat == rdr.OK:
                print("🔎 UID REAL detectado (Polling) →", uid_to_hex(uid))
                tarjeta_leida = True
                ultimo_uid = uid

    # ----- Si NO hay tarjeta → activar TARJETA VIRTUAL -----
    if not tarjeta_leida:
        print("🟦 Sin tarjeta → usando TARJETA VIRTUAL:", uid_to_hex(VIRTUAL_UID))
        ultimo_uid = VIRTUAL_UID

    utime.sleep(1)
