# Módulo 4  - Capa física

---

## Contenido

- **Propósito de la capa física:** Describa el propósito y las funciones de la capa física en la red.
- **Características de la capa física:** Describa las características de la capa física.
- **Cableado de cobre:** Identifique las características básicas del cableado de cobre.
- **Cableado UTP:** Explique cómo se utiliza el cable UTP en las redes Ethernet. (Este submodulo esta integrado en el de **Cableado de cobre**)
- **Cableado de fibra óptica:** Describir el cableado de fibra óptica y sus ventajas principales sobre otros medios.
- **Medios inalámbricos:** Conecte dispositivos utilizando medios conectados por cable e inalámbricos.

---

## Propósito de la capa física

### Conexión física

Para que haya comunicación en red, primero se necesita conexión a una red local, ya sea por cable o de forma inalámbrica.

- **Red cableada**: los dispositivos se conectan mediante cables a un switch, transmitiendo datos por el medio físico.

- **Red inalámbrica**: los dispositivos usan ondas de radio y se conectan a un punto de acceso o router.

Las empresas suelen usar ambas opciones según las necesidades y ventajas de cada una.

Estos son los componentes de un punto de acceso:

1. Las antenas inalámbricas (Estas están integradas dentro de la versión del router que se muestra en la figura anterior).
2. Varios puertos de switch de Ethernet
3. Un puerto de internet

<img src="https://www.netacad.com/content/itn/1.0/courses/content/m4/es-XL/assets/4.1.1-image-1.jpg" title="" alt="" data-align="center">

### Conexión por cable al router inalámbrico

Las **tarjetas de interfaz de red (NIC)** permiten que un dispositivo se conecte a la red:

- **NIC Ethernet**: para conexión por cable.

- **NIC WLAN**: para conexión inalámbrica.

Algunos dispositivos incluyen solo un tipo (ej. impresora con Ethernet, tablet o smartphone con WLAN), mientras que otros pueden tener ambos.

### La capa física

La capa física del modelo OSI se encarga de transmitir los bits de una trama de la capa de enlace de datos a través del medio de red. Codifica la trama en señales eléctricas, ópticas o de radio y las envía una a una. En el destino, la capa física recibe esas señales, las convierte nuevamente en bits y entrega la trama completa a la capa de enlace de datos.

---

## Características de la capa física

La capa física se encarga del hardware de la red (circuitos, medios y conectores), por lo que requiere estándares internacionales definidos por diferentes organismos. Estos regulan aspectos como cableado, señalización y codificación.

Organizaciones destacadas:

- **ISO**: Organización Internacional para la Estandarización.

- **TIA/EIA**: Asociación de las Industrias de Telecomunicaciones y Asociación de Industrias Electrónicas.

- **ITU**: Unión Internacional de Telecomunicaciones.

- **ANSI**: Instituto Nacional Estadounidense de Estándares.

- **IEEE**: Instituto de Ingenieros Eléctricos y Electrónicos.

- **FCC**: Comisión Federal de Comunicaciones (EE. UU.).

- **ETSI**: Instituto Europeo de Estándares de Telecomunicaciones.

- **CSA**: Asociación de Normas Canadienses.

- **CENELEC**: Comité Europeo de Normalización Electrotécnica.

- **JSA/JIS**: Asociación de Normas Japonesas.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-08-10-21-51-image.png" title="" alt="" data-align="center">

### Componentes físicos

Son todos los elementos de hardware que permiten transmitir los bits a través del medio físico. 
Incluyen:

- NIC (tarjeta de red)

- Cables (UTP, fibra óptica, coaxial)

- Conectores (RJ-45, puertos ópticos, etc.)

- Interfaces y puertos en dispositivos como routers o switches.

Son las “partes tangibles” que permiten que los datos viajen de un dispositivo a otro.

---

### Codificación

Es el método para transformar los bits en un patrón reconocible que tanto el emisor como el receptor entiendan.

- Se usan códigos predefinidos para representar los 0 y 1.

- Ejemplo: Codificación Manchester (usada en Ethernet 10 Mbps):
  
  - `0` = transición de alto → bajo.
  
  - `1` = transición de bajo → alto.

- A mayores velocidades se requieren esquemas más eficientes como 4B/5B (100BASE-TX) o 8B/10B (1000BASE-T).

Es como un “idioma digital” que traduce los bits a un formato que pueda viajar y ser entendido en el otro extremo.

---

### Señalización

Se refiere a cómo físicamente se representan los 0 y 1 en el medio de transmisión (eléctrico, óptico o inalámbrico).

- Puede ser un cambio de voltaje (en cobre)

- Un pulso de luz (en fibra)

- Una onda electromagnética (en Wi-Fi)
  
  Ejemplo: Un pulso largo = 1, un pulso corto = 0.

