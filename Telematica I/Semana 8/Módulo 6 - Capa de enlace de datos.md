# Módulo 6: Capa de enlace de datos

---

## Contenido

- **Propósito de la capa de enlace de datos:** Describe el propósito y la función de la capa de enlace de datos al preparar comunicación para su transmisión en medios específicos.

- **Topologías:** Compara las características de los métodos de control de acceso a medios en WAN y LAN. Topologías LAN.

- **Trama de enlace de datos:** Describe las características y las funciones de la trama de enlace de datos.

---

### Propósito de la capa de enlace de datos

La capa de enlace de datos (Capa 2 del modelo OSI) se encarga de que la comunicación entre dispositivos (como tarjetas de red o NICs) sea confiable sobre un medio físico.

- **Interfaz con capas superiores:** Sirve de puente para que las capas superiores (como la de red) puedan usar el medio físico sin preocuparse por su tipo.

- **Encapsulación:** Toma los paquetes de la capa 3 (IPv4 o IPv6) y los convierte en tramas, que son la unidad de datos en esta capa.

- **Control del medio:** Define cómo se colocan y se reciben los datos en el medio (cables, Wi-Fi, fibra, etc.).

- **Transmisión de tramas:** Se asegura de que las tramas lleguen desde un dispositivo hasta otro.

- **Entrega al protocolo correcto:** Una vez recibe datos, los entrega a la capa superior adecuada (ejemplo: IPv4 o IPv6).

- **Detección de errores:** Revisa si las tramas están dañadas y descarta las incorrectas.

La capa de enlace de datos prepara los datos de red para la red física.



- **Nodo en redes:** Un nodo es cualquier dispositivo conectado a la red que puede manejar datos. Puede ser un dispositivo final (PC, laptop, celular) o un dispositivo intermediario (switch, router, etc.).

- **Función de la capa de enlace de datos:**
  
  - Evita que la capa de red (IP) tenga que preocuparse por los distintos tipos de medios físicos (cobre, fibra, Wi-Fi).
  
  - Si no existiera, cada protocolo de red tendría que adaptarse manualmente a cada nueva tecnología de transmisión.

- **Encapsulación en Capa 2:**
  
  - Cuando un paquete de Capa 3 (ejemplo: IPv4/IPv6) viaja por la red, la capa de enlace de datos (Capa 2) le añade información de control en forma de trama.
  
  - Esa información incluye:
    
    - **Dirección MAC de destino (Ethernet).**
    
    - **Dirección MAC de origen (NIC del emisor).**
  
  - Luego, la trama se transforma en señales entendibles para la capa física (Capa 1), que finalmente la transmite por el medio.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-22-10-42-10-image.png" title="" alt="" data-align="center">

#### Subcapas de enlace de datos IEEE 802 LAN/MAN

Los estándares IEEE 802 LAN/MAN definen cómo funcionan las redes locales (LAN) y metropolitanas (MAN), tanto cableadas como inalámbricas (Ethernet, Wi-Fi, Bluetooth, etc.).

Dentro de la capa de enlace de datos (Capa 2) se distinguen dos subcapas:

1. **LLC (Logical Link Control – IEEE 802.2):**
   
   - Actúa como intermediaria entre el software de red (protocolos como IPv4 o IPv6 en Capa 3) y el hardware de red.
   
   - Añade a la trama información para identificar qué protocolo de red se está usando.
   
   - Permite que varios protocolos de red (ej. IPv4 e IPv6) compartan la misma tarjeta de red y medio físico.

2. **MAC (Media Access Control – IEEE 802.3, 802.11, 802.15):**
   
   - Se implementa en hardware (tarjeta de red).
   
   - Encapsula los datos en tramas y decide cómo acceder al medio (quién transmite y cuándo).
   
   - Define las direcciones MAC para identificar los dispositivos.
   
   - Está ligado directamente a la capa física (cables, Wi-Fi, etc.).

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-22-10-46-39-image.png" title="" alt="" data-align="center">

**Subcapa LLC (Logical Link Control)**

- Recibe datos de la capa de red (paquetes IPv4 o IPv6).

- Le agrega información de control de Capa 2 que ayuda a que esos datos lleguen correctamente al nodo de destino.

