# Módulo 3: Protocolos y modelos

---

## Contenido

- **Las reglas:** Describa los tipos de reglas que se necesitan para que se realice correctamente comunicarse.
- **Protocolos:** Explique por qué los protocolos son necesarios en la comunicación de redes.
- **Suites de protocolos:** Explique el propósito de adherirse a una suite de protocolos.
- **Organizaciones estándares:** Explique la función de las organizaciones de estandarización en el establecimiento de protocolos para la Interoperabilidad de la red.
- **Modelos de referencia:** Explique la forma en que se utilizan los modelos TCP/IP y OSI para facilitar la estandarización en el proceso de comunicación.
- **Encapsulamiento de datos:** Explique la forma en que el encapsulamiento de datos permite que estos se transporten a través e inalámbrica.
- **Acceso a los datos:** Explique la forma en que los hosts locales acceden a recursos locales en una red.

---

## Las reglas

Las redes pueden ser simples (dos PCs con un cable) o complejas (Internet), pero no basta con la conexión física: los dispositivos deben saber cómo comunicarse**.

Al igual que las personas, toda comunicación tiene tres elementos clave:

- **Origen**: Quien envía el mensaje.

- **Destino**: Quien lo recibe e interpreta.

- **Canal**: El medio por el que viaja la información.

El envío de mensajes, ya sea en persona o en una red, sigue reglas llamadas protocolos, que varían según el medio de comunicación. Igual que no usamos las mismas reglas para una llamada que para una carta, en las redes también cada medio tiene sus propios protocolos.

El proceso de enviar una carta se asemeja al de transmitir información en una red informática.

Los protocolos deben tener en cuenta los siguientes requisitos para entregar correctamente un mensaje que sea comprendido por el receptor:

- Un emisor y un receptor identificados
- Idioma y gramática común
- Velocidad y momento de entrega
- Requisitos de confirmación o acuse de recibo

Los protocolos de red no solo identifican el origen y el destino, también establecen cómo viaja el mensaje. Para ello definen aspectos clave como:

- **Codificación de mensajes**: Cómo se representan los datos.

- **Formato y encapsulamiento del mensaje**: La estructura del mensaje.

- **Tamaño del mensaje**: Cuánto puede ocupar cada mensaje.

- **Sincronización del mensaje**: En qué momento se envía y recibe.

- **Opciones de entrega del mensaje**: Distintas formas de llegar al destino.

---

### Codificación de los mensajes

El primer paso para enviar un mensaje es la codificación, que convierte la información en una forma adecuada para su transmisión. Luego, en el destino, la decodificación invierte el proceso para que el mensaje pueda ser entendido.

### Formato y encapsulamiento del mensaje

**Formato del mensaje:** Es la forma o estructura que debe tener la información para que el receptor pueda entenderla.

- Ejemplo: cuando mandas un correo electrónico, tiene asunto, cuerpo, adjuntos… todo organizado.

**Encapsulamiento del mensaje:** Es como empaquetar la información con datos extra que la red necesita para transportarla.

- Ejemplo: si mandas un paquete por mensajería, además de lo que va dentro, le pones la caja, la dirección del remitente y la del destinatario.

En redes pasa igual: el mensaje original se va metiendo en “capas” de información (direcciones IP, puertos, tipo de protocolo, etc.), y cada capa ayuda a que viaje y llegue bien a su destino.

### Tamaño del mensaje

Cuando un mensaje es muy largo y debe viajar por la red, no se manda todo de una sola vez, porque las redes tienen reglas muy estrictas sobre el tamaño máximo y mínimo de lo que pueden transportar.

Lo que hace el equipo de origen es cortar el mensaje en pedazos más pequeños, llamados tramas. 
Cada trama lleva:

- Una parte del mensaje original.

- Su propia “etiqueta” de dirección para saber de dónde viene y a dónde va. 

El receptor, al recibir todas esas tramas, las vuelve a unir como un rompecabezas para reconstruir el mensaje completo.

**Ejemplo del corte:** Imagina que quieres enviar:

`"HOLA MUNDO DESDE LA RED"`

Antes de enviarlo, el host lo divide en segmentos más pequeños. 
Ejemplo (si solo admite 8 caracteres por segmento):

- Segmento 1: "HOLA MUN"

- Segmento 2: "DO DESDE"

- Segmento 3: " LA RED"

### Sincronización del mensaje

El tiempo es clave para que la comunicación funcione bien. Se divide en tres partes:

1. **Control de flujo**
   
   - Regula la **velocidad de envío** para que el receptor no se sature.
   
   - Ejemplo: Si alguien habla demasiado rápido, el otro no entiende. En redes, los protocolos ajustan esa velocidad.

2. **Tiempo de espera (Timeout)**
   
   - Es el **límite de espera por una respuesta**.
   
   - Ejemplo: Haces una pregunta y, si no responden en unos segundos, repites o sigues adelante. En redes, si un dispositivo no responde, el otro reintenta o cierra la conexión.

3. **Método de acceso**
   
   - Define **cuándo se puede hablar o enviar datos**.
   
   - Ejemplo: Si dos personas hablan al mismo tiempo, se interrumpen. En redes pasa igual: si dos equipos envían datos al mismo tiempo, hay “choque” y deben reintentarlo.

##### ¿Qué es una NIC?

- **NIC (Network Interface Card):** Es la tarjeta de red que conecta tu computador o dispositivo a la red. Puede ser:
  
  - **Ethernet** (por cable).
  
  - **Wi-Fi** (inalámbrica).

