# Introducción al módulo 3

---

## Reglas

#### Fundamentos de las Comunicaciones

Las redes pueden variar en tamaño y complejidad. No basta con tener una conexión, los dispositivos deben ponerse de acuerdo en “cómo” comunicarse.

Hay tres elementos en toda comunicación:

- Habrá una fuente (emisor).

- Habrá un destino (receptor).

- Habrá un canal (medio) que proporciona la ruta por la cual ocurre la comunicación.

#### Protocolos de Comunicación

- Todas las comunicaciones están regidas por protocolos.

- Los protocolos son las reglas que seguirán las comunicaciones.

- Estas reglas variarán dependiendo del protocolo.

#### Establecimiento de Reglas

- Las personas deben usar reglas o acuerdos establecidos para guiar la conversación.

- El primer mensaje es difícil de leer porque no está formateado correctamente. El segundo muestra el mensaje con el formato adecuado.

#### Establecimiento de Reglas (Cont.)

Los protocolos deben tener en cuenta los siguientes requisitos:

- Un emisor y un receptor identificados

- Un lenguaje y gramática comunes

- Velocidad y sincronización de la entrega

- Requisitos de confirmación o acuse de recibo

#### Requisitos de los Protocolos de Red

Los protocolos comunes de computadoras deben estar en acuerdo e incluir los siguientes requisitos:

- Codificación de mensajes

- Formato y encapsulación de mensajes

- Tamaño de los mensajes

- Sincronización de los mensajes

- Opciones de entrega de mensajes

---

##### Codificación de Mensajes

- La codificación es el proceso de convertir la información en otra forma aceptable para su transmisión.

- La decodificación revierte este proceso para interpretar la información.

##### Formato y Encapsulación de Mensajes

- Cuando se envía un mensaje, este debe usar un formato o estructura específica.

- Los formatos de los mensajes dependen del tipo de mensaje y del canal que se utilice para entregarlo.

##### Tamaño del Mensaje

La codificación entre hosts debe estar en un formato apropiado para el medio.

- Los mensajes enviados a través de la red se convierten en bits.

- Los bits se codifican en un patrón de luz, sonido o impulsos eléctricos.

- El host de destino debe decodificar las señales para interpretar el mensaje.

##### Sincronización de Mensajes

La sincronización de los mensajes incluye lo siguiente:

- **Control de flujo**: Administra la velocidad de la transmisión de datos y define cuánta información se puede enviar y a qué velocidad puede entregarse.

- **Tiempo de espera de respuesta**: Gestiona cuánto tiempo espera un dispositivo cuando no recibe respuesta del destino.

- **Método de acceso**: Determina cuándo alguien puede enviar un mensaje.

- Puede haber varias reglas que regulen problemas como las **colisiones**. Esto ocurre cuando más de un dispositivo envía tráfico al mismo tiempo y los mensajes se corrompen.

- Algunos protocolos son proactivos e intentan prevenir las colisiones; otros son reactivos y establecen un método de recuperación después de que ocurre la colisión.

##### Opciones de Entrega de Mensajes

La entrega de mensajes puede realizarse mediante uno de los siguientes métodos:

- **Unicast** – comunicación de uno a uno.

- **Multicast** – comunicación de uno a muchos, normalmente no a todos.

- **Broadcast** – comunicación de uno a todos.

**Nota:** Los *broadcasts* se utilizan en redes IPv4, pero no son una opción en IPv6. Más adelante también veremos **Anycast** como una opción adicional de entrega en IPv6.

---

#### Una Nota Sobre el Ícono de Nodo

- Los documentos pueden usar el ícono de nodo, típicamente un **círculo**, para representar a todos los dispositivos.

- La figura ilustra el uso del ícono de nodo para mostrar las **opciones de entrega**.

---

## Protocolos

#### Visión General de los Protocolos de Red

Los protocolos de red definen un conjunto común de reglas.

- Pueden implementarse en los dispositivos mediante:
  
  - **Software**
  
  - **Hardware**
  
  - **Ambos**

- Cada protocolo tiene su propio:
  
  - **Función**
  
  - **Formato**
  
  - **Reglas**

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-01-08-57-41-image.png" title="" alt="" data-align="center">

#### Funciones de los Protocolos de Red

- Los dispositivos usan protocolos acordados para poder comunicarse.

- Los protocolos pueden tener una o varias funciones.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-01-08-58-37-image.png" title="" alt="" data-align="center">

#### Interacción de Protocolos

- Las redes requieren el uso de varios protocolos.

- Cada protocolo tiene su propia función y formato.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-01-08-59-28-image.png" title="" alt="" data-align="center">

---

## Protocolos de suites

#### Suites de Protocolos de Red

Los protocolos deben poder trabajar junto con otros protocolos.

**Suite de protocolos:**

- Es un conjunto de protocolos interrelacionados necesarios para realizar una función de comunicación.

- Son conjuntos de reglas que trabajan en conjunto para ayudar a resolver un problema.

Los protocolos se organizan en términos de capas:

- **Capas superiores** – se encargan de los aspectos más cercanos al usuario y la aplicación.

- **Capas inferiores** – se ocupan del movimiento de los datos y de proporcionar servicios a las capas superiores.



#### Evolución de las Suites de Protocolos

Existen varias suites de protocolos:

- **Suite de Protocolo de Internet o TCP/IP** – La suite de protocolos más común, mantenida por el *Internet Engineering Task Force (IETF)*.

- **Protocolos de Interconexión de Sistemas Abiertos (OSI)** – Desarrollados por la *International Organization for Standardization (ISO)* y la *International Telecommunications Union (ITU)*.

- **AppleTalk** – Suite propietaria lanzada por Apple Inc.

- **Novell NetWare** – Suite propietaria desarrollada por Novell Inc.

<img title="" src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-09-01-09-02-04-image.png" alt="" data-align="center">

#### Ejemplo de Protocolo TCP/IP

- Los protocolos TCP/IP operan en las capas de **aplicación**, **transporte** e **internet**.

- Los protocolos de capa de acceso a la red más comunes en redes LAN son Ethernet y WLAN (red de área local inalámbrica).



#### Suite de Protocolos TCP/IP

- TCP/IP es la suite de protocolos utilizada por Internet e incluye muchos protocolos.

**Características de TCP/IP:**

- Es una suite de protocolos de estándar abierto, disponible libremente para el público y que puede ser utilizada por cualquier fabricante.

- Es una suite de protocolos basada en estándares, respaldada por la industria de redes y aprobada por organizaciones de estandarización para garantizar la interoperabilidad.



#### Proceso de Comunicación TCP/IP

- Un servidor web encapsula y envía una página web a un cliente.

- El cliente desencapsula la página web para que pueda ser visualizada en el navegador.
