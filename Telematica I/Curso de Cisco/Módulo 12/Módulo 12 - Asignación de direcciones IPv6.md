# Módulo 12 - Asignación de direcciones IPv6

---

## Contenido

- **Probremas con IPv4:** Explica la necesidad de la asignación de direcciones IPv6.

- **Direccionamiento dinámico para las GUAs de IPv6:** Explica cómo se representan las direcciones IPv6.

- **Tipos de direcciones IPv6:** Compara los tipos de direcciones de red IPv6.

- **Configuración estática de GUA y LLA:** Explica cómo configurar la unidifusión global estática y direcciones IPv6 locales de vínculo.

- **Direccionamiento dinámico para GUA IPv6:** Explica cómo configurar las direcciones global unicast de forma dinámica.

- **Direccionamiento dinámico para LLA de IPv6:** Configura dinámicamente direcciones locales de vínculo.

- **Direcciones IPv6 de multidifusión:** Identifica direcciones IPv6.

- **División de subredes de una red IPv6:** Implementación de un esquema de direccionamiento IPv6 dividido en subredes.

---

### Probremas con IPv4

IPv4 se está quedando sin direcciones, por lo que se creó IPv6 como su sucesor. IPv6 usa direcciones de 128 bits, lo que permite un espacio mucho más grande (340 undecillones de direcciones). Además de más direcciones, IPv6 corrige limitaciones de IPv4 e incluye mejoras, como ICMPv6, que permite resolución de direcciones y configuración automática de manera más eficiente. El agotamiento de IPv4, especialmente con el crecimiento de Internet en África, Asia y otras regiones, motivó la migración a IPv6.

*Fechas de agotamiento de las direcciones IPv4*

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-29-17-25-10-image.png" title="" alt="" data-align="center">

IPv4 tiene un límite de ~4.300 millones de direcciones, y aunque las direcciones privadas y NAT ayudaron a retrasar el agotamiento, NAT presenta problemas de latencia y limita las comunicaciones entre pares. Con el aumento de dispositivos móviles, los principales proveedores de telefonía e Internet han adoptado IPv6, alcanzando altos porcentajes de tráfico en esta versión.

Además, el crecimiento del **Internet de las cosas (IoT)**, con dispositivos como autos, electrodomésticos y equipos biomédicos conectados, hace que el espacio limitado de IPv4 sea insuficiente. Por estas razones, la transición a IPv6 es necesaria para soportar la expansión de Internet y nuevas tecnologías.

#### Coexistencia de IPv6 e IPv6

No hay una fecha límite para la adopción de IPv6; IPv4 e IPv6 coexistirán durante varios años. El IETF desarrolló protocolos y herramientas para facilitar la migración, y las técnicas de transición se pueden clasificar en tres categorías principales:

- **Dual-stack:** Permite que un dispositivo use IPv4 e IPv6 al mismo tiempo. Así, la red puede conectarse a Internet usando cualquiera de los dos protocolos, y los dispositivos pueden acceder a contenido en IPv6 sin problemas.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-29-17-29-32-image.png" title="" alt="" data-align="center">

- **Tunelización:** Permite enviar paquetes IPv6 a través de redes que solo entienden IPv4. Para hacerlo, el paquete IPv6 se “mete” dentro de un paquete IPv4, como si fuera una caja dentro de otra caja. De esta manera, el paquete puede viajar por la red IPv4 y llegar a su destino, donde se extrae y se entrega como paquete IPv6 normal.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-29-17-30-39-image.png" title="" alt="" data-align="center">

- **Traducción:** NAT64 permite que los dispositivos que usan IPv6 hablen con dispositivos que usan IPv4. Funciona traduciendo los paquetes: un paquete IPv6 se convierte en IPv4 para viajar por la red, y un paquete IPv4 se convierte en IPv6 cuando regresa, permitiendo la comunicación entre ambos tipos de redes.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-29-17-31-50-image.png" title="" alt="" data-align="center">

*Nota: La tunelizacion y la traduccion son para la transicion a IPv6 nativo y solo deben usarse cuando sea necesario. El objetivo debe ser las comunicaciones IPv6 nativas de origen a destino.*

---

### Direccionamiento Dinámico para las GUAs de IPv6

Las direcciones IPv6 tienen una longitud de 128 bits y se escriben como una cadena de 32 dígitos hexadecimales, donde cada 4 bits equivalen a un dígito hexadecimal. No distinguen entre mayúsculas y minúsculas, por lo que pueden escribirse de ambas formas. Estas direcciones son mucho más amplias que las IPv4, lo que hace improbable que se agoten.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-11-18-24-image.png" title="" alt="" data-align="center">

El formato preferido de una dirección IPv6 se escribe como:

`x:x:x:x:x:x:x:x`

Cada “x” representa un hexteto, es decir, un grupo de 16 bits o cuatro dígitos hexadecimales (por ejemplo, `2001`, `0db8`, `abcd`, etc.).

En total, una dirección IPv6 contiene ocho hextetos que equivalen a 128 bits o 32 dígitos hexadecimales.

Este formato muestra la dirección completa sin abreviaciones, pero no es el método más práctico para escribirla, ya que existen dos reglas de abreviación que permiten reducir su longitud.

**Ejemplos de formato preferido:**