##### ¿Qué es una WLAN?

- **WLAN (Wireless Local Area Network):** Es una red de área local inalámbrica, es decir, una red Wi-Fi.

- Ejemplo: tu router de casa que da internet sin cables a tu celular, portátil, etc.

La NIC WLAN es la tarjeta de red inalámbrica de tu dispositivo que le permite conectarse a una Wi-Fi.

### Opciones de entrega del mensaje

**Unicast**
El mensaje va de un emisor a un solo receptor.
**Ejemplo:** Cuando envías un WhatsApp a una sola persona.

**Multicast** 
El mensaje va de un emisor a un grupo específico de receptores (no a todos). 
**Ejemplo:** Cuando haces una videollamada grupal, solo los que están en el grupo reciben los datos.

**Broadcast (Transmisión)** 
El mensaje se envía a todos los dispositivos de la red, sin importar si lo necesitan o no. 
**Ejemplo:** Cuando el router anuncia su señal Wi-Fi, todos los equipos cercanos pueden verla.

**Anycast** 
El mensaje va a un grupo de receptores posibles, pero **solo uno de ellos lo recibe**, normalmente el más cercano o disponible. 
**Ejemplo:** Cuando escribes `google.com`, tu petición llega al servidor de Google más cercano para responder más rápido.

**Definición simple:**

- **Unicast** → de uno a uno.

- **Multicast** → de uno a varios.

- **Broadcast** → de uno a todos.

- **Anycast** → de uno al mejor receptor (más cercano o eficiente).

En los diagramas de red, los dispositivos se representan con un **icono de nodo** (generalmente un círculo). Estos nodos ayudan a mostrar cómo se entrega la información (unicast, multicast, broadcast, anycast) sin necesidad de dibujar computadores reales.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-03-13-56-57-image.png" title="" alt="" data-align="center">

---

## Protocolos

Para que los dispositivos se comuniquen en una red, deben seguir **protocolos**, que son reglas comunes de intercambio de mensajes.

- Los **protocolos de red** definen formato, funciones y reglas de comunicación.

- Se implementan en **software, hardware o ambos**.

- Cada protocolo cumple una función específica.

- Existen distintos **tipos de protocolos**, y todos juntos permiten que la comunicación en la red sea posible.

En la tabla se enumeran los distintos tipos de protocolos que se necesitan para habilitar las comunicaciones en una o más redes.

| **Tipo de protocolo**                    | **Descripción**                                                                                                                               |
|:---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Protocolos de comunicaciones de red**  | Permiten que dos o más dispositivos se comuniquen a través de tecnologías compatibles. Ejemplos: **IP**, **TCP**, **HTTP**.                   |
| **Protocolos de seguridad de red**       | Protegen los datos asegurando **autenticación**, **integridad** y **cifrado**. Ejemplos: **SSH**, **SSL**, **TLS**.                           |
| **Protocolos de routing**                | Permiten a los routers intercambiar información de rutas, elegir el mejor camino y dirigir el tráfico en la red. Ejemplos: **OSPF**, **BGP**. |
| **Protocolos de detección de servicios** | Se usan para la detección automática y configuración de dispositivos o servicios en la red. Ejemplos: **DHCP**, **DNS**.                      |

- **IP (Internet Protocol):** Identifica a cada dispositivo con una dirección única en la red.

- **TCP (Transmission Control Protocol):** Asegura que los datos lleguen completos y en orden.

- **HTTP (HyperText Transfer Protocol):** Protocolo usado para transferir páginas web.

- **SSH (Secure Shell):** Permite conectarse de forma segura a otro dispositivo por red (ej. administrar servidores).

- **SSL (Secure Sockets Layer):** Capa que cifra la comunicación (ej. HTTPS).

- **TLS (Transport Layer Security):** Versión mejorada de SSL, más segura y actual. Ya que el SSL no es recomendable, su uso es obsoleto.

- **OSPF (Open Shortest Path First):** Protocolo de enrutamiento que busca siempre la ruta más corta entre routers.

- **BGP (Border Gateway Protocol):** Protocolo que conecta grandes redes, como las de los proveedores de Internet.

- **DHCP (Dynamic Host Configuration Protocol):** Asigna automáticamente direcciones IP a los dispositivos de una red.

- **DNS (Domain Name System):** Traduce nombres de dominio (ej. *google.com*) a direcciones IP que entiende la red.

## Protocolos de comunicación de red

Los protocolos de comunicación de red son responsables de una varSiedad de funciones necesarias para las comunicaciones de red entre dispositivos finales. Por ejemplo, en la figura, ¿cómo envía el equipo un mensaje, a través de varios dispositivos de red, al servidor?

| **Función**                   | **Descripción**                                                                                                                              |
| ----------------------------- |:-------------------------------------------------------------------------------------------------------------------------------------------- |
| **Direccionamiento**          | Identifica al remitente y destinatario del mensaje usando un esquema definido (ej: Ethernet, IPv4, IPv6).                                    |
| **Confiabilidad**             | Garantiza que los datos lleguen completos y sin pérdidas. TCP asegura la entrega correcta.                                                   |
| **Control de flujo**          | Regula la velocidad de transmisión para que el receptor no se sature. TCP gestiona este control.                                             |
| **Secuenciación**             | Ordena los segmentos de datos y permite reconstruir el mensaje completo aunque lleguen fuera de orden o con retraso. TCP se encarga de esto. |
| **Detección de errores**      | Verifica si los datos se dañaron en el tránsito. Protocolos como Ethernet, IPv4, IPv6 y TCP incluyen este control.                           |
| **Interfaz de la aplicación** | Permite la comunicación entre aplicaciones de red. Ejemplo: HTTP o HTTPS para acceder a páginas web.                                         |