Es la forma física real que toma la señal (voltajes, luz, ondas) para transportar la información digital.



### Ancho de banda

El ancho de banda es la capacidad de un medio para transportar datos en un tiempo determinado, expresado en kbps, Mbps o Gbps. No se refiere a la velocidad de los bits (que viajan a la velocidad de la electricidad), sino a la cantidad de bits transmitidos por segundo. Su valor práctico depende de las propiedades del medio físico, la tecnología de señalización y detección, así como de limitaciones físicas y tecnológicas.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-00-35-55-image.png" title="" alt="" data-align="center">

La **terminología del ancho de banda** se entiende a partir de tres conceptos clave:

- **Latencia**: Tiempo que tardan los datos en viajar de un punto a otro, incluyendo retrasos. Un enlace lento en la ruta puede generar un cuello de botella en toda la red.

- **Rendimiento**: Cantidad real de bits transferidos en un período de tiempo. Suele ser menor al ancho de banda teórico, ya que depende del tráfico, tipo de datos y número de dispositivos intermedios.

- **Capacidad de transferencia útil (Goodput)**: Datos efectivamente utilizables transmitidos en un tiempo determinado. Se obtiene restando al rendimiento la sobrecarga de protocolos (establecimiento de sesiones, acuses de recibo, encapsulación y retransmisiones).

Conclusión: **Ancho de banda ≥ Rendimiento ≥ Goodput**.

---

## Cableado de cobre

El cableado de cobre es el medio más común en redes por ser económico, fácil de instalar y con baja resistencia eléctrica, aunque presenta limitaciones de distancia e interferencia.

Los datos viajan como impulsos eléctricos que sufren **atenuación** al recorrer largas distancias, lo que obliga a respetar límites según los estándares. Además, el cobre es sensible a:

- **Interferencia electromagnética (EMI) y de radiofrecuencia (RFI):** Causada por ondas de radio, motores eléctricos, luces fluorescentes, etc., que pueden distorsionar la señal.

- **Crosstalk (diafonía):** Interferencia entre hilos adyacentes debido a campos eléctricos o magnéticos, provocando fugas de señales, como ocurre en llamadas telefónicas donde se escucha otra conversación.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-00-48-21-image.png" title="" alt="" data-align="center">

Para reducir las interferencias en el **cableado de cobre**, se aplican distintas técnicas:

- **Blindaje metálico y conexión a tierra:** Protege contra la **EMI** y la **RFI** al bloquear señales externas que puedan distorsionar la transmisión.

- **Trenzado de pares de hilos:** Cancela el **crosstalk** al compensar los campos eléctricos y magnéticos entre hilos adyacentes.



### Tipos de cableado de cobre

---

#### 1. Par trenzado no blindado (UTP)

El cable UTP es el más usado en LAN porque es económico, pequeño y fácil de instalar. Está formado por cuatro pares de hilos codificados por colores, trenzados y recubiertos con plástico.

A diferencia del STP, no usa blindaje metálico contra **EMI** (interferencia electromagnética) y **RFI** (interferencia de radiofrecuencia). En su lugar, se basa en dos técnicas de diseño:

1. **Anulación**: Los dos hilos de un circuito generan campos magnéticos opuestos que se cancelan entre sí, reduciendo el efecto de interferencias externas.

2. **Variación de vueltas por par**: Cada par tiene un número diferente de trenzas por metro, lo que evita que los pares interfieran entre sí (**crosstalk**).

Además, se rige por la norma TIA/EIA-568, que define aspectos como tipos de cables, longitudes, conectores, terminación y pruebas. 
El **IEEE** establece sus características eléctricas y clasifica los cables por categorías según su capacidad de transmisión:

- **Cat. 3**: Voz y datos básicos.

- **Cat. 5**: 100 Mbps (FastEthernet).

- **Cat. 5e**: 1000 Mbps (Gigabit Ethernet), mínima aceptable hoy.

- **Cat. 6**: Hasta 10 Gbps, recomendada para nuevas instalaciones.

- **Cat. 6a**: Mejora de la 6.

- **Cat. 7**: Hasta 10 Gbps.

- **Cat. 8**: Hasta 40 Gbps.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-14-56-image.png" title="" alt="" data-align="center">

##### Conectores RJ-45 para UTP

<img src="https://www.netacad.com/content/itn/1.0/_assets/media/2dd9fd50-1c25-11ea-a010-eb2108469056/2dd9fd55-1c25-11ea-81a0-ffc2c49b96bc.jpg" title="" alt="" data-align="center">

##### Socket RJ-45 para UTP

<img src="https://www.netacad.com/content/itn/1.0/_assets/media/2dda2460-1c25-11ea-a010-eb2108469056/2dda2464-1c25-11ea-81a0-ffc2c49b96bc.jpg" title="" alt="" data-align="center">