`2001 : 0db8 : 0000 : 1111 : 0000 : 0000 : 0000: 0200`
`2001 : 0db8 : 0000 : 00a3 : abcd : 0000 : 0000: 1234` 
`2001 : 0db8 : 000a : 0001 : c012 : 9aff : fe9a: 19ac`
`2001 : 0db8 : aaaa : 0001 : 0000 : 0000 : 0000: 0000` 
`fe80 : 0000 : 0000 : 0000 : 0123 : 4567 : 89ab: cdef` 
`fe80 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0001` 
`fe80 : 0000 : 0000 : 0000 : c012 : 9aff : fe9a: 19ac` 
`fe80 : 0000 : 0000 : 0000 : 0123 : 4567 : 89ab: cdef` 
`0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0001` 
`0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0000`

#### Regla 1 - Omitir los ceros iniciales

La primera regla de abreviación de direcciones IPv6 permite omitir los ceros iniciales en cada hexteto.

Por ejemplo:

- `01ab` → `1ab`

- `09f0` → `9f0`

- `0a00` → `a00`

- `00ab` → `ab`

Solo se pueden eliminar los ceros al inicio del hexteto, no los ceros finales, ya que esto podría cambiar el valor de la dirección y causar ambigüedad.

| Tipo                    | Formato                                 |
| ----------------------- | --------------------------------------- |
| **Recomendado**         | 2001:0db8:0000:1111:0000:0000:0000:0200 |
| **Sin ceros iniciales** | 2001:db8:0:1111:0:0:0:200               |
| **Recomendado**         | 2001:0db8:0000:00a3:ab00:0ab0:00ab:1234 |
| **Sin ceros iniciales** | 2001:db8:0:a3:ab00:ab0:ab:1234          |
| **Recomendado**         | 2001:0db8:000a:0001:c012:9eff:fe90:0001 |
| **Sin ceros iniciales** | 2001:db8:a:1:c012:9eff:fe90:1           |
| **Recomendado**         | 2001:0db8:aaaa:0001:0000:0000:0000:0000 |
| **Sin ceros iniciales** | 2001:db8:aaaa:1:0:0:0:0                 |
| **Recomendado**         | fe80:0000:0000:0000:0123:4567:89ab:cdef |
| **Sin ceros iniciales** | fe80:0:0:0:123:4567:89ab:cdef           |
| **Recomendado**         | fe80:0000:0000:0000:0000:0000:0000:0001 |
| **Sin ceros iniciales** | fe80:0:0:0:0:0:0:1                      |
| **Recomendado**         | 0000:0000:0000:0000:0000:0000:0000:0001 |
| **Sin ceros iniciales** | 0:0:0:0:0:0:0:1                         |
| **Recomendado**         | 0000:0000:0000:0000:0000:0000:0000:0000 |
| **Sin ceros iniciales** | 0:0:0:0:0:0:0:0                         |

#### Regla 2 - Dos puntos dobles

La segunda regla de abreviación en IPv6 permite usar doble punto (::) para reemplazar una sola secuencia continua de hextetos compuestos solo por ceros.

Por ejemplo: 
`2001:db8:cafe:1:0:0:0:1` → `2001:db8:cafe:1::1`

- El `::` solo puede usarse una vez por dirección, ya que usarlo más veces generaría ambigüedad.

- Se recomienda aplicar `::` en la cadena más larga de ceros; si hay dos de igual longitud, se usa en la primera.

Esta forma abreviada se conoce como formato comprimido, y se usa junto con la omisión de ceros iniciales para simplificar las direcciones IPv6.

| Tipo                      | Formato                                 |
| ------------------------- | --------------------------------------- |
| **Recomendado**           | 2001:0db8:0000:1111:0000:0000:0000:0200 |
| **Comprimido / espacios** | 2001:db8:0:1111:0:0:0:200               |
| **Comprimido**            | 2001:db8:0:1111::200                    |
| **Recomendado**           | 2001:0db8:0000:00a3:ab00:0ab0:00ab:0000 |
| **Comprimido / espacios** | 2001:db8:0:a3:ab00:ab0:ab::             |
| **Comprimido**            | 2001:db8:0:a3:ab00::                    |
| **Recomendado**           | 2001:0db8:aaaa:0001:0000:0000:0000:0000 |
| **Comprimido / espacios** | 2001:db8:aaaa:1::                       |
| **Comprimido**            | 2001:db8:aaaa:1::                       |
| **Recomendado**           | fe80:0000:0000:0000:0123:4567:89ab:cdef |
| **Comprimido / espacios** | fe80::123:4567:89ab:cdef                |
| **Comprimido**            | fe80::123:4567:89ab:cdef                |
| **Recomendado**           | fe80:0000:0000:0000:0000:0000:0000:0001 |
| **Comprimido / espacios** | fe80::1                                 |
| **Comprimido**            | fe80::1                                 |
| **Recomendado**           | 0000:0000:0000:0000:0000:0000:0000:0001 |
| **Comprimido / espacios** | ::1                                     |
| **Comprimido**            | ::1                                     |
| **Recomendado**           | 0000:0000:0000:0000:0000:0000:0000:0000 |
| **Comprimido / espacios** | ::                                      |
| **Comprimido**            | ::                                      |

----

### Tipos de direcciones IPv6

Existen tres tipos principales de direcciones IPv6:

1. **Unidifusión:** Identifica de forma única una interfaz en un dispositivo IPv6.

2. **Multidifusión:** Permite enviar un solo paquete a varios destinos simultáneamente.

3. **Difusión por proximidad(Anycast):** Asigna una dirección a varios dispositivos, pero el paquete se envía solo al más cercano con esa dirección.

A diferencia de IPv4, IPv6 no usa direcciones de difusión, aunque la multidifusión de todos los nodos cumple una función similar.

#### Longitud de prefijo IPv6

En IPv6, la longitud de prefijo cumple la misma función que el prefijo o máscara de subred en IPv4, pero sin usar la notación decimal punteada.

Se representa con notación de barra inclinada ( / ), indicando cuántos bits corresponden a la parte de red. 
Por ejemplo: 
`192.168.1.10/24` en IPv4 equivale a algo como `2001:db8::/64` en IPv6.

La longitud del prefijo puede ir de /0 a /128, y la recomendada para redes LAN y la mayoría de redes IPv6 es /64.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-11-43-24-image.png" title="" alt="" data-align="center">

Se recomienda encarecidamente utilizar un ID de interfaz de 64 bits para la mayoría de las redes. Esto se debe a que la autoconfiguración de direcciones sin estado (SLAAC) utiliza 64 bits para el Id. de interfaz. También facilita la creación y gestión de subredes.



#### Tipos de direcciones de unidifusion IPv6

Las direcciones IPv6 de unidifusión identifican de forma única una interfaz en un dispositivo habilitado para IPv6. 
Los paquetes enviados a una dirección de unidifusión son recibidos solo por esa interfaz específica. 
Al igual que en IPv4, las direcciones de origen deben ser de unidifusión, mientras que las de destino pueden ser unidifusión o multidifusión. 
Existen varios tipos de direcciones de unidifusión IPv6, según su alcance y propósito.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-11-46-39-image.png" title="" alt="" data-align="center">

Los dispositivos IPv6 suelen tener dos direcciones de unidifusión:

1. **Dirección de unidifusión global (GUA):**
   
   - Similar a una dirección pública IPv4.
   
   - Es única y enrutable en Internet.
   
   - Puede configurarse de forma manual o dinámica.

2. **Dirección local de enlace (LLA):**
   
   - Obligatoria en todos los dispositivos IPv6.
   
   - Permite la comunicación dentro del mismo enlace o subred.
   
   - No es enrutable fuera del enlace; los routers no reenvían paquetes con direcciones link-local.

#### Una nota sobre la dirección local única

Las direcciones locales únicas (ULA), del rango fc00::/7 a fdff::/7, se usan para redes internas y no son enrutable globalmente.

- Sirven para el direccionamiento local dentro de un sitio o entre pocos sitios.

- Se aplican a dispositivos que no necesitan acceso externo, como servidores internos o impresoras.

- No se traducen ni enrutan hacia Internet.

Aunque algunas redes usan direcciones privadas (como las de RFC 1918) para ocultarse del exterior, esto no sustituye las medidas de seguridad adecuadas recomendadas por el IETF.

#### IPv6 GUA

Las direcciones IPv6 de unidifusión global (GUA) son únicas y enrutable en Internet, equivalentes a las direcciones públicas IPv4.

- Son asignadas por la ICANN/IANA a los cinco RIR regionales.

- Actualmente, solo se asignan direcciones con los tres primeros bits “001”, es decir, dentro del rango 2000::/3.

- El primer dígito hexadecimal de estas direcciones suele comenzar con 2 o 3.

- Esto representa solo una pequeña parte del espacio total de direcciones IPv6.

*Nota: La dirección 2001:db8::/32 está reservada para documentación y ejemplos*.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-11-53-15-image.png" title="" alt="" data-align="center">

- **Direccion IPv6 con un prefijo de enrutamiento global /48 y un prefijo /64**

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-10-30-11-54-09-image.png)

GUA tiene 3 partes:

- Prefijo de routing global

- ID de subred

- ID de interfaz

#### Estructura IPv6 GUA

1. **Prefijo Global de Enrutamiento**

Es la parte de la dirección IPv6 que identifica la red globalmente, asignada por el proveedor de servicios (ISP).

- Es equivalente al prefijo de red pública en IPv4.

- Los ISP suelen asignar un prefijo /48 a sus clientes.

- Ejemplo:
  
  `2001:db8:acad::/48`
  
  Aquí los primeros 48 bits (2001:db8:acad) son el prefijo global, y los bits restantes son ceros.

- Este prefijo determina el tamaño disponible para crear subredes.
2. **ID de subred**

Es la parte de la dirección que separa la red global de la interfaz.

- En IPv6 no se necesitan pedir prestados bits del host como en IPv4.

- La ID de subred se usa para dividir internamente la red de una organización.

- Cuantos más bits tenga la ID de subred, más subredes pueden crearse.

**Ejemplo:**

- Si una empresa recibe un prefijo /32 y usa subredes /64, 
  → tiene 32 bits para ID de subred, 
  → lo que equivale a 4.300 millones de subredes, 
  → cada una con 18 quintillones de direcciones disponibles. 
  Es decir, una sola organización puede tener más subredes que direcciones IPv4 en todo el mundo.
3. **ID de Interfaz**