## Interracción de protocolos

Cuando un dispositivo envía una solicitud a un servidor web, se usan varios protocolos al mismo tiempo, cada uno con una función específica:

- **HTTP:** Define cómo cliente y servidor web piden y entregan páginas.

- **TCP:** Asegura que los datos lleguen completos, en orden y regula la velocidad.

- **IP:** Encargado de llevar los mensajes del origen al destino, incluso pasando por varios routers.

- **Ethernet:** Se ocupa de mover los datos entre tarjetas de red (NIC) dentro de la misma red local (LAN).

HTTP pide la página, TCP garantiza que llegue bien, IP la envía al destino correcto y Ethernet la mueve dentro de la red local.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-03-15-03-21-image.png" title="" alt="" data-align="center">

---

## Suites de protocolos

Una suite de protocolos es un grupo de protocolos que trabajan juntos para permitir la comunicación en red. Estos protocolos se organizan en una **pila de capas**:

- **Capas inferiores:** Se encargan del movimiento físico de los datos y sirven de base.

- **Capas superiores:** Se enfocan en el contenido y el significado de la información.

Cada capa depende de los servicios de la capa inferior, funcionando como un sistema escalonado.

Ejemplo con una conversación cara a cara:

- **Capa física:** La voz que transmite sonidos.

- **Capa de reglas:** Usar un idioma común para entenderse.

- **Capa de contenido:** El mensaje real que se transmite.

Ejemplo en redes:

- **Capa física:** Los cables, ondas Wi-Fi o fibra óptica que transportan señales eléctricas/luz.

- **Capa de reglas (protocolos de red):** El uso de direcciones IP y protocolos comunes (como TCP/IP) que permiten que los dispositivos se entiendan.

- **Capa de contenido:** La información que realmente se transmite, como un correo electrónico, una página web o un mensaje de WhatsApp.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-03-15-11-32-image.png" title="" alt="" data-align="center">

Una suite de protocolos es como una pila organizada, donde las capas de abajo mueven los datos y las de arriba se encargan del mensaje y su significado.

## Evolución de los conjuntos de protocolos

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-03-15-21-44-image.png" title="" alt="" data-align="center">

### Internet Protocol Suite o TCP/IP

- Es el conjunto de protocolos más usado actualmente en internet y redes locales.

- Fue creado como un estándar abierto y lo mantiene la **IETF**.

- Está organizado en capas (Aplicación, Transporte, Internet y Acceso a la red).

- Ejemplo: cuando visitas una página web, usas **HTTP (aplicación)** sobre **TCP (transporte)**, sobre **IP (internet)**, y al final viaja por **Ethernet o Wi-Fi (acceso a red)**.

### Protocolos OSI (Interconexión de Sistemas Abiertos)

- Desarrollados en 1977 por la **ISO** y la **UIT**.

- Su mayor aporte fue el **modelo de referencia OSI** con **7 capas** (físico, enlace de datos, red, transporte, sesión, presentación y aplicación).

- Aunque sus protocolos casi no se usan hoy, su modelo en capas sigue siendo fundamental para **aprender y entender cómo funciona una red**.

### **AppleTalk**

- Protocolo creado por Apple en 1985 para conectar sus computadoras y dispositivos.

- Fue muy usado en impresoras y redes locales de Apple.

- En 1995, Apple lo reemplazó por **TCP/IP**, porque se volvió el estándar universal.

### **Novell NetWare (IPX/SPX)**

- Creado en 1983 por Novell para sistemas empresariales.

- Su protocolo principal era IPX/SPX, similar a TCP/IP pero menos escalable.

- Fue muy popular en oficinas en los 80s y principios de los 90s.

- En 1995, también adoptaron TCP/IP, ya que era el más compatible y aceptado mundialmente.

## Ejemplo de protocolo TCP/IP

Los protocolos TCP/IP se usan en las capas: **Aplicación (HTTP)**, **Transporte (TCP)** e **Internet (IP)**. En la capa de acceso a la red no hay protocolos TCP/IP; ahí se usan otros como **Ethernet** (cableado) o **WLAN** (inalámbrico).

Ejemplo: Cuando un navegador web se comunica con un servidor:

- **HTTP** → define el contenido y formato de la web.

- **TCP** → asegura la entrega correcta.

- **IP** → se encarga de direccionar y mover los paquetes.

- **Ethernet/WLAN** → transporta físicamente los datos por el medio (cable o aire).

## **Conjunto de TCP/IP**

**TCP/IP** es el conjunto de protocolos usado en Internet y redes actuales, y sigue evolucionando con nuevos servicios.

Tiene dos características clave:

- **Estándar abierto**: Disponible para cualquiera, gratis y usable en hardware o software de cualquier proveedor.

- **Basado en estándares**: Aprobado por la industria y organizaciones de estándares, lo que garantiza que equipos de distintos fabricantes funcionen juntos.

### Capa de aplicación

 **Sistema de nombres**

- **DNS**: Traduce nombres de dominio (ej. cisco.com) a direcciones IP.

**Configuración de host**

- **DHCPv4/DHCPv6**: Asignan automáticamente direcciones IPv4 o IPv6.