##### Cable UTP mal terminado

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-17-00-image.png" title="" alt="" data-align="center">

##### Cable UTP correctamente terminado

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-17-23-image.png" title="" alt="" data-align="center">

Los **cables UTP** pueden armarse con diferentes convenciones de conexión en el conector **RJ-45**:

- **Cable directo (Ethernet straight-through):** Más común; conecta **host–switch** o **switch–router**.

- **Cable cruzado (Ethernet crossover):** Conecta **dispositivos similares** (host–host, switch–switch, router–router). Hoy en día casi no se usa por **Auto-MDIX**.

- **Cable rollover (propietario de Cisco):** conecta una **PC al puerto de consola** de routers o switches.

**Auto-MDIX** permite que los equipos de red ajusten automáticamente la conexión, funcionando con cualquier cable Ethernet (directo o cruzado) sin importar el tipo.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-24-54-image.png" title="" alt="" data-align="center">

<img title="" src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-25-08-image.png" alt="" data-align="center">

---

#### 2. Par trenzado blindado (STP)

- Ofrece mayor protección contra ruido que el UTP.

- Es más costoso y difícil de instalar.

- También utiliza conectores RJ-45, pero requiere conectores blindados especiales para aprovechar el blindaje.

- Combina:
  
  - **Blindaje metálico:** Protege contra **EMI** (interferencia electromagnética) y **RFI** (interferencia de radiofrecuencia).
  
  - **Trenzado de hilos:** Reduce el crosstalk.

- Cada par de hilos tiene su propio blindaje de hoja metálica, y el conjunto está recubierto por una malla tejida o lámina metálica.

- Requiere conexión a tierra adecuada, de lo contrario el blindaje puede actuar como antena y captar interferencias.

---

#### 3. Cable coaxial

- Su nombre proviene de que tiene dos conductores en el mismo eje.

- Estructura:
  
  - **Conductor de cobre central:** Transporta la señal.
  
  - **Aislamiento plástico flexible** alrededor del conductor.
  
  - **Malla de cobre tejida o lámina metálica:** Funciona como segundo hilo y blindaje contra EMI.
  
  - **Revestimiento externo:** Protege contra daños físicos menores.

- Usa distintos conectores: **BNC**, **tipo N** y **tipo F**.

- Aunque el UTP reemplazó al coaxial en Ethernet moderna, aún se utiliza en:
  
  - **Instalaciones inalámbricas**: Conecta antenas con equipos de radio y transporta energía RF (radiofrecuencia).
  
  - **Internet por cable**: Combina coaxial en instalaciones del cliente con fibra óptica en el proveedor.

---

- **UTP** es el más usado por su bajo costo y facilidad de instalación.

- **STP** se utiliza en entornos con alta interferencia, aunque es más caro.

- **Coaxial** hoy tiene un uso más específico en antenas y conexiones de Internet por cable, pero ya no en LAN modernas.

---

## Cableado de fibra óptica

La fibra óptica, aunque más costosa que el cobre, permite transmitir datos a grandes distancias con mayor ancho de banda, mínima atenuación y sin interferencias. Está compuesta por hilos de vidrio que transportan impulsos de luz, funcionando como un tubo reflectante que garantiza una transmisión eficiente y confiable.



### Tipos de fibra óptica

Existen**dos tipos principales de medios de fibra óptica:

1. **Fibra multimodo (MMF)**
   
   - Núcleo más grande.
   
   - Usa **LEDs** como emisores de luz.
   
   - La luz viaja en varios ángulos o modos dentro del núcleo.
   
   - Es más económica y se utiliza en redes LAN o distancias cortas.
   
   - Alcance hasta 550 m con velocidades de hasta 10 Gb/s.
   
   - Tiene mayor dispersión, lo que provoca pérdida de señal a distancias largas.

2. **Fibra monomodo (SMF)**
   
   - Núcleo muy pequeño.
   
   - Usa láser como emisor de luz.
   
   - La luz viaja en un solo rayo recto.
   
   - Se utiliza en largas distancias** (cientos de km) como telefonía y TV por cable.
   
   - Su alcance puede cubrir enlaces de cientos de kilómetros.
   
   - Tiene muy baja dispersión, lo que mantiene la señal fuerte y clara a grandes distancias.

**MMF (multimodo)**: Más barata, corta distancia, más dispersión.

**SMF (monomodo)**: Más cara, larga distancia, menos dispersión.

---

El cableado de fibra óptica se usa principalmente en:

- **Redes empresariales**: Para cableado backbone e interconexión de dispositivos.

- **Fibra hasta el hogar (FTTH)**: Brinda servicios de banda ancha a hogares y pequeñas empresas.

- **Redes de larga distancia**: Conecta países y ciudades mediante proveedores de servicio.

- **Redes submarinas**: Ofrecen soluciones de alta velocidad y capacidad a nivel transoceánico.