Equivale a la parte de host en IPv4, pero en IPv6 se llama ID de interfaz, porque un mismo dispositivo puede tener múltiples interfaces.

- Representa una interfaz individual dentro de una subred.

- Por recomendación, se usa una longitud de 64 bits para la ID de interfaz.

- Esto permite que los dispositivos con SLAAC (Stateless Address Autoconfiguration) creen automáticamente su propia dirección.

- Cada subred /64 puede tener hasta 18 quintillones de dispositivos.

**Importante:**

- En IPv6 sí pueden usarse las direcciones todo-0 y todo-1, ya que no existen direcciones de difusión (broadcast).

- La dirección todo-0 se reserva para la difusión por proximidad subred-router, por lo que solo debe asignarse a routers.

#### IPv6 LLA

Las direcciones locales de enlace (LLA) permiten la comunicación solo dentro de la misma red local o subred. 
No pueden usarse para enviar paquetes más allá de ese enlace, es decir, no son enrutable fuera de la red local.

**Características principales:**

- Toda interfaz IPv6 debe tener una dirección LLA, incluso si no tiene una dirección global.

- Las LLAs permiten que los dispositivos se comuniquen entre sí dentro del mismo enlace, e incluso con el router predeterminado.

- Se generan automáticamente por el sistema, sin necesidad de un servidor DHCPv6.

**Rango de direcciones:**

- Van desde `fe80::` hasta `febf::`

- Se representan con el prefijo `/10` (los primeros 10 bits son `1111 1110 10`).

**Ejemplo:** 
Un PC y una impresora en la misma red pueden comunicarse directamente usando sus direcciones locales de enlace, sin requerir direcciones globales ni conexión a Internet.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-15-58-05-image.png" title="" alt="" data-align="center">

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-15-58-31-image.png" title="" alt="" data-align="center">

**Usos principales de las LLA:**

1. Los enrutadores utilizan las LLAs de sus vecinos para intercambiar actualizaciones de enrutamiento.

2. Los hosts usan la LLA del enrutador local como su puerta de enlace predeterminada.

> En IPv6, normalmente la puerta de enlace predeterminada de los dispositivos es la LLA del router, no su dirección global (GUA).

**Formas de obtener una LLA:**

1. **Estática:** Configurada manualmente por el administrador.

2. **Dinámica:** Generada automáticamente por el dispositivo:
   
   - Puede usar un ID de interfaz aleatorio
   
   - El método EUI-64, que combina la dirección MAC del dispositivo con bits adicionales para formar el identificador.

---

### Configuración estática de GUA y LLA

#### Configuración de GUA estática en un router

**Direcciones GUA IPv6:** 
Son equivalentes a las direcciones públicas IPv4: globalmente únicas y enrutables en Internet IPv6. 
Permiten que dos dispositivos habilitados para IPv6 se comuniquen en la misma subred (vínculo).

**Similitud entre comandos IPv4 e IPv6 en Cisco IOS:** 
Los comandos de configuración y verificación son casi iguales; solo cambia el prefijo ip → ipv6.

**Ejemplo:**

- IPv4 → `ip address <ip-address> <subnet-mask>`

- IPv6 → `ipv6 address <ipv6-address>/<prefix-length>`
  
  > (Sin espacio entre la dirección y la longitud del prefijo)

🔹 **Ejemplo de subredes utilizadas:**

- `2001:db8:acad:1::/64`

- `2001:db8:acad:2::/64`

- `2001:db8:acad:3::/64`

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-16-02-39-image.png" title="" alt="" data-align="center">

El ejemplo muestra cómo asignar direcciones IPv6 globales unicast (GUA) a las interfaces de un router Cisco (R1). 
Se configuran tres interfaces distintas:

1. **GigabitEthernet 0/0/0**

2. **GigabitEthernet 0/0/1**

3. **Serial 0/1/0**

Cada una recibe una dirección IPv6 GUA con su correspondiente longitud de prefijo para permitir la comunicación en sus redes asignadas.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-16-03-55-image.png" title="" alt="" data-align="center">

#### Configuración de GUA estática en un host de Windows

Configurar una dirección IPv6 manualmente en un host es similar a hacerlo con IPv4. 
En el ejemplo, la puerta de enlace predeterminada de PC1 es la dirección **2001:db8:acad:1::1**, correspondiente a la interfaz GigabitEthernet del router R1. 
También puede usarse la dirección local de enlace (LLA) del router como puerta de enlace, lo cual es la práctica recomendada, aunque ambas opciones funcionan correctamente.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-16-05-17-image.png" title="" alt="" data-align="center">

Al igual que en IPv4, configurar direcciones IPv6 estáticas en cada cliente no es práctico en redes grandes. 
Por eso, se usa la asignación dinámica de direcciones IPv6, que permite que los dispositivos obtengan su dirección automáticamente sin intervención manual.

Existen dos métodos principales:

1. **SLAAC (Stateless Address Autoconfiguration)** → el dispositivo genera su propia dirección IPv6 usando la información que recibe del router, sin depender de un servidor DHCP.

2. **DHCPv6 con información de estado** → el servidor DHCPv6 asigna direcciones IPv6 y puede llevar un registro (estado) de qué dirección tiene cada dispositivo.

*Nota: En ambos casos, el LLA (Link-Local Address) del router se configura automáticamente como la puerta de enlace predeterminada, facilitando la comunicación dentro de la red.*