- **SLAAC**: Autoconfiguración automática de IPv6 sin servidor.

**Correo electrónico**

- **SMTP**: Envía correos entre clientes y servidores.

- **POP3**: Descarga correos del servidor al cliente.

- **IMAP**: Permite acceder y gestionar correos directamente en el servidor.

**Transferencia de archivos**

- **FTP**: Transfiere archivos de forma confiable y con acuse de recibo.

- **SFTP**: Transfiere archivos de forma cifrada y segura usando SSH.

- **TFTP**: Versión ligera y simple de FTP, sin confirmación.

**Web y servicios web**

- **HTTP**: Transfiere páginas y contenido en la web.

- **HTTPS**: HTTP seguro con cifrado de datos.

- **REST**: Estilo de servicios web basado en APIs y solicitudes HTTP.

---

### Capa de transporte

**TCP (Protocolo de Control de Transmisión)**

- Comunicación **confiable y orientada a la conexión**.

- Garantiza que los datos lleguen completos y en orden.

- Usa confirmaciones (acuse de recibo).

**UDP (Protocolo de Datagramas de Usuario)**

- Comunicación **rápida y sin conexión**.

- No garantiza entrega ni orden de los datos.

- Útil en aplicaciones donde la velocidad es más importante que la confiabilidad (ej. streaming, juegos online).

---

### Capa de Internet

**Protocolos de Internet**

- **IPv4**: Direcciones de 32 bits, empaqueta y dirige datos.

- **IPv6**: Igual que IPv4, pero con direcciones de 128 bits (más espacio).

- **NAT**: Traduce direcciones privadas a públicas para acceder a Internet.

**Mensajería**

- **ICMPv4**: Reporta errores de entrega en IPv4.

- **ICMPv6**: Versión para IPv6.

- **ICMPv6 ND**: Descubre vecinos y evita direcciones duplicadas en IPv6.

**Protocolos de Routing**

- **OSPF**: Encuentra el camino más corto, protocolo interno de enrutamiento abierto.

- **EIGRP**: Protocolo de Cisco, calcula rutas con varias métricas (ancho de banda, retardo, etc.).

- **BGP**: Protocolo entre proveedores de Internet y grandes clientes para intercambiar rutas.

---

### Capa de acceso a la red

**Resolución de dirección**

- **ARP**: Traduce direcciones IP en direcciones MAC para enviar datos dentro de una red local.

**Protocolos de enlace de datos**

- **Ethernet**: Estándar más común para redes cableadas.

- **WLAN**: Define la comunicación inalámbrica en 2,4 GHz y 5 GHz.

---

## Organizaciones estándares

### Estándares abiertos

En redes, **los estándares abiertos** permiten que equipos de distintos fabricantes funcionen juntos, fomentando **interoperabilidad, competencia e innovación**.

Ejemplo: un router Wi-Fi funciona con cualquier PC o sistema operativo porque todos usan protocolos estándar como **IPv4, DHCP, Ethernet (802.3) y WLAN (802.11)**.

Las **organizaciones de estandarización** (sin fines de lucro y neutrales) crean y promueven estos estándares para mantener una **Internet abierta**. Pueden desarrollar reglas desde cero o basarse en protocolos ya existentes (a veces creados por un proveedor).

### Estándares de Internet

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-03-17-34-46-image.png" title="" alt="" data-align="center">

Distintas organizaciones tienen diferentes responsabilidades para promover y elaborar estándares para el protocolo TCP/IP como:

- **Sociedad de Internet (ISOC)** - Promueve el uso abierto y global de Internet.
- **Consejo de Arquitectura de Internet (IAB)** - Supervisa y guía los estándares de Internet.
- **Grupo de trabajo de ingeniería de Internet (IEFT)** - Crea y actualiza protocolos como TCP/IP (publica los RFC).
- **Grupo de trabajo de investigación de Internet (IRTF)** - Investiga a largo plazo temas de Internet (seguridad, criptografía, P2P, etc.).

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-03-17-36-22-image.png" title="" alt="" data-align="center">

- **ICANN:** Organización con sede en EE. UU. que gestiona la **asignación de direcciones IP** y la **administración de nombres de dominio** (ej. .com, .org, .net), además de otros identificadores usados en **TCP/IP**.

- **IANA:** Es parte de ICANN y se encarga de la **operación técnica**: asignar direcciones IP, administrar nombres de dominio y coordinar identificadores de protocolo.

### Organizaciones de estándares para comunicaciones y electrónica

- **IEEE (Institute of Electrical and Electronics Engineers)** 
  Organización internacional de ingeniería eléctrica y electrónica que crea estándares tecnológicos. 
  En redes, sus más famosos son **802.3 (Ethernet, cableado)** y **802.11 (WLAN, Wi-Fi inalámbrico)**.

- **EIA (Electronics Industries Alliance)**
  Famosa por estándares de **cableado, conectores y racks de 19”** usados en equipos de red.

- **TIA (Telecommunications Industry Association)**
  Crea estándares de comunicación en **radio, torres de telefonía móvil, VoIP (Voice over IP, llamadas por Internet), comunicaciones satelitales**, etc.  
  Ejemplo: en conjunto con la EIA, desarrollaron el estándar de **cables Ethernet**.

- **UIT-T (Unión Internacional de Telecomunicaciones – Sector de Normalización de Telecomunicaciones)**
  Una de las más antiguas y grandes. Define estándares para **compresión de vídeo, IPTV (Internet Protocol Television), DSL (Digital Subscriber Line, Internet por línea telefónica)** y banda ancha.

