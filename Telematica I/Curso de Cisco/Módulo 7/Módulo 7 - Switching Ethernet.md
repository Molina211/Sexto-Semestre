# Módulo 7: Switching Ethernet

---

## Contenido

- **Trama de Ethernet:** Explica la forma en que las subcapas de Ethernet se relacionan con los campos de trama.

- **Dirección MAC de Ethernet:** Describe la dirección MAC de Ethernet.

- **La tabla de direcciones MAC:** Explica la forma en que un switch arma su tabla de direcciones MAC y reenvía las tramas.

- **Velociodades y métodos de reenvío del switch:** Describe los métodos de reenvío  de switch y la configuración de puertos disponibles para los puertos de switch en la capa 2 puertos de switch.

---

### Tramas de Ethernet

**Ethernet** es tecnología LAN por cable (pares trenzados, fibra óptica, coaxial).

Como alternativas tiene la tecnología LAN actual es WLAN (inalámbrica).

Las capas en las que opera en enlace de datos (sublayer MAC) y física.

Sus estándares son IEEE 802.2 y 802.3.

**Velocidades soportadas**:

- 10 Mbps

- 100 Mbps

- 1 Gbps

- 10 Gbps

- 40 Gbps

- 100 Gbps

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-25-08-15-46-image.png" title="" alt="" data-align="center">

Capa de enlace de datos (IEEE 802) se divide en dos subcapas:

- **LLC (Logical Link Control, IEEE 802.2):**
  
  - Comunica capas superiores ↔ hardware.
  
  - Identifica el protocolo de red usado (ej: IPv4, IPv6).
  
  - Permite que varios protocolos de Capa 3 compartan la misma interfaz.

- **MAC (Media Access Control, IEEE 802.3 / 802.11 / 802.15):**
  
  - Implementada en hardware.
  
  - Encapsula datos y controla acceso al medio.
  
  - Maneja direccionamiento en capa de enlace y se integra con la capa física.

El LLC conecta software y protocolos de red con el hardware, mientras que MAC gestiona el acceso al medio y la entrega física de las tramas.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-25-08-17-15-image.png" title="" alt="" data-align="center">



#### Subcapa MAC

La subcapa MAC (IEEE 802.3) cumple dos funciones principales:

1. **Encapsulación de datos**:
   
   - Crea la trama Ethernet (cabecera + datos + verificación).
   
   - Añade direcciones MAC de origen y destino.
   
   - Incluye un FCS para detección de errores.

2. **Acceso a los medios**:
   
   - Define cómo los dispositivos usan el medio físico (cobre, fibra, etc.).
   
   - Antes usaba CSMA/CD, hoy se usan enlaces conmutados sin colisiones.

La subcapa MAC organiza los datos en tramas y controla cómo se accede al medio de transmisión.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-25-08-19-39-image.png" title="" alt="" data-align="center">

**Ethernet heredado (antiguo)**

- **Topología**: Bus o con hubs → medio compartido.

- **Modo**: Half-dúplex (solo un dispositivo transmite a la vez).

- **Acceso**: Usa CSMA/CD (Carrier Sense Multiple Access with Collision Detection).
  
  - Escucha antes de transmitir.
  
  - Si dos dispositivos transmiten a la vez → ocurre una colisión.
  
  - Se detecta la colisión y se aplica un algoritmo de retroceso para reintentar.

- Ventaja: Permitía que varios equipos compartieran un mismo cable.

- Desventaja: Colisiones frecuentes → menor eficiencia.

**Ethernet actual (moderno)**

- **Topología**: Con switches.

- **Modo**: Full-dúplex (ambos extremos transmiten y reciben al mismo tiempo).

- **Acceso**: No necesita CSMA/CD porque cada enlace es punto a punto y no hay colisiones.

- Resultado: Comunicaciones más rápidas, estables y eficientes.



#### Campos de trama de Ethernet

El rango válido de una trama Ethernet es 64–1518 bytes; fuera de ese rango se descarta automáticamente.

- Una trama Ethernet mide entre 64 y 1518 bytes (sin contar el preámbulo).

- Menos de 64 bytes → se considera trama corta o fragmento de colisión y se descarta.

- Más de 1518 bytes → se considera trama jumbo; muchos switches y NIC modernos la soportan.

- Tramas fuera de este rango se descartan por ser inválidas (colisiones o ruido).

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-25-08-24-47-image.png" title="" alt="" data-align="center">