#### Configuración estática de una dirección de unidifusión local de enlace

Configurar una dirección local de enlace (LLA) manualmente permite asignar una dirección más fácil de identificar y recordar, lo cual resulta útil especialmente en enrutadores, ya que sus LLAs se usan como puertas de enlace predeterminadas y para enviar mensajes de enrutamiento.

Para configurarla manualmente, se usa el comando:

`ipv6 address <dirección-link-local> link-local`

La dirección debe comenzar con un valor dentro del rango **fe80 a febf**, que identifica a las direcciones locales de enlace.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-16-08-25-image.png" title="" alt="" data-align="center">

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-16-08-37-image.png" title="" alt="" data-align="center">

Las LLAs estáticas se configuran para que sean fáciles de reconocer y asociar con un router específico.

En el ejemplo, todas las interfaces del router R1 usan direcciones que comienzan con `fe80::1:n`, donde el “1” identifica al router y “n” cambia según la interfaz. 
Por ejemplo, si existiera un router R2, sus direcciones serían `fe80::2:1`, `fe80::2:2` y `fe80::2:3`.

Aunque es posible usar la misma LLA en todas las interfaces (siempre que sean únicas en su enlace), la buena práctica es asignar una diferente por interfaz para facilitar su identificación.

---

### Direccionamiento dinámico para GUA IPv6

#### Mensajes RS y RA

Los dispositivos IPv6 pueden obtener sus direcciones GUA dinámicamente mediante el Protocolo ICMPv6, sin necesidad de configurarlas manualmente.

Los routers IPv6 envían periódicamente mensajes de Anuncio de Enrutador (RA) —aproximadamente cada 200 segundos— a todos los dispositivos con IPv6 habilitado en la red. 
Además, cuando un host envía una Solicitud de Enrutador (RS), el router responde con un RA, proporcionando la información necesaria para que el host configure su dirección IPv6.

Entonces, los mensajes RA y RS permiten que los dispositivos se autoconfiguren dinámicamente en redes IPv6 sin intervención manual.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-17-45-53-image.png" title="" alt="" data-align="center">

Los mensajes RA (Router Advertisement) se envían desde las interfaces Ethernet de un router IPv6 para ayudar a los dispositivos de la red a configurarse automáticamente. 
Sin embargo, el enrutamiento IPv6 no está habilitado por defecto, por lo que debe activarse con el comando global:

`ipv6 unicast-routing`

Una vez habilitado, el router envía mensajes ICMPv6 RA que informan a los dispositivos sobre cómo obtener su dirección IPv6. 
Cada mensaje RA contiene:

- **Prefijo de red y su longitud** → indica a qué red pertenece el dispositivo.

- **Puerta de enlace predeterminada** → es la LLA (Link-Local Address) del router, usada como gateway.

- **Direcciones DNS y nombre de dominio** → información opcional para resolver nombres.

Existen tres métodos principales para que los dispositivos obtengan su configuración a partir de los mensajes RA:

1. **SLAAC (Stateless Address Autoconfiguration)** → El router proporciona toda la información necesaria (prefijo, longitud, puerta de enlace). El dispositivo se autoconfigura sin usar DHCPv6.

2. **SLAAC + DHCPv6 sin estado** → El router da los datos básicos (prefijo y gateway), pero el dispositivo obtiene información adicional (como DNS) desde un servidor DHCPv6 sin estado.

3. **DHCPv6 con estado (sin SLAAC)** → El router solo indica la puerta de enlace, y el dispositivo obtiene toda su configuración (dirección IPv6, DNS, etc.) desde un servidor DHCPv6 con estado.

El router IPv6 guía a los hosts sobre cómo autoconfigurarse, ya sea completamente por sí mismos (SLAAC), con ayuda parcial de DHCPv6, o totalmente a través de un servidor DHCPv6.

#### Método 1 - SLAAC

**SLAAC (Stateless Address Autoconfiguration)** es un método que permite a un dispositivo generar su propia dirección IPv6 global unicast (GUA) sin depender de un servidor DHCPv6.

**Cómo funciona:** 
El dispositivo recibe un mensaje ICMPv6 RA (Router Advertisement) del router local, el cual le proporciona la información necesaria para crear su dirección IPv6 y conectarse a la red. 
No se necesita ningún servidor DHCPv6, ya que el propio dispositivo genera su dirección.

**Por qué se llama “sin estado” (stateless):** 
No existe un servidor que mantenga un registro de qué dirección IPv6 tiene cada dispositivo. 
Cada host se autoconfigura usando los datos recibidos en el mensaje RA.

**Cómo se construye la dirección IPv6:**

1. **Prefijo:** Proviene del mensaje RA enviado por el router (por ejemplo, `2001:db8:acad:1::/64`).

2. **ID de interfaz:** El dispositivo genera esta parte de 64 bits usando uno de dos métodos:
   
   - **EUI-64:** Basado en su dirección MAC (única para cada interfaz).
   
   - **Número aleatorio:** Generado de forma segura por el sistema operativo.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-17-51-22-image.png" title="" alt="" data-align="center">

1. *El enrutador envia un mensaje RA con el prefijo para el enlace local.*
2. *La PC usa SLAAC para obtener un prefijo del mensaje RA y crea su propia ID de interfaz.*