---

### Modelos de referencia

### Beneficios del uso de un modelo en capas

Los **modelos en capas** sirven para entender cómo funciona una red dividiéndola en partes más fáciles de manejar.

**Beneficios principales:**

- Facilitan el diseño de protocolos.

- Permiten que equipos de distintos fabricantes funcionen juntos.

- Aíslan los cambios en una capa sin afectar a las demás.

- Proporcionan un lenguaje común para explicar redes.

Los dos modelos más usados son:

- **OSI (Open Systems Interconnection).**

- **TCP/IP.**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-03-17-50-35-image.png" title="" alt="" data-align="center">

### El modelo de referencia de OSI

El modelo OSI define qué funciones debe cumplir cada capa de una red, sin imponer cómo hacerlo. Describe la interacción entre capas superiores e inferiores y sirve de base para entender cómo se organizan los protocolos, incluidos los de la suite TCP/IP.

| **Capa**                | **Función principal**                                                          | **Ejemplo sencillo**                      |
| ----------------------- | ------------------------------------------------------------------------------ | ----------------------------------------- |
| **7 - Aplicación**      | Servicios que usan los usuarios para comunicarse en la red.                    | HTTP (web), SMTP (correo), FTP (archivos) |
| **6 - Presentación**    | Traduce, cifra o comprime los datos para que la aplicación los entienda.       | SSL/TLS, JPEG, MP3                        |
| **5 - Sesión**          | Administra la conexión: inicio, mantenimiento y cierre.                        | Videollamadas, inicios de sesión          |
| **4 - Transporte**      | Garantiza que los datos lleguen completos y en orden (o rápido sin confirmar). | TCP, UDP                                  |
| **3 - Red**             | Decide la mejor ruta y mueve datos entre redes con direcciones IP.             | IPv4, IPv6, routers                       |
| **2 - Enlace de Datos** | Transmite datos sin errores en la misma red usando direcciones MAC.            | Ethernet, switches                        |
| **1 - Física**          | Transmite bits (0 y 1) como señales eléctricas o inalámbricas.                 | Cables, conectores, Wi-Fi                 |

#### Capa 1 – Física

- **Qué hace:** Se encarga de transmitir los **bits** por el medio físico (cables, fibra, aire, etc.).

- **Dispositivos:**
  
  - **Hub**: Repite la señal a todos los puertos, no analiza nada.
  
  - **Repetidor**: Amplifica la señal para que llegue más lejos.

- **Resumen:** Solo mueve electricidad, luz o radio, no entiende direcciones ni datos.

---

#### Capa 2 – Enlace de datos

- **Qué hace:** Envía **tramas** de un dispositivo a otro dentro de la misma red local, usando **direcciones MAC**.

- **Dispositivos:**
  
  - **Switch**: Envía datos solo al puerto correcto según la MAC, más eficiente que un hub.
  
  - **Bridge**: Conecta dos redes LAN, filtrando tráfico.

- **Resumen:** Se ocupa de **quién recibe qué** dentro de la red local.

---

#### Capa 3 – Red

- **Qué hace:** Se encarga del **enrutamiento** de paquetes entre diferentes redes, usando **direcciones IP**.

- **Dispositivos:**
  
  - **Router**: Decide por dónde enviar los paquetes para llegar al destino.
  
  - **Layer 3 Switch**: Combina funciones de switch y router.

- **Resumen:** Se ocupa de **a dónde van los datos** a través de varias redes.

---

#### Capa 4 – Transporte

- **Qué hace:** Controla cómo se entregan los datos entre aplicaciones, usando **TCP** o **UDP**.

- **Dispositivos:**
  
  - No hay muchos dispositivos físicos, pero algunos **firewalls avanzados** o **balanceadores de carga** pueden operar aquí.

- **Resumen:** Se ocupa de **qué aplicación recibe los datos y cómo**, controlando errores y orden de entrega.

---

#### Capas superiores (5, 6, 7) – Sesión, Presentación y Aplicación

- **Qué hacen:** Manejan la **interacción entre aplicaciones**, la **presentación de datos** (por ejemplo, cifrado o compresión) y la **interfaz con el usuario**.

- **Dispositivos:** Normalmente software, como:
  
  - Navegadores web
  
  - Servidores de correo
  
  - Aplicaciones de videoconferencia

- **Resumen:** No suelen ser “dispositivos de red físicos”, sino funciones que garantizan que las aplicaciones se comuniquen correctamente.

---

### Modelo de protocolo TCP/IP

El **modelo TCP/IP** (o modelo de Internet) se creó en los años 70 para describir cómo funcionan las comunicaciones en redes. Representa las funciones de cada capa de la suite de protocolos TCP/IP y, al igual que el modelo OSI, sirve como modelo de referencia para entender cómo interactúan los protocolos.

| **Capa del modelo TCP/IP** | **Explicación sencilla**                                                    |
| -------------------------- | --------------------------------------------------------------------------- |
| **4 - Aplicación**         | Es lo que el usuario ve y usa, como páginas web, correos o chats.           |
| **3 - Transporte**         | Asegura que los datos lleguen completos y en orden al destino.              |
| **2 - Internet**           | Se encarga de encontrar la mejor ruta para que los datos viajen por la red. |
| **1 - Acceso a la red**    | Es el “cableado” y dispositivos físicos que permiten enviar los datos.      |