- Actúa como “traductor” entre los protocolos de red y el hardware de la tarjeta de red.

El LLC asegura que los paquetes de red puedan viajar usando la capa de enlace sin importar el medio.

---

**Subcapa MAC (Media Access Control)**

Es la que controla directamente la tarjeta de red (NIC) y el hardware encargado de enviar y recibir datos. Aquí ocurren funciones clave:

**Encapsulación de datos en tramas**

- **Delimitación de tramas:** 
  Marca el inicio y fin de un mensaje para no confundirlo con otros. 
  *Ejemplo:* Como los sobres de una carta, sabes dónde empieza y dónde termina lo escrito.

- **Direccionamiento:** 
  Indica quién envía y quién recibe mediante direcciones MAC. 
  *Ejemplo:* Como poner remitente y destinatario en la carta para que llegue a la persona correcta.

- **Detección de errores:** 
  Revisa si el mensaje llegó bien usando un código de verificación (CRC). 
  *Ejemplo:* Como comprobar si el sobre llegó cerrado o roto antes de leer la carta.}

La subcapa MAC controla el acceso al medio en comunicaciones compartidas (semidúplex), pero no es necesaria en dúplex completo.

---

##### Explicación del cuadro

---

**1. Capa de red (gris arriba)**

- **Qué es:** Parte del modelo OSI (Capa 3). Incluye protocolos como IPv4, IPv6.

- **Función:** Se encarga del direccionamiento lógico (IP) y del enrutamiento de paquetes entre redes distintas.

- **En el cuadro:** Aparece como “Protocolo de capa de red”, que envía datos hacia la capa de enlace.

- **Ejemplo / analogía:** Es como **la dirección de la ciudad y la calle escrita en un paquete**: *Calle 10 #25, Bogotá*. Indica a qué zona debe ir el envío.

---

**2. Capa de enlace de datos (violeta grande)**

- **Qué es:** La Capa 2 del modelo OSI.

- **Función:** Asegura la entrega de datos entre dispositivos dentro de la misma red local. Encapsula los paquetes de capa 3 en tramas y los transmite al medio físico.

- **Ejemplo / analogía:** Es como **el área logística de la empresa de mensajería**, que organiza cómo debe viajar la caja dentro de la ciudad y asegura que llegue al destinatario correcto.

---

**a. Subcapa LLC (Logical Link Control – IEEE 802.2)**

- **Qué es:** Subcapa superior de la Capa 2.

- **Función:**
  
  - Conecta la capa de red (IP) con la capa de enlace.
  
  - Indica qué protocolo de red (IPv4, IPv6, ARP, etc.) se está usando.
  
  - Permite que varios protocolos de red usen la misma tarjeta de red.

- **En el cuadro:** Se ve como “Subcapa LLC – IEEE 802.2”.

- **Ejemplo / analogía:** Es como **una etiqueta en la caja que dice qué tipo de envío es** (documento, frágil, medicamento). Así, la empresa sabe cómo manejarla aunque todos viajen por el mismo camión.

---

**b. Subcapa MAC (Media Access Control)**

- **Qué es:** Subcapa inferior de la Capa 2.

- **Función:**
  
  - Controla el acceso al medio físico (quién transmite y cuándo).
  
  - Define las direcciones MAC de origen y destino.
  
  - Se encarga de encapsular los datos en tramas con control de errores.

- **En el cuadro:** Está en color violeta y se conecta directamente con los estándares específicos de red (Ethernet, WLAN, WPAN).

- **Ejemplo / analogía:** Es como **el área de despacho en la bodega** que:
  
  - Sella la caja (delimitación de tramas).
  
  - Pone etiquetas con nombre del remitente y destinatario exacto (direcciones MAC).
  
  - Revisa que la caja no esté dañada (detección de errores).
  
  - Decide qué camión/moto sale primero si hay varios esperando (control de acceso al medio).

---

**3. Estándares IEEE 802 en la subcapa MAC (verde)**

**a. Ethernet (IEEE 802.3)**

- **Qué es:** Estándar para redes cableadas.

- **Función:** Define cómo viajan las tramas en cable (UTP, fibra óptica).

- **Incluye:** Variantes como Fast Ethernet, Gigabit Ethernet, 10 Gigabit.