#### Método 2 - SLAAC y DHCPv6 sin estado

El enrutador puede configurarse para que los dispositivos obtengan su configuración IPv6 combinando SLAAC y DHCPv6 sin estado.

- **SLAAC (Stateless Address Autoconfiguration)** permite que cada dispositivo genere automáticamente su dirección IPv6 global (GUA) usando la información que recibe en los anuncios del enrutador (RA).

- El gateway predeterminado será la dirección link-local del router, que también se incluye en el mensaje RA.

- Además, el router indica que los dispositivos deben contactar un servidor DHCPv6 sin estado, el cual no asigna direcciones IP, pero sí proporciona información adicional, como la dirección del servidor DNS y el nombre de dominio.

SLAAC configura la dirección IPv6, el router actúa como puerta de enlace, y el DHCPv6 sin estado entrega solo la información complementaria de red.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-17-56-28-image.png" title="" alt="" data-align="center">

1. *El PC envia un RS a todos los enrutadores IPv6, «Necesito información de direccionamiento».*
2. *El enrutador envia un mensaje RA a todos los nodos IPv6 con el Método 2 (SLAAC y DHCPv6) especificado. "Aqui esta la información de su prefijo, longitud de
   prefijo y puerta de enlace predeterminada. Pero tendrá que obtener información DNS de un servidor DHCPv6»*.
3. *El PC envia un mensaje de solicitud DHCPv6 a todos los servidores DHCPv6. «Utilicé SLAAC para crear mi dirección IPv6 y obtener mi dirección de puerta de
   enlace predeterminada, pero necesito otra información de un servidor DHCPv6 sin estado.* 

#### Método 3 - DHCPv6 con estado

El método DHCPv6 con estado funciona como el DHCP tradicional de IPv4: el servidor asigna direcciones IPv6 (GUA) y guarda un registro de qué dispositivo tiene cada una.

En este caso, el router solo envía un mensaje RA (Router Advertisement) indicando a los dispositivos que:

- Usen la dirección link-local (LLA) del router como puerta de enlace predeterminada.

- Obtengan toda la demás información (dirección IPv6, DNS y nombre de dominio) desde un servidor DHCPv6 con estado.

El router solo indica el gateway, y el servidor DHCPv6 gestiona el resto del direccionamiento.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-18-03-40-image.png" title="" alt="" data-align="center">

1. *La PC envia un RS a todos los enrutadores IPv6, "Necesito información de direccionamiento"*.
2. *El enrutador envia un mensaje RA a todos los nodos IPv6 con el Método 3 (DHCPv6 con estado) especificado: "Soy su puerta de enlace predeterminada, pero
   debe pedirle a un servidor DHCPv6 con estado su direccion IPv6 y otra información de direccionamiento"*.
3. *La PC envia un mensaje de solicitud de DHCPv6 a todos los servidores DHCPv6, "Recibi mi dirección de puerta de enlace predeterminada del mensaje RA,
   pero necesito una dirección IPv6 y toda otra información de direccionamiento de un servidor DHCPv6 con estado"*.

Un servidor DHCPv6 con estado asigna direcciones IPv6 a los dispositivos y mantiene un registro de qué dirección tiene cada uno, similar a cómo funciona DHCP en IPv4.

La dirección de puerta de enlace predeterminada no la entrega el servidor DHCPv6 (ni con ni sin estado); solo se obtiene automáticamente a través del mensaje RA (Router Advertisement) del enrutador.

#### Proceso EUI-64 versus generado aleatorio

Cuando el mensaje RA usa SLAAC o SLAAC con DHCPv6 sin estado, el cliente genera su propia ID de interfaz, ya que elprefijo se obtiene del mensaje RA, pero la segunda parte (ID de interfaz) debe crearla el dispositivo. 
Esta ID puede generarse mediante el método EUI-64 o con un número aleatorio de 64 bits.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-18-07-21-image.png" title="" alt="" data-align="center">

1. *El enrutador envia un mensaje RA.*
2. *El PC utiliza el prefijo del mensaje RA y utiliza EUI-64 o un número aleatorio de 64 bits para generar un ID de interfaz.*

#### Proceso EUI-64

El proceso EUI-64 permite generar una ID de interfaz IPv6 de 64 bits a partir de la dirección MAC de 48 bits de un dispositivo.

**Cómo funciona:**

1. Toma la dirección MAC del dispositivo, que está dividida en:
   
   - **OUI (Organizationally Unique Identifier)**: Los primeros 24 bits (asignados por IEEE al fabricante).
   
   - **Identificador del dispositivo**: Los últimos 24 bits (únicos dentro del fabricante).

2. Se inserta el valor “FFFE” (16 bits) en medio de la dirección MAC.

3. Se invierte el séptimo bit del OUI (llamado bit universal/local, U/L):
   
   - Si es 0, se cambia a 1.
   
   - Si es 1, se cambia a 0.

Al final, una ID de interfaz de 64 bits única basada en la dirección MAC. 
Por ejemplo, a partir de la MAC `fc99:4775:cee0`, el proceso genera una ID extendida que el dispositivo usará para su dirección IPv6.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-18-25-34-image.png" title="" alt="" data-align="center">

*Paso 1: Divida la dirección MAC entre la OUI y el identificador del dispositivo.*