### Comparación del modelo OSI y el modelo TCP/IP

**Puntos claves**

- El modelo **OSI** es teórico y muy detallado (7 capas).

- El modelo **TCP/IP** es más práctico (4 capas) y se ajusta a cómo funciona realmente Internet.

- TCP/IP **no define protocolos de capa física**, solo asume que existen (ej: Ethernet, Wi-Fi).

- En OSI, las capas 1 y 2 (Física + Enlace de datos) corresponden a la **capa de acceso a la red** en TCP/IP.

- En OSI, las capas 5, 6 y 7 (Sesión, Presentación y Aplicación) se combinan todas en la **capa de aplicación** en TCP/IP.

| **Modelo OSI (7 capas)** | **Modelo TCP/IP (4 capas)** | **Explicación sencilla**                                                                            |
| ------------------------ | --------------------------- | --------------------------------------------------------------------------------------------------- |
| **7. Aplicación**        | **Aplicación**              | Incluye todo lo relacionado con los programas y servicios que usan los usuarios (correo, web, FTP). |
| **6. Presentación**      | **Aplicación**              | Maneja formato, cifrado y compresión de datos. En TCP/IP se integra en la aplicación.               |
| **5. Sesión**            | **Aplicación**              | Controla diálogos y sincronización. En TCP/IP también está dentro de la capa de aplicación.         |
| **4. Transporte**        | **Transporte**              | Asegura la entrega de datos de extremo a extremo (TCP con conexión, UDP sin conexión).              |
| **3. Red**               | **Internet**                | Se encarga de direcciones lógicas y del enrutamiento (ejemplo: IP).                                 |
| **2. Enlace de datos**   | **Acceso a la red**         | Define cómo se envían los datos en un enlace físico (Ethernet, Wi-Fi).                              |
| **1. Física**            | **Acceso a la red**         | Se ocupa de la transmisión real por cables, señales o radio.                                        |

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-03-22-19-18-image.png" title="" alt="" data-align="center"> **Similitudes**

- En ambos modelos, la capa de red (OSI 3) coincide con la **capa de Internet (TCP/IP)** → se encarga de direcciones y enrutamiento.

- La capa de transporte (OSI 4) coincide con la **capa de transporte (TCP/IP)** → asegura la entrega confiable de datos entre origen y destino.

**Diferencias**

- En TCP/IP, la **capa de aplicación** reúne lo que en OSI son tres capas: **Aplicación (7), Presentación (6) y Sesión (5)**.

- En OSI, la **capa de enlace (2)** y la **capa física (1)** están separadas; en **TCP/IP** se combinan en la **capa de acceso a la red**.

---

## Encapsulamiento de datos

### Segmentación del mensaje

Cuando enviamos datos por una red, no viajan como un bloque enorme (ej: un video completo), porque:

- Ocuparía demasiado el canal y retrasaría a otros usuarios.

- Si fallara la transmisión, se perdería todo y habría que volver a enviar el archivo entero.

La ****segmentación**** se divide la información en partes pequeñas llamadas **paquetes**. Cada paquete se envía de forma independiente y puede viajar por diferentes rutas hasta llegar al destino.

### **Beneficios principales**

1. **Velocidad (Multiplexación):** Varios usuarios pueden compartir la red al mismo tiempo porque los datos viajan en pedazos pequeños que se intercalan.

2. **Eficiencia:** Si un paquete se pierde, solo se reenvía ese paquete, no toda la información.

**Ejemplo:** 
Es como enviar un libro grande por correo en varias cartas. Si se pierde una carta, solo hay que reenviar esa y no todo el libro.

---

### Secuenciación

La **secuenciación** es el proceso de **numerar los segmentos de datos** cuando se dividen para enviarse por la red. Así, aunque los paquetes lleguen desordenados (porque toman rutas distintas en la red), el receptor puede reconstruirlos en el orden correcto.

****Ejemplo****:

- Si envías un libro de 100 páginas en sobres separados, cada sobre lleva el número de página. Aunque lleguen en desorden, el receptor puede organizarlos de nuevo como estaban.

---

### Unidades de datos de protocolo (PDU)

Cuando los datos de una aplicación se envían por la red, pasan por varias capas de protocolos. Cada capa agrega información específica según su función; este proceso se llama **encapsulamiento**. La unidad de datos en cada capa se llama **PDU (Protocol Data Unit)**. Según la capa y el protocolo, la PDU recibe un nombre diferente: por ejemplo, en UDP se llama *datagrama*, mientras que en IP a veces también se le llama *datagrama IP*.

**Explicación:**

1. **Encapsulamiento:**
   
   - Cada capa del modelo de red (por ejemplo, TCP/IP) toma los datos de la capa superior, les añade su propia información de control y los pasa a la capa inferior.
   
   - Esto permite que los datos se transmitan correctamente, se enruten, se detecten errores, etc.

2. **PDU:**
   
   - Es la forma que toman los datos en cada capa.
   
   - Nombres comunes según TCP/IP:
     
     - **Capa de aplicación:** Datos
     
     - **Capa de transporte:** Segmento (TCP) o Datagrama (UDP)
     
     - **Capa de red:** Paquete o Datagrama IP
     
     - **Capa de enlace:** Trama (Frame)
     
     - **Capa física:** Bits