- **Ejemplo / analogía:** Es como **usar camiones en carretera** para transportar cajas por rutas físicas (cables).

**b. WLAN (IEEE 802.11)**

- **Qué es:** Estándar para redes inalámbricas Wi-Fi.

- **Función:** Define cómo se transmiten las tramas por radiofrecuencia.

- **Incluye:** 802.11a/b/g/n/ac/ax (Wi-Fi 5, Wi-Fi 6).

- **Ejemplo / analogía:** Es como **usar motos con radio o drones** que llevan los paquetes por el aire sin necesidad de carreteras.

**c. WPAN (IEEE 802.15)**

- **Qué es:** Estándar para redes personales inalámbricas de corto alcance.

- **Función:** Usado en dispositivos de baja potencia y corto alcance.

- **Incluye:** Bluetooth, ZigBee, RFID, etc.

- **Ejemplo / analogía:** Es como **un mensajero a pie entregando paquetes dentro de la misma cuadra o edificio**, ideal para distancias muy cortas.

---

**4. Capa física (gris abajo)**

- **Qué es:** La Capa 1 del modelo OSI.

- **Función:** Transmite los bits en forma de señales eléctricas, de radio o de luz a través del medio (cable, aire, fibra).

- **En el cuadro:** Es la base donde se apoyan Ethernet, WLAN y WPAN.

- **Ejemplo / analogía:** Es como **la carretera, la calle o el aire por donde circula el mensajero**:
  
  - Carretera asfaltada → cable UTP.
  
  - Autopista rápida → fibra óptica.
  
  - Aire libre → Wi-Fi o Bluetooth.

---

#### Provisión de acceso a los medios

Cuando un paquete IP viaja desde un host local (tu PC, por ejemplo) hasta un host remoto (un servidor en internet), pasa por varios entornos de red distintos. 
Cada entorno puede ser LAN, WAN, enlaces seriales, inalámbricos, fibra, etc., y cada uno usa su propio método de transmisión en la Capa 2 (enlace de datos).

Los routers son los encargados de que el paquete pueda atravesar todos esos entornos, porque:

1. Reciben una trama desde un medio (ej: Ethernet).

2. Desencapsulan esa trama para extraer el paquete IP.

3. Encapsulan el paquete en una nueva trama, pero esta vez adecuada al siguiente medio (ej: Serial, Wi-Fi).

4. Reenvía la nueva trama al siguiente enlace de red.

Este proceso se repite en cada salto (cada router que atraviesa el paquete).

*Ejemplo:*

Imagina que quieres enviar un regalo a un amigo que vive en otro país.

- En tu barrio, lo llevas en una bolsa plástica (LAN – trama Ethernet).

- En la terminal, cambian la bolsa por una caja de cartón (WAN – trama serial).

- Al llegar a otro país, la vuelven a cambiar por un sobre de burbuja (Wi-Fi, fibra, etc.).

- En cada punto, alguien (el router) abre el empaque, saca el regalo (el paquete IP), y lo vuelve a empacar según el transporte siguiente.

El regalo nunca cambia (el paquete IP siempre es el mismo), lo único que cambia es el empaque (trama de Capa 2) según el medio de transporte.

*La capa de enlace de datos es responsable de controlar la transferencia de tramas en todos los medios.*



#### Estándares de la capa de enlace de datos

El IETF (Internet Engineering Task Force) se encarga de protocolos como IP, TCP, HTTP, etc., que son capas superiores (red, transporte, aplicación). Pero no regula cómo viajan los bits por el cable o por el aire.

Ese trabajo lo hacen organismos especializados en normas de hardware y transmisión:

- El **IEEE** define cómo debe funcionar Ethernet y Wi-Fi.

- El **ITU** define normas para la telefonía y transmisión global.

- El **ISO** define marcos de referencia internacionales (ejemplo: OSI).

- El **ANSI** establece normas técnicas para EE. UU. que luego influyen en estándares globales.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-22-11-26-17-image.png" title="" alt="" data-align="center">

---

### Topologías

































LLC puede hacer que los protocolos capa 3 puedan pasar a capa 2
Encapsulamiento en de direccionamiento es la capa MAC

Topología COP and SCOP
Los capa 2 en direccionamiento son las MAC'S y en capa 3 son las IP's