*Paso 2: Inserte el valor hexadecimal fffe, que en binario es: 1111 1111 1111 1110.*

*Paso 3: Convierta los primeros 2 valores hexadecimales de la OU a binario y voltee el bit U/ L (bit 7). En este ejemplo, el 0 en el bit 7 se cambia a 1.*

*El resultado es un ID de interfaz generado por EUI-64 de **fe99: 47ff: fe75: cee0**.*

*Nota: El uso del bit U/L, y las razones para invertir su valor, se discuten en RFC 5342.*

**Contexto de la Nota:** Explica que el bit U/L (Universal/Local) indica si una dirección fue asignada por el fabricante o creada manualmente:

- **0 = Universal:** La dirección proviene del fabricante (es globalmente única).

- **1 = Local:** La dirección fue modificada o creada localmente (por ejemplo, al generar una ID de interfaz con EUI-64).

Por eso, al crear una dirección EUI-64, se invierte este bit para mostrar que la nueva dirección ya no es la original del fabricante, sino una versión modificada localmente.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-18-36-03-image.png" title="" alt="" data-align="center">

El comando ipconfig puede mostrar una dirección IPv6 global (GUA) generada dinámicamente mediante SLAAC y el proceso EUI-64, que inserta **“fffe”** en medio de la ID de la interfaz, derivándola de la dirección MAC. 
Este método facilita rastrear una dirección IPv6 hasta un dispositivo físico, lo que plantea problemas de privacidad. Por ello, se pueden usar IDs de interfaz aleatorias para evitar el rastreo.

#### ID de interfaz generadas aleatoriamente

Según el sistema operativo, un dispositivo puede generar su ID de interfaz de forma aleatoria o mediante EUI-64. 
Desde Windows Vista, se usa una ID aleatoria, mientras que Windows X** y versiones anteriores empleaban EUI-64. 
Una vez creada la ID (por cualquiera de los métodos), se combina con el prefijo IPv6 recibido en el mensaje RA para formar una dirección GUA.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-30-18-41-27-image.png" title="" alt="" data-align="center">

*Nota: Para garantizar la unicidad de cualquier direccion de unidifusion IPv6, el cliente puede usar un proceso conocido como Detección de direcciones duplicadas (DAD). Es similar a una solicitud de ARP para su propia dirección. Si no se obtiene una respuesta, la dirección es única.*

---

### Direccionamiento dinámico para las LLAS IPv6

Todos los dispositivos IPv6 deben tener una dirección link-local (LLA). Estas direcciones se pueden crear dinámicamente, al igual que las GUA. 
El LLA se genera automáticamente usando el prefijo fe80::/10 y una ID de interfaz, que puede formarse mediante el proceso EUI-64 o con un número aleatorio de 64 bits. 
Es fundamental verificar la configuración IPv6 para asegurarse de que las direcciones (tanto LLA como GUA) se hayan creado correctamente.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-10-14-28-image.png" title="" alt="" data-align="center">

#### LLA dinámicos en Windows

Los sistemas operativos, como Windows, suelen usar el mismo método de generación de direcciones (por ejemplo, EUI-64 o un número aleatorio) tanto para crear una GUA mediante SLAAC como para asignar una LLA de forma dinámica.

*ID de interfaz generada mediante EUI-64*

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-10-15-50-image.png" title="" alt="" data-align="center">

*ID de interfaz de 64 bits generada aleatoriamente*

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-10-16-27-image.png" title="" alt="" data-align="center">

#### LLA dinámicos en enrutadores Cisco

Los routers Cisco generan automáticamente una LLA IPv6 al asignar una GUA a una interfaz, usando el método EUI-64 para crear la ID de interfaz. En interfaces seriales, usan la MAC de una interfaz Ethernet. Aunque estas LLAs son únicas en su enlace, su longitud las hace difíciles de identificar, por lo que es común configurarlas manualmente para facilitar su reconocimiento.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-11-56-02-image.png" title="" alt="" data-align="center">

#### Verifique la configuración de la dirección IPv6

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-12-02-38-image.png" title="" alt="" data-align="center">

- **Show ipv6 interface brief**

El comando **`show ipv6 interface brief`** muestra las direcciones MAC usadas por EUI-64 para generar las LLA y un resumen del estado de las interfaces. Cada interfaz tiene dos direcciones IPv6:

- Una LLA (que comienza con `fe80`) creada automáticamente.

- Una GUA configurada manual o dinámicamente.

En interfaces seriales, como no tienen MAC propia, Cisco IOS usa la MAC de la primera interfaz Ethernet disponible, lo cual es válido porque las LLA solo deben ser únicas dentro de su enlace.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-12-05-12-image.png" title="" alt="" data-align="center">

- **Show ipv6 route**

El comando **`show ipv6 route`** permite verificar las redes IPv6 y las direcciones configuradas en la tabla de enrutamiento (no muestra redes IPv4).

- La letra C indica una red conectada directamente.

- La letra L representa una ruta local, que corresponde a la dirección IPv6 específica de una interfaz (no a una LLA).

- Cuando una interfaz con una GUA está en estado up/up, su prefijo IPv6 se agrega como ruta conectada y su dirección individual (/128) como ruta local, lo que permite procesar eficientemente los paquetes destinados al propio router.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-12-05-47-image.png" title="" alt="" data-align="center">