3. **Función de los nombres:**
   
   - Cada nombre refleja el trabajo que hace esa capa: por ejemplo, un segmento TCP incluye control de flujo y confiabilidad, mientras que un paquete IP se encarga de direccionamiento y enrutamiento.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-00-35-35-image.png" title="" alt="" data-align="center">

Resumen:

- **Datos:** PDU en la capa de aplicación.

- **Segmento/Datagrama:** PDU en la capa de transporte (TCP → segmento, UDP → datagrama).

- **Paquete:** PDU en la capa de red.

- **Trama:** PDU en la capa de enlace de datos.

- **Bits:** PDU en la capa física, transmitida por el medio.

Básicamente, cada capa le da un nombre distinto al “paquete” según la función que cumple.

---

## Acceso a los datos

### Direcciones

Las capas de red y enlace de datos trabajan juntas para enviar información del emisor al receptor, pero con objetivos distintos:

- **Capa de red:** Sus direcciones (IP) permiten que el paquete llegue del dispositivo de origen al dispositivo final, incluso si está en otra red.

- **Capa de enlace de datos:** Sus direcciones (MAC) permiten que la trama llegue de una tarjeta de red a otra dentro de la misma red local.

**Explicación sencilla:**

La capa de red se encarga del “viaje largo”: Llevar los datos al destino correcto en otra red si es necesario.

La capa de **enlace de datos** se encarga del “viaje corto”: Pasar los datos de un dispositivo al siguiente dentro de la misma red local.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-00-40-51-image.png" title="" alt="" data-align="center">



### Dirección lógica de capa 3

La **capa de red (capa 3)** usa **direcciones IP** para enviar paquetes desde el dispositivo de origen hasta el dispositivo de destino, ya sea dentro de la misma red o entre redes diferentes.

- Cada **paquete IP** tiene:
  
  - **Dirección IP de origen:** quién envía el paquete.
  
  - **Dirección IP de destino:** quién recibe el paquete.

- La **dirección IP** se divide en dos partes:
  
  1. **Porción de red / prefijo:** identifica la **red** a la que pertenece el dispositivo. Todos los dispositivos de la misma red comparten esta parte.
  
  2. **Porción de host / ID de interfaz:** identifica un **dispositivo específico** dentro de esa red.

- La **máscara de subred (IPv4)** o **longitud del prefijo (IPv6)** indica cuál parte de la dirección es de red y cuál es de host.



Conceptos a tener en cuenta:

1. **Porción de red / prefijo:**
   
   - Es la parte de la IP que indica **a qué red pertenece el dispositivo**.
   
   - Ejemplo IPv4: en 192.168.1.10/24, la porción de red es **192.168.1**.
   
   - Prefijo en IPv6 funciona igual, usando los primeros bits para la red.

2. **Porción de host / ID de interfaz:**
   
   - Es la parte de la IP que indica **el dispositivo específico** dentro de esa red.
   
   - Ejemplo IPv4: en 192.168.1.10/24, la porción de host es **10**.
   
   - En IPv6 se llama **ID de interfaz** y también identifica el dispositivo dentro de la red.

3. **Máscara de subred (IPv4):**
   
   - Es un número que indica cuántos bits de la dirección IP corresponden a la red.
   
   - Ejemplo: 255.255.255.0 → los primeros 24 bits son la red, los últimos 8 bits son host.

4. **Longitud del prefijo (IPv6):**
   
   - Funciona como la máscara de subred, pero se expresa como **/n**, donde n es la cantidad de bits de red.
   
   - Ejemplo: 2001:db8::/32 → los primeros 32 bits son la red.

En pocas palabras:

- **Porción de red / prefijo:** Indica la **red**.

- **Porción de host / ID de interfaz:** Indica el **dispositivo dentro de la red**.

- **Máscara de subred / longitud de prefijo:** Nos dice dónde termina la red y empieza el host.



### Dispositivos en la misma red

Si la porción de red de la dirección IP de origen y de destino es **igual**, significa que ambos dispositivos están en la misma red.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-01-06-26-image.png" title="" alt="" data-align="center">

### Función de las direcciones de la capa de enlace de datos (capa 2) - La misma red IP

Cuando el emisor y el receptor están en la misma red, la trama de enlace de datos se envía directamente al dispositivo receptor usando las direcciones MAC.

- **MAC de origen:** Dirección física de la tarjeta de red que envía la trama (ej. PC1 → AA-AA-AA-AA-AA-AA).

- **MAC de destino:** Dirección física del dispositivo receptor dentro de la misma red (ej. servidor FTP → CC-CC-CC-CC-CC-CC).

- El paquete IP se encapsula dentro de la trama de enlace de datos y se transmite directamente al receptor.

---

**Explicación sencilla:**

- El **IP** nos dice “a qué dispositivo final debe llegar” (dirección lógica de la red).

- La **MAC** nos dice “cómo llegar físicamente a ese dispositivo dentro de la red local” (dirección física).

- Cuando ambos dispositivos están en la misma red, no se necesita router; basta con que la NIC use la **MAC del receptor** para entregar la trama.

---

**Por qué es importante:**

- Las direcciones IP no funcionan directamente sobre el cable; los dispositivos necesitan direcciones físicas (MAC) para entregar los datos en la red local.

- La combinación IP + MAC permite que los datos lleguen correctamente desde la red local hasta el dispositivo final, ya sea en la misma red o a través de varias redes.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-01-12-31-image.png" title="" alt="" data-align="center">

