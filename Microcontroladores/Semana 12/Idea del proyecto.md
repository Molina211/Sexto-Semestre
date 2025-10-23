# Idea del proyecto

---

## Cerradura Biométrica con Monitoreo en la Nube

### Descripción:

Sistema de seguridad inteligente que permite el acceso mediante huella digital, tarjeta RFID o código PIN, registrando cada intento en tiempo real en la nube.  
Diseñado para hogares, laboratorios o áreas restringidas, ofrece autenticación biométrica, control automatizado del cerrojo, y registro de accesos con notificaciones de alerta.

El sistema bloquea y desbloquea la puerta automáticamente, muestra mensajes en pantalla y envía los registros a Firebase para monitoreo remoto.

---

### Componentes sugeridos:

#### **Sensores:**

- **Sensor de huella dactilar (R307 o AS608)** → autenticación principal.

- **Módulo RFID RC522** → lectura de tarjetas.

- **Teclado matricial 4x4** → ingreso de PIN.

- **Sensor PIR** → detección de presencia cercana.

- **Sensor de luz (LDR)** → detección día/noche.

- **Sensor de temperatura (DHT22)** → registro ambiental.

---

#### **Actuadores (5 mínimos):**

1. **Servomotor SG90/MG996R** → mueve el cerrojo o pestillo principal.

2. **Relé 5V** → controla una luz exterior de acceso (se enciende al detectar movimiento o desbloquear).

3. **Zumbador (buzzer)** → señal sonora de acceso permitido o denegado.

4. **LEDs RGB o bicolor** → indicador visual de estado (verde = acceso, rojo = error).

5. **Microservo auxiliar o motor vibrador** → simula mecanismo interno adicional o alerta de intento fallido (vibración o movimiento del pestillo interno).  

---

#### **Motor:**

- **Servomotor principal** para el sistema de cierre y apertura automática de la puerta.

---

#### **Display:**

- **Pantalla OLED I²C 0.96”**  
  Muestra en tiempo real mensajes como:
  
  - “Esperando Identificación...”
  
  - “Acceso Autorizado ✅”
  
  - “Acceso Denegado ❌”
  
  - “Registro enviado a la nube ☁️”

---

#### **Comunicación:**

- **WiFi (ESP32 o NodeMCU ESP8266)** → conexión a internet.

- **Firebase Realtime Database** → almacenamiento de:
  
  - Usuario, hora, tipo de acceso.
  
  - Intentos fallidos y alertas.

---

#### **Extras:**

- Registro histórico de accesos consultable desde una app o web.

- Alertas en tiempo real por intentos de acceso no autorizados.

- Modo “noche” con iluminación automática.

- Control remoto opcional desde aplicación móvil.

- Recuperación de acceso mediante PIN maestro.

---

### Maqueta:

Maqueta representando una puerta inteligente en miniatura, con:

- Lector de huella, teclado y RFID visibles.

- Servomotor actuando como cerrojo.

- LEDs y zumbador para retroalimentación.

- Display OLED con los estados del sistema.

- Luz de acceso (relé) que se enciende al desbloquear.

- Conectividad WiFi activa para mostrar el registro en Firebase.

### GRUPO 10 - Jhon Sebastián Molina Fierro - Brayan Smith Bedoya Montealegre