- **Ping**

El comando **`ping`** en IPv6 funciona igual que en IPv4, pero utiliza una dirección IPv6. 
Cuando se hace ping a una dirección link-local (LLA) desde un router, Cisco IOS solicita especificar la interfaz de salida, ya que una misma LLA puede existir en distintos enlaces. Esto permite verificar la conectividad de Capa 3 entre dispositivos como el router y una PC.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-12-08-43-image.png" title="" alt="" data-align="center">

---

### Direcciones IPv6 de multidifusión

Las direcciones IPv6 de multidifusión se usan para enviar un solo paquete a varios destinos dentro de un grupo específico. 
Tienen el prefijo `ff00::/8` y solo pueden usarse como direcciones de destino, no de origen.

Existen dos tipos principales:

1. **Multidifusión conocidas** → grupos predefinidos con funciones específicas (por ejemplo, todos los routers o todos los nodos).

2. **Multidifusión de nodo solicitado** → utilizadas por los dispositivos para la resolución de direcciones y detección de vecinos.

#### Direcciones de multidifusión IPv6 bien conocidas

Las direcciones de multidifusión IPv6 conocidas son direcciones reservadas para grupos específicos de dispositivos que comparten un protocolo o servicio común, como DHCPv6.

Dos de las más comunes son:

- **`ff02::1` (Todos los nodos):** Incluye a todos los dispositivos IPv6 del enlace. Los mensajes enviados a esta dirección son recibidos por todos los nodos, similar a una difusión en IPv4.

- **`ff02::2` (Todos los enrutadores):** Incluye a todos los routers IPv6 del enlace. Los routers se unen automáticamente a este grupo cuando se habilita el enrutamiento IPv6 con `ipv6 unicast-routing`.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-13-16-28-image.png" title="" alt="" data-align="center">

*Los dispositivos con IPv6 habilitado envían mensajes ICMPv6 RS (Router Solicitation) a la dirección de multidifusión de todos los enrutadores (`ff02::2`) para pedir información de configuración. En respuesta, el router IPv6 envía un mensaje RA (Router Advertisement) que proporciona los datos necesarios para que el dispositivo configure su dirección IPv6.*

#### Direcciones IPv6 de multidifusión de nodo solicitado

Una dirección de multidifusión de nodo solicitado funciona como la de todos los nodos, pero tiene una ventaja clave: Se vincula a una dirección MAC de multidifusión especial, lo que permite que la tarjeta de red (NIC) filtre los paquetes directamente a nivel de hardware. 
Así, solo los paquetes destinados al dispositivo correcto son procesados por IPv6, mejorando la eficiencia de red.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-13-18-30-image.png" title="" alt="" data-align="center">

---

### División de subredes de una red IPv6

En IPv6, la subredificación es más sencilla que en IPv4 porque fue diseñada desde el inicio para soportarla. 
A diferencia de IPv4, donde se toman bits del host para crear subredes, en IPv6 existe un campo específico llamado ID de subred dentro de la **GUA (Global Unicast Address)**. 
Este campo se encuentra entre el prefijo de enrutamiento global y el ID de interfaz, lo que facilita la organización y segmentación de redes sin alterar otras partes de la dirección.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-13-21-36-image.png" title="" alt="" data-align="center">

La división en subredes IPv6 es más sencilla que en IPv4 porque el protocolo fue diseñado con subredes en mente.

Con un prefijo global /48, se obtienen:

- 16 bits para el ID de subred, lo que permite hasta 65.536 subredes.

- 64 bits para el ID de interfaz, lo que admite cerca de 18 quintillones de direcciones por subred.

No es necesario convertir a binario: para crear nuevas subredes, basta con sumar valores en hexadecimal. 
Además, la conservación de direcciones no es un problema gracias al amplio espacio de 128 bits.

#### Ejemplo de subred IPv6

Cuando a una organización se le asigna el prefijo 2001:db8:acad::/48, los primeros 48 bits identifican el prefijo de enrutamiento global, común para todas sus subredes.

Luego, la organización puede usar los 16 bits siguientes como ID de subred, lo que permite crear 65.536 subredes /64. 
Para generar cada nueva subred, simplemente se incrementa el valor hexadecimal del hexteto correspondiente a la subred, mientras el prefijo global se mantiene igual.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-13-45-29-image.png" title="" alt="" data-align="center">

#### Asignación de subredes IPv6

Con IPv6, el administrador debe diseñar un esquema lógico de direccionamiento entre más de 65.536 subredes posibles. En el ejemplo, se requieren cinco subredes: una para cada LAN y una para el enlace serie entre R1 y R2. A diferencia de IPv4, todas las subredes, incluso la del enlace serie, usan la misma longitud de prefijo, lo que simplifica la administración, ya que en IPv6 no es necesario preocuparse por conservar direcciones.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-13-54-58-image.png" title="" alt="" data-align="center">

Se asignaron cinco subredes IPv6 con los ID de subred del 0001 al 0005. Cada subred tiene un prefijo /64, lo que ofrece una cantidad de direcciones muy superior a las que se podrían necesitar.

#### Enrutador configurado con subredes IPv6

Al igual que en IPv4, cada interfaz del enrutador en IPv6 se configura dentro de una subred distinta.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-10-31-13-57-54-image.png" title="" alt="" data-align="center">