---

Los conectores de fibra óptica permiten unir y desconectar fibras de forma sencilla y segura, garantizando una buena transmisión de datos. Existen varios tipos, como los conectores **ST, SC y LC**, que se utilizan según las necesidades de cada red.

- **ST (Straight Tip / Punta Directa):** 
  Conector de acoplamiento tipo bayoneta, común en redes más antiguas y entornos empresariales.

- **SC (Subscriber Connector / Suscriptor):** 
  Conector de inserción y extracción sencilla (push-pull), muy usado en telecomunicaciones y redes de datos.

- **LC (Lucent Connector) Simplex:** 
  Conector compacto de tipo push-pull, diseñado para equipos de alta densidad; conecta una sola fibra.

- **LC Multimodo Dúplex:** 
  Versión doble del LC, permite transmisión y recepción simultánea en dos fibras, ideal para enlaces dúplex.

Por último, los cables de conexión de fibra óptica interconectan dispositivos y se diferencian por colores: amarillo para monomodo y naranja o aqua para multimodo.

#### Cable de conexión multimodo SC-SC

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-44-38-image.png" title="" alt="" data-align="center">

#### Cable de conexión monomodo LC-LC

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-45-15-image.png" title="" alt="" data-align="center">

#### Cable de conexión multimodo ST-LC

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-45-48-image.png" title="" alt="" data-align="center">

#### Cable de conexión monomodo SC-ST

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-46-26-image.png" title="" alt="" data-align="center">

**Cuadro comparativo entre cobre y fibra**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-15-01-47-40-image.png" title="" alt="" data-align="center">

---

## Medios inalámbricos

Los medios inalámbricos permiten la conexión a la red sin cables, usando ondas electromagnéticas (radio y microondas) para transmitir datos. Son la opción con mayor movilidad, razón por la cual hoy son el método más usado en redes domésticas y cada vez más en entornos empresariales.

Sin embargo, presentan algunas limitaciones importantes:

- **Cobertura:** Funcionan bien en espacios abiertos, pero muros, estructuras o el terreno pueden reducir su alcance.

- **Interferencia:** Son vulnerables a dispositivos como teléfonos inalámbricos, microondas o luces fluorescentes.

- **Seguridad:** Al no requerir un medio físico, es más fácil que usuarios no autorizados intenten acceder, por lo que la seguridad debe reforzarse.

- **Medio compartido:** En las WLAN solo un dispositivo transmite o recibe a la vez; si muchos se conectan, el ancho de banda disponible se reparte.

Por estas razones, aunque el WiFi gana popularidad, los cables de cobre y fibra óptica siguen siendo los más usados en la infraestructura de red (routers, switches, etc.) por su mayor estabilidad y capacidad.



### Tipos de medios inalámbricos

Los estándares inalámbricos regulan cómo se transmiten y reciben los datos a través del aire, abarcando aspectos de la capa física (codificación de señales, frecuencias, potencia, antenas) y de la capa de enlace de datos (cómo los dispositivos acceden y comparten el medio).

**Principales estándares:**

- **Wi-Fi (IEEE 802.11):** 
  Tecnología para redes LAN inalámbricas (WLAN). Usa el protocolo CSMA/CA, donde la tarjeta de red escucha antes de transmitir para evitar colisiones. Es el estándar más usado en hogares y empresas.

- **Bluetooth (IEEE 802.15):** 
  Tecnología para redes personales inalámbricas (WPAN). Se basa en el emparejamiento de dispositivos y funciona en distancias cortas (1 a 100 m).

- **WiMAX (IEEE 802.16):** 
  Tecnología de acceso inalámbrico de largo alcance, usando topología punto a multipunto para ofrecer ancho de banda similar al de conexiones fijas.

- **Zigbee (IEEE 802.15.4):** 
  Diseñado para bajo consumo de energía, baja velocidad de datos y corto alcance. Se usa en IoT e industria (sensores, interruptores, dispositivos médicos).



### LAN inalámbrica

Una WLAN (Wireless LAN) permite que los dispositivos se conecten a la red sin cables, usando radiofrecuencia. Para su funcionamiento necesita:

- **Punto de acceso inalámbrico (AP):** 
  Dispositivo que recibe y concentra las señales inalámbricas de los usuarios, conectándolas con la red cableada (Ethernet). En casas y pequeñas empresas, suele venir integrado en los **routers inalámbricos**, que combinan router, switch y AP en un solo equipo.

- **Adaptador NIC inalámbrico:** 
  Tarjeta o componente del dispositivo (computadora, móvil, impresora, etc.) que le da la capacidad de conectarse a la red Wi-Fi.

Con el tiempo surgieron varios estándares WLAN basados en Ethernet (IEEE 802.11), por lo que al comprar equipos inalámbricos se debe verificar su compatibilidad e interoperabilidad.
