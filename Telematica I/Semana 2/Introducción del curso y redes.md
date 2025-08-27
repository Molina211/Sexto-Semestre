# Introducción del curso CCNA1v7 TELI 90B 2025B AHALARCON G2 de Cisco y redes

---

1. Suscripción del curso con su Gmail institucional por medio del link:
   
    *https://www.netacad.com/courses/ccna-introduction-networks?courseLang=es-XL&instance_id=a53879b5-08f2-43cd-b928-30760a9fab36*

2. Descarga e instalación del software (Packet Tracer) para el curso

3. Explicación de conceptos iniciales:

---

- ##### Host:
  
  Un host es cualquier dispositivo que puede enviar y recibir datos en una red y que tiene una dirección IP. 
  
  **Ejemplo**: Una computadora de escritorio conectada a Internet para navegar o enviar correos.

- ##### Peer-to-Peer (P2P):
  
  Es un modelo de red donde cada dispositivo (nodo) actúa como cliente y servidor a la vez, compartiendo recursos directamente sin un servidor central.
  
  **Ejemplo**: La *red BitTorrent*, donde los usuarios intercambian archivos directamente entre sí.

- ##### End Devices:
  
  Son dispositivos finales que están en el borde de la red, utilizados por los usuarios para acceder o enviar información. Es el punto donde la red y el usuario se encuentran. Es lo que usas para consumir o producir información, no para encaminarla.
  
  **Ejemplo**: Un teléfono inteligente conectado a una red Wi-Fi para usar aplicaciones de mensajería.

- ##### Intermediary Network Devices:
  
  Son dispositivos que no están al final de la red, sino en medio, encargados de encaminar, filtrar, dirigir o gestionar el tráfico de datos entre los *end devices*. Su función es mantener la red funcionando de forma eficiente y segura.

---

### Componentes de conexión:

- ##### Network Media:
  
  Son los medios físicos o inalámbricos por los que viajan los datos entre dispositivos en una red. Funcionan como el camino que conecta *end devices* e *intermediary devices*.
  
  - **Metal wires within cables**: Usan hilos de cobre para transmitir datos mediante señales eléctricas. 
    
    Ejemplo: Cable Ethernet UTP (Cat5e, Cat6) usado en redes LAN.
  
  - **Glass or plastic fibers within cables (Fiber-optic cable)**: Usan fibras de vidrio o plástico para transmitir datos mediante pulsos de luz, lo que permite alta velocidad y larga distancia.
    
    Ejemplo: Cable de fibra óptica que conecta un proveedor de Internet con un barrio o edificio.
  
  - **Wireless transmission**: Transmite datos mediante ondas electromagnéticas (radio, microondas, infrarrojo) sin necesidad de cables físicos.
    
    Ejemplo: Conexión Wi-Fi o Bluetooth entre un teléfono y un altavoz.

- ##### Netwotk Representations:
  
  - **Network Interface Card (NIC)**: 
    
    Es una tarjeta de red (puede ser física o integrada en la placa madre) que permite que un dispositivo se conecte a una red. Convierte los datos del dispositivo en señales que pueden viajar por el *network media*. Normalmente se dibuja como parte del *end device* (computadora, servidor, impresora) y se indica con un ícono de conexión de red o un puerto Ethernet/Wi-Fi.
  
  - **Physical (Topology)**:
    
    Es la disposición física de los dispositivos y cables en una red: cómo están físicamente conectados. Mediante un mapa visual que muestra la ubicación real de cables, switches, routers y dispositivos finales
  
  - **Logical topology**: 
    
    Describe cómo fluye la información dentro de la red, sin importar la disposición física de los cables. Se basa en direcciones IP, rutas, y protocolos. Diagramas que muestran rutas de datos y relaciones lógicas entre dispositivos, normalmente con flechas para indicar el sentido del tráfico.

- ##### Topology diagrams:
  
  Es una representación gráfica que muestra la estructura y conexiones de una red. Sirve para entender la ubicación de los dispositivos, la forma en que están enlazados y cómo circulan los datos.
  
  - **Dispositivos** (*end devices* como PCs, impresoras, teléfonos IP).
  
  - **Dispositivos intermedios** (routers, switches, puntos de acceso).
  
  - **Medios de conexión** (cables, enlaces inalámbricos).
  
  - **Símbolos estandarizados** para identificar cada elemento.

- ##### Networks of many sizes:
  
  Son las redes clasificadas por su tamaño y alcance geográfico.  
  Van desde redes muy pequeñas (en una casa) hasta redes enormes que cubren el planeta entero (Internet).
  
  ###### Tipos principales
  
  1. **LAN (Local Area Network)**
     
     - **Alcance:** Pequeño, como una casa, oficina o escuela.
     
     - **Ejemplo:** Red Wi-Fi de una biblioteca.
  
  2. **WAN (Wide Area Network)**
     
     - **Alcance:** Muy grande, conecta varias redes LAN a través de ciudades, países o continentes.
     
     - **Ejemplo:** Internet.
  
  3. **MAN (Metropolitan Area Network)**
     
     - **Alcance:** Cubre un área de ciudad o metropolitana.
     
     - **Ejemplo:** Red de cámaras de seguridad de toda una ciudad.
  
  4. **PAN (Personal Area Network)**
     
     - **Alcance:** Muy pequeño, pocos metros alrededor de una persona.
     
     - **Ejemplo:** Conexión Bluetooth entre un celular y unos audífonos.
  
  5. **SAN (Storage Area Network)**
     
     - **Alcance:** Red especializada para almacenamiento y acceso rápido a datos.
     
     - **Ejemplo:** Red de servidores de una empresa para copias de seguridad.

- ##### LANs and WANs:
  
  *LAN*: Red que conecta dispositivos en un área geográfica pequeña, como una casa, oficina o escuela.
  
  **Características:**
  
  - Propiedad privada (normalmente administrada por el dueño del lugar).
  
  - Alta velocidad y baja latencia.
  
  - Generalmente usa cables Ethernet o Wi-Fi.
    
    **Ejemplo:**  La red de computadoras y Wi-Fi en una oficina.
    
    
  
  *WAN*: Red que cubre un área muy grande, conectando múltiples LANs a través de ciudades, países o continentes.
  
  **Características:**
  
  - Generalmente administrada por proveedores de servicios (ISP).
  
  - Velocidad más baja que una LAN debido a la distancia.
  
  - Usa enlaces de fibra óptica, satélite o cables submarinos.
    
    **Ejemplo:** Internet, que conecta millones de redes LAN en todo el mundo.

| Característica | LAN                        | WAN                              |
|:--------------:| -------------------------- | -------------------------------- |
| Alcance        | Pequeño (edificio, campus) | Muy grande (países, continentes) |
| Propietario    | Privado                    | ISP u organizaciones grandes     |
| Velocidad      | Alta                       | Menor que LAN                    |
| Ejemplo        | Wi-Fi de una casa          | Internet                         |