| **Campo**                                   | **Descripción resumida y explicada**                                                                                                |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Preámbulo y Delimitador de inicio (8 B)** | Sirve para sincronizar la comunicación entre emisor y receptor. Indica el inicio de la trama.                                       |
| **Dirección MAC de destino (6 B)**          | Identifica el dispositivo receptor. Puede ser unicast (uno), multicast (grupo) o broadcast (todos).                                 |
| **Dirección MAC de origen (6 B)**           | Identifica la NIC del emisor, es decir, quién envía la trama.                                                                       |
| **Tipo/Longitud (2 B)**                     | Indica qué protocolo de capa superior está encapsulado (IPv4=0x800, IPv6=0x86DD, ARP=0x806).                                        |
| **Datos (46 - 1500 B)**                     | Contiene la información real (ej. un paquete IPv4). Si es pequeño, se agrega relleno (pad) hasta llegar al mínimo de 64 B de trama. |
| **Secuencia de verificación FCS (4 B)**     | Campo de detección de errores usando CRC. Si los cálculos no coinciden, la trama se descarta.                                       |

---

### Dirección MAC de Ethernet

IPv4 se representa en decimal y binario, en cambio la IPv6 y direcciones MAC se representan en hexadecimal. En Hexadecimal usa dígitos 0–9 y letras A–F (16 símbolos), en relación, la mejor forma de expresarlo será 1 dígito hex = 4 bits binarios.

Dirección MAC → 48 bits → expresada con 12 dígitos hexadecimales.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-25-08-29-29-image.png" title="" alt="" data-align="center">

Un byte puede representarse como dos dígitos hexadecimales.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-25-08-30-16-image.png" title="" alt="" data-align="center">

En hexadecimal se muestran los ceros iniciales para completar el byte (ej: `00001010` → `0A`). Sus formas  más comunes de escribir hex son:

- `0x73`

- `73H`

- `73₁₆`

Para convertir entre decimal y hex, lo más práctico es pasar primero por binario.



#### Dirección MAC y hexadecimal

En Ethernet, cada dispositivo tiene una dirección MAC única que identifica su tarjeta de red (NIC). Su mejor representación seria:

Una dirección MAC = 48 bits = 6 bytes = 12 dígitos hexadecimales.

Esta dirección sirve para identificar origen y destino en la capa de enlace de datos (OSI). Siendo el “número de identidad” físico de cada tarjeta de red en una LAN.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-25-08-33-18-image.png" title="" alt="" data-align="center">

Cada MAC debe ser única, con el IEEE se da a cada fabricante un código de 24 bits (3 bytes) llamado OUI. El fabricante usa ese OUI como los primeros 6 dígitos hex de la MAC, con esto, los últimos 6 dígitos los asigna el fabricante para identificar cada dispositivo, o sea, la MAC se compone de OUI (fabricante) + número único del dispositivo.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-25-08-35-26-image.png" title="" alt="" data-align="center">

Cada fabricante (ej. **Cisco**) recibe un OUI del IEEE.

- Ejemplo: `00-60-2F` = OUI de Cisco.

Luego el fabricante añade un código propio de otros 3 bytes para diferenciar cada dispositivo.

- Ejemplo: `3A-07-BC`.

- Así se forma la MAC completa: `00-60-2F-3A-07-BC`.

El fabricante debe evitar duplicados, pero a veces ocurren por:

- **Errores de fabricación**.

- **Problemas en máquinas virtuales**.

- **Cambios manuales con software**.

Si pasa, la solución es cambiar la MAC (nueva tarjeta de red o ajuste en software).



#### Procesamiento de tramas

- Cada tarjeta de red (NIC) viene con una dirección física única llamada MAC (Media Access Control).

- También se le dice BIA (Burned-In Address) porque está grabada permanentemente en el chip ROM de la tarjeta.

- Ejemplo: `00:1A:2B:3C:4D:5E`.



**Cómo funciona en el arranque**

- Cuando el computador enciende, la tarjeta de red copia su dirección MAC desde la ROM hacia la RAM, para que el sistema operativo la use.

- Es como si la tarjeta dijera: *“Esta es mi identificación, guárdala para comunicarte en la red”*.



**Origen y destino en una trama Ethernet**

Cuando un dispositivo envía datos en Ethernet:

- En el encabezado de la trama se colocan dos direcciones:
  
  - **MAC de origen** → la de la NIC del dispositivo que envía.
  
  - **MAC de destino** → la de la NIC del dispositivo al que va dirigido.

Ejemplo: 
PC1 (MAC `AA:BB:CC:DD:EE:01`) envía un mensaje a PC2 (MAC `AA:BB:CC:DD:EE:02`). 
La trama Ethernet llevará:

- **Origen:** `AA:BB:CC:DD:EE:01`

- **Destino:** `AA:BB:CC:DD:EE:02`.



**Cambio de dirección MAC**

Aunque la dirección está grabada, los sistemas modernos permiten modificarla temporalmente en software.

- Esto se usa, por ejemplo, para conectarse a una red que filtra dispositivos por MAC.

- Pero por eso el filtrado por MAC no es totalmente seguro, ya que se puede suplantar.



Al final la NIC revisa la MAC de destino de cada trama recibida.

- Si coincide con su propia MAC → la acepta y la pasa a las capas OSI.

- Si no coincide → la descarta.

- **Excepciones:** También acepta tramas de:
  
  - **Broadcast** (`FF:FF:FF:FF:FF:FF`) → para todos.
  
  - **Multicast** → solo si el host es miembro del grupo.

- Todo dispositivo en Ethernet (PC, servidor, impresora, móvil, router) tiene NIC y dirección MAC.



#### Dirección MAC de unicast

En Ethernet, se utilizan diferentes direcciones MAC para las comunicaciones de unicast, broadcast y multicast de capa 2.
Una dirección MAC de unicast es la dirección única que se utiliza cuando se envía una trama desde un único dispositivo de transmisión a un único dispositivo de destino.

##### Paso a paso de como es el flujo de unicast

1. **Unicast en IP y MAC**
- Cuando un host quiere comunicarse con otro (ej: `192.168.1.5` → `192.168.1.200`), se usan dos direcciones:
  
  - **IP destino (unicast)** → va en el encabezado del paquete IP.
  
  - **MAC destino (unicast)** → va en el encabezado de la trama Ethernet.

- Ambas direcciones (IP + MAC) trabajan juntas para que los datos lleguen al host correcto.
2. **Cómo se obtiene la MAC destino**
- Si el host solo conoce la IP, necesita averiguar la MAC correspondiente:
  
  - En **IPv4** → usa ARP (Address Resolution Protocol).
  
  - En **IPv6** → usa ND (Neighbor Discovery).
3. **Regla importante**
- La MAC de origen siempre es unicast, porque identifica de manera única al dispositivo que envía la trama.



#### Dirección MAC broadcast

El Broadcast en Ethernet es la trama que va a todos los dispositivos de la LAN con su dirección MAC destino: **FF:FF:FF:FF:FF:FF** mientras el switch la envía por todos los puertos, menos por donde llegó. El router no la reenvía (se queda en la red local) y en IPv4, la dirección de destino con todos los bits en 1 indica “para todos en la red”.

###### Paso a paso de como es el flujo de broadcast

1. Host origen genera el mensaje quiere que todos lo reciban.

2. Encapsulación:
   
   - IP destino = broadcast (ej. `192.168.1.255`).
   
   - MAC destino = `FF:FF:FF:FF:FF:FF`.

3. Switch recibe la trama y la inunda a todos los puertos, excepto por donde entró.

4. Todos los hosts de la LAN reciben la trama y la procesan porque la MAC es broadcast.

5. Finalmente el Router no reenvía porque el broadcast queda limitado al dominio de broadcast (la red local).



#### Dirección MAC de multicast

Una trama multicast la reciben solo los dispositivos miembros de un grupo, no todos como en broadcast.

**Direcciones MAC destino:**

- `01-00-5E` → para multicast IPv4.

- `33-33` → para multicast IPv6.

También hay direcciones multicast reservadas para otros protocolos (ej. **STP**, **LLDP**).

Switches: Por defecto la envían a todos los puertos (excepto el de origen), a menos que estén configurados con snooping de multicast.

Routers: No reenvían multicast, salvo que tengan activado el enrutamiento de multicast.

**Direcciones IP de multicast:**

- IPv4 → rango `224.0.0.0 – 239.255.255.255`.

- IPv6 → rango `ff00::/8`.

La IP multicast siempre se traduce a una MAC multicast para poder entregarse en la LAN.

El origen siempre es unicast, el destino es multicast.