Cuando un dispositivo se comunica con otro en una red remota, la dirección de la capa de red (IP) indica el destino final del paquete, mientras que la dirección de la capa de enlace de datos (MAC) se utiliza para enviar la trama al siguiente dispositivo en la ruta, normalmente un router, dentro de cada red por la que pasa el paquete.



### Función de las direcciones de la capa de red

Cuando el emisor y el receptor están en redes diferentes, las direcciones IP muestran que los hosts pertenecen a redes distintas:

- **IP de origen:** 192.168.1.110 (PC1, red de origen)

- **IP de destino:** 172.16.1.99 (servidor web, red de destino)

La **porción de red** de cada IP indica que el paquete debe atravesar más de una red para llegar al destino.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-01-41-56-image.png" title="" alt="" data-align="center">

### Rol de acceso a datos de las direcciones de capa de vínculo de datos - Diferentes redes IP

Cuando el emisor y el receptor están en redes diferentes, la trama de Ethernet no puede enviarse directamente al destino.

- La trama se envía al router o gateway predeterminado (ej. R1), que tiene una MAC en la misma red que el emisor.

- **MAC de origen:** del dispositivo emisor (PC1 → AA-AA-AA-AA-AA-AA).

- **MAC de destino:** del router/gateway (R1 → 11-11-11-11-11-11).

El router recibe la trama, desempaqueta el paquete IP y lo reenvía hacia el destino, ya sea a otro router o directamente al servidor web si está en una red conectada.

Es fundamental que cada host tenga configurada la IP del gateway predeterminado, porque todos los paquetes a redes remotas se envían a ese gateway, usando la MAC del router para salir de la red local.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-01-47-17-image.png" title="" alt="" data-align="center">

En resumen, la IP indica el destino final, la **MAC** y el **gateway** permiten que los datos salgan de tu red y lleguen correctamente al destino.



### Direcciones de enlace de datos

La dirección física (MAC) de la capa de enlace de datos tiene la función de enviar la trama de una interfaz de red a otra dentro de la misma red.

- Antes de enviarse, un paquete IP se encapsula en una trama de enlace de datos para poder transmitirse por el medio físico.

- Cada vez que el paquete pasa de host a router, de router a router, se crea una nueva trama, con direcciones de origen y destino de las NIC correspondientes.

- La capa de enlace de datos solo funciona dentro de la misma red; los routers eliminan la información de enlace anterior y agregan nueva para el siguiente salto.

**Información de la trama:**

- **Dirección de origen:** MAC de la NIC que envía la trama.

- **Dirección de destino:** MAC de la NIC que recibe la trama (siguiente router o destino final).

---

### **Explicación sencilla:**

- La **IP** indica a dónde debe llegar el paquete en términos de red lógica.

- La **MAC** indica cómo moverse físicamente entre interfaces dentro de cada red local.

- Cada vez que el paquete cruza un router, se elimina la MAC anterior y se pone una nueva, porque la trama solo funciona de NIC a NIC en la misma red.

La MAC mueve la trama en cada salto local, mientras que la IP guía el paquete hasta el destino final.



**Flujo de datos**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-01-50-19-image.png" title="" alt="" data-align="center">

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-01-50-34-image.png" title="" alt="" data-align="center">

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-04-01-50-44-image.png" title="" alt="" data-align="center">

## RESUMEN

- **Las reglas de comunicación en red**
  
  - Todo mensaje requiere un **remitente, receptor y canal**.
  
  - Se rige por **protocolos**, que definen: codificación, formato, encapsulación, sincronización, tamaño, distribución y entrega del mensaje.
  
  - Los mensajes pueden ser **unidifusión, multidifusión o difusión**.

- **Protocolos**
  
  - Se implementan en dispositivos de red y tienen funciones específicas.
  
  - Ejemplos: **Ethernet, IP, TCP, HTTP, SSH, SSL, TLS, OSPF, BGP, DHCP, DNS**.
  
  - Sus funciones incluyen: direccionamiento, confiabilidad, control de flujo, detección de errores e interfaz de aplicación.

- **Suite de protocolos**
  
  - Conjunto de protocolos interrelacionados para la comunicación (ejemplo: **TCP/IP**).
  
  - TCP/IP es la base de Internet, abierto y basado en estándares.
  
  - Procesos como encapsulación/descapsulación permiten enviar y recibir información entre cliente y servidor.

- **Organizaciones de estandarización**
  
  - Promueven la **interoperabilidad y la innovación**.
  
  - Ejemplos: **ISOC, IAB, IETF, IRTF, ICANN, IANA, IEEE, EIA, TIA, ITU-T**.

- **Modelos de referencia**
  
  - **Modelo OSI (7 capas):** Aplicación, Presentación, Sesión, Transporte, Red, Enlace de datos, Física.
  
  - **Modelo TCP/IP (4 capas):** Aplicación, Transporte, Internet, Acceso a la red.

- **Encapsulación de datos**
  
  - Permite dividir mensajes en segmentos pequeños (**multiplexación y eficiencia**).
  
  - Cada capa encapsula su PDU y al llegar al receptor se **desencapsula**.
  
  - **TCP** organiza y secuencia los segmentos.

- **Acceso a los datos**
  
  - La **capa de red** usa direcciones **IP** para enviar paquetes.
  
  - La **capa de enlace de datos** usa direcciones **MAC** para enviar tramas en la red local.
  
  - Direcciones IP incluyen parte de red y parte de host, con IPv4 o IPv6.
  
  - Si el destino está en otra red, los paquetes se envían a través de un **router o gateway**.
