# Módulo 11 - Asignación de direcciones IPv4

---

## Contenido

- **Estructura de la dirección IPv4:** Describe la estructura de una dirección IPv4, incluidas la porción de red y de host, y la
  máscara de subred.

- **IPv4 Unicast, Broadcast, y Multicast:** Compare las características y los usos de las direcciones IPv4 unicast, broadcast y multicast.

- **Tipos de direcciones IPv4:** Explica las direcciones IPv4 públicas, privadas y reservadas.

- **Segmentación de la red:** Explica la forma en que la division en subredes segmenta una red para permitir una mejor comunicación.

- **Division de subredes de una red IPv4:** Calcula las subredes IPv4 para un prefijo /24.

- **Division de subredes con prefijos /16 y /8:** División de subredes con prefijos /16 y /8.

- **Division en subredes para cumplir con requisitos:** Dado un conjunto de requisitos para subredes, implementar un IPv4 esquema de direccionamiento.

- **Mascara de subred de longitud variable:** Explica cómo crear un esquema de direccionamiento flexible usando variables Máscara de subred de longitud variable (VLSM).

- **Diseño estructurado:** Implemente un esquema de asignación de direcciones VLSM.

---

### Estructura de la dirección IPv4

Una dirección IPv4 tiene 32 bits y está dividida en dos partes:

- **Porción de red:** Identifica la red a la que pertenece el dispositivo.

- **Porción de host:** Identifica el dispositivo dentro de esa red.

Para saber qué parte corresponde a red y cuál a host, se analiza la dirección junto con la máscara de subred, que indica cuántos bits pertenecen a la red y cuántos al host.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-11-08-20-image.png]]

Una dirección IPv4 de 32 bits se divide en porción de red y porción de host, y la máscara de subred determina cuántos bits corresponden a cada una.

### La máscara de subred

Como se muestra en la figura, asignar una dirección IPv4 a un host requiere lo siguiente:

- **Dirección IPv4:** Esta es la dirección IPv4única del host.

- **Máscara de subred:** Se usa para identificar la parte de red/host de la dirección IPv4.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-11-11-08-image.png]]

Una puerta de enlace predeterminada permite comunicarse con redes remotas y los servidores DNS traducen nombres de dominio a direcciones IPv4.

La máscara de subred se usa para distinguir la porción de red y la porción de host en una dirección IPv4. 
Al asignar una dirección a un dispositivo, la máscara permite identificar la dirección de red, que representa a todos los dispositivos dentro de la misma red.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-11-13-21-image.png]]

La máscara de subred está formada por unos (1) que indican la porción de red y ceros (0) que indican la porción de host. 
Para determinar qué parte de la dirección IPv4 corresponde a la red y cuál al host, se compara la dirección con la máscara bit por bit, de izquierda a derecha:

- Los bits donde la máscara tiene 1 pertenecen a la red.

- Los bits donde la máscara tiene 0 pertenecen al host.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-11-17-13-image.png]]

Tenga en cuenta que la máscara de subred en realidad no contiene la porción de red o host de una dirección IPv4, solo le dice a la computadora dónde buscar la parte de la dirección IPv4 que es la porción de red y qué parte es la porción de host.

El proceso real que se usa para identificar la porción de red y la porción de host se denomina AND.

#### La longitud del prefijo

Para simplificar el uso de las máscaras de subred en formato decimal, se utiliza la longitud del prefijo. 
La longitud del prefijo indica cuántos bits de la máscara están en 1 y se escribe en notación con barra, por ejemplo /24. 
Así, solo se cuenta la cantidad de bits en 1 en la máscara y se escribe después de una barra para representar la máscara de subred de forma más sencilla.

| Máscara de subred | Dirección en 32 bits                | Longitud de prefijo |
| ----------------- | ----------------------------------- | ------------------- |
| 255.0.0.0         | 11111111.00000000.00000000.00000000 | /8                  |
| 255.255.0.0       | 11111111.11111111.00000000.00000000 | /16                 |
| 255.255.255.0     | 11111111.11111111.11111111.00000000 | /24                 |
| 255.255.255.128   | 11111111.11111111.11111111.10000000 | /25                 |
| 255.255.255.192   | 11111111.11111111.11111111.11000000 | /26                 |
| 255.255.255.224   | 11111111.11111111.11111111.11100000 | /27                 |
| 255.255.255.240   | 11111111.11111111.11111111.11110000 | /28                 |
| 255.255.255.248   | 11111111.11111111.11111111.11111000 | /29                 |
| 255.255.255.252   | 11111111.11111111.11111111.11111100 | /30                 |

#### Determinación de la red - Lógico AND

La operación AND lógica se usa para obtener la dirección de red a partir de una dirección IPv4 y su máscara de subred. 
En la operación AND, solo 1 AND 1 = 1, y cualquier otra combinación resulta en 0.

Para encontrar la dirección de red, se compara bit por bit la dirección IPv4 con la máscara de subred usando AND. 
Por ejemplo, al aplicar AND entre 192.168.10.10 y 255.255.255.0, el resultado es la dirección de red 192.168.10.0.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-11-30-09-image.png]]

Para obtener la dirección de red, se realiza una operación AND entre los bits de la dirección IPv4 del host y los bits de la máscara de subred. 
Solo cuando ambos bits son 1, el resultado es 1. 
Al aplicar esta operación a la dirección 192.168.10.10 con la máscara 255.255.255.0 (/24), se obtiene la dirección de red 192.168.10.0/24, que indica a qué red pertenece el host.

#### Direcciones de red, de host y de difusión

Dentro de cada red hay tres tipos de direcciones IP:

- Direccion de red 

- Direcciones de host

- Dirección de broadcast

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-14-58-02-image.png]]

La dirección de red identifica a una red específica. Un dispositivo pertenece a esa red si usa la misma máscara de subred y tiene los mismos bits de red. 
Para obtener la dirección de red, el host realiza una operación AND entre su dirección IPv4 y la máscara de subred. 
En la dirección de red, todos los bits de la parte de host son 0, por lo que no puede asignarse a un dispositivo. 
Ejemplo: 192.168.10.0/24.

| Descripción                                  | Porción de red (Decimal / Binario)                                                | Porción de host (Decimal / Binario)                                               | Bits de host        |
| :------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------- |
| **Máscara de subred 255.255.255.0 /24**      | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-49-46-image.png]]   | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-52-57-image.png]]   | Todos los 0         |
| **Dirección de red 192.168.10.0 /24**        | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-51-26-image.png]]   | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-52-57-image 1.png]] | Todos los 0         |
| **Primera dirección 192.168.10.1 /24**       | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-51-26-image 1.png]] | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-53-07-image.png]]   | Todos los 0s y un 1 |
| **Última dirección 192.168.10.254 /24**      | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-51-26-image 2.png]] | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-53-16-image.png]]   | Todos los 1s y un 0 |
| **Dirección de difusión 192.168.10.255 /24** | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-51-26-image 3.png]] | ![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-27-15-53-29-image.png]]   | Todos los 1s        |

En una red IPv4, las direcciones de host son las que se asignan a los dispositivos (computadores, teléfonos, impresoras, routers, etc.). 
Estas direcciones comparten la misma parte de red y la misma máscara, pero tienen una parte de host diferente.

- La parte de host corresponde a los bits en la dirección que son 0 en la máscara de subred.

- Las direcciones de host pueden usar cualquier combinación de bits en la parte de host, excepto:
  
  - **Todos 0** → sería la dirección de red.
  
  - **Todos 1** → sería la dirección de difusión (broadcast).

Por eso, dentro de una red:

- **Primera dirección de host**: 192.168.10.1/24

- **Última dirección de host**: 192.168.10.254/24

- Cualquier dirección entre estas dos se puede asignar a dispositivos.

La dirección de broadcast (difusión) se utiliza para enviar mensajes a todos los dispositivos de la red. En este ejemplo es:

- 192.168.10.255/24

Esta dirección no se asigna a ningún dispositivo.

---

### IPv4 Unicast, Broadcast, y Multicast

#### Unidifusión

La dirección IPv4 se compone de una parte de red y una parte de host. Existen diferentes formas de enviar paquetes, y una de ellas es la unidifusión.

La transmisión unidifusión ocurre cuando un dispositivo envía un mensaje a un solo dispositivo específico. Es una comunicación uno a uno.

- La dirección IP de destino es una dirección de unidifusión (es decir, una dirección única que identifica a un solo host).

- La dirección IP de origen también siempre es una dirección de unidifusión, porque el mensaje proviene de un solo dispositivo.

- Esto sigue siendo cierto incluso si el destino fuera una dirección de difusión o multidifusión, siempre hay un único origen.

Las direcciones IPv4 de unidifusión son aquellas que se pueden asignar a dispositivos para comunicaciones uno a uno. Estas direcciones van desde 1.1.1.1 hasta 223.255.255.255. 
Sin embargo, dentro de este rango existen algunas direcciones reservadas para usos especiales (como redes privadas, pruebas, o direcciones de loopback), las cuales se explicarán más adelante.

#### Dirección

La transmisión de difusión (broadcast) ocurre cuando un dispositivo envía un mensaje a todos los dispositivos dentro de la misma red.

- El paquete de difusión tiene una dirección IPv4 de destino donde la parte de host son todos 1.

- IPv4 sí usa difusión, pero IPv6 no.

Existen dos tipos de difusión:

| Tipo                  | Dirección usada                                                                          | ¿A quién llega?                                                    |
| --------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Difusión dirigida** | La dirección de difusión de una red, por ejemplo: 172.16.4.255 para la red 172.16.4.0/24 | A todos los host de esa red específica                             |
| **Difusión limitada** | 255.255.255.255                                                                          | A todos los host del dominio de difusión local (no sale de la red) |

*Nota: Los routers no reenvían paquetes de difusión, por lo tanto, se quedan dentro del dominio de difusión.*

Los paquetes de difusión consumen recursos de red y deben limitarse para evitar afectar el rendimiento, ya que todos los hosts deben procesarlos. Los routers separan los dominios de difusión, mejorando el rendimiento al reducir el tráfico innecesario.

Además de la dirección 255.255.255.255, cada red tiene una difusión dirigida, que usa la dirección más alta del rango (por ejemplo, para 192.168.1.0/24 es 192.168.1.255). Esta permite enviar un solo paquete a todos los hosts de esa red.

Sin embargo, por motivos de seguridad, las difusiones dirigidas IP están deshabilitadas por defecto desde Cisco IOS 12.0 mediante el comando: 
`no ip directed-broadcasts`.

#### Multidifusión

La multidifusión reduce el tráfico al permitir que un host envíe un solo paquete a un grupo específico de hosts suscritos. Utiliza direcciones IP del rango 224.0.0.0 a 239.255.255.255.

Los clientes de multidifusión se suscriben a un grupo mediante un programa cliente y reciben solo los paquetes dirigidos a la dirección del grupo o a su propia dirección unidifusión.

Protocolos como OSPF emplean multidifusión para comunicarse entre routers, usando direcciones reservadas como 224.0.0.5, que solo procesan los dispositivos configurados para OSPF, mientras que los demás las ignoran.

---

### Tipos de direcciones IPv4

La multidifusión optimiza el tráfico al enviar un solo paquete a varios hosts suscritos, usando direcciones del rango 224.0.0.0 a 239.255.255.255. Los hosts se unen a grupos específicos para recibir solo esos paquetes. Protocolos como OSPF la utilizan para comunicarse entre routers mediante direcciones reservadas como 224.0.0.5.

| **Dirección de red y prefijo** | **Rango de direcciones privadas de RFC 1918** |
| ------------------------------ | --------------------------------------------- |
| 10.0.0.0/8                     | 10.0.0.0 a 10.255.255.255                     |
| 172.16.0.0/12                  | 172.16.0.0 a 172.31.255.255                   |
| 192.168.0.0/16                 | 192.168.0.0 a 192.168.255.255                 |

#### Enrutamiento en Internet

Las direcciones IPv4 privadas se usan en redes internas (intranets) de hogares y empresas, pero no son enrutables globalmente. Por ello, cuando los dispositivos envían paquetes hacia Internet con direcciones privadas de origen, estos deben ser filtrados o traducidos a direcciones públicas mediante mecanismos como NAT antes de salir hacia el ISP.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-09-20-13-image.png]]

El NAT (Traducción de Direcciones de Red) convierte las direcciones IPv4 privadas en públicas para permitir la comunicación con Internet, proceso que realiza el router que conecta la red interna con el ISP. Aunque el NAT evita el acceso directo desde Internet, no es una medida de seguridad real.

Las organizaciones con servicios accesibles desde Internet, como servidores web, usan una DMZ (zona desmilitarizada), donde el router actúa también como firewall y gestiona tanto el enrutamiento como la traducción de direcciones.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-09-24-38-image.png]]

#### Direcciones IPv4 de uso especial

Las direcciones de loopback (rango 127.0.0.0/8, comúnmente 127.0.0.1) permiten que un host envíe tráfico a sí mismo. Se usan para probar la configuración TCP/IP y confirmar que la pila de red funciona correctamente. Todas las direcciones dentro de este bloque hacen un bucle interno hacia el mismo dispositivo.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-09-31-49-image.png]]

Las direcciones link-local o APIPA (169.254.0.0/16) se asignan automáticamente cuando un cliente DHCP no encuentra un servidor disponible. Permiten la comunicación local dentro de la misma red, aunque no son enrutables ni se usan comúnmente para conexiones punto a punto.

#### Direccionamiento con clase antigua

El direccionamiento con clases, definido en 1981 (RFC 790), organizaba las direcciones IPv4 en tres clases principales (A, B y C) según el tamaño de la red:

- **Clase A (0.0.0.0 – 127.255.255.255)**: Para redes muy grandes, con más de 16 millones de hosts por red.

- **Clase B (128.0.0.0 – 191.255.255.255)**: Para redes medianas, con hasta 65,000 hosts.

- **Clase C (192.0.0.0 – 223.255.255.255)**: Para redes pequeñas, con 254 hosts como máximo.

También existían:

- **Clase D (224.0.0.0 – 239.255.255.255)** para multidifusión.

- **Clase E (240.0.0.0 – 255.255.255.255)** para uso experimental.

Este esquema era útil cuando Internet tenía pocos equipos, pero con el crecimiento de la red se volvió ineficiente, ya que las clases A y B reservaban demasiadas direcciones sin uso, provocando desperdicio del espacio IPv4.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-09-40-00-image.png]]

A mediados de los años 90, el crecimiento de Internet hizo que el direccionamiento con clase quedara obsoleto. Fue reemplazado por el direccionamiento sin clase (CIDR), que permite asignar bloques de direcciones IPv4 según la necesidad real y no según clases fijas (A, B o C). Esto optimizó el uso del espacio limitado de direcciones IPv4.

#### Asignación de direcciones IP

Las direcciones IPv4 públicas son únicas y enrutables globalmente a través de los routers de los ISP. Su asignación es gestionada por la IANA, que distribuye bloques de direcciones a los Registros Regionales de Internet (RIR). Estos RIR asignan direcciones a los ISP y organizaciones, que luego las reparten a sus usuarios según sus necesidades y políticas.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-10-08-31-image.png]]

- **AfriNIC** (African Network Information Centre) - Africa Region

- **APNIC** (Asia Pacific Network Information Centre) - Asia/Pacific Region

- **ARIN** (American Registry for Internet Numbers) - North America Region

- **LACNIC** (Regional Latin-American and Caribbean IP Address Registry) - Latin America and some Caribbean Islands

- **RIPE NCC** (Réseaux IP Européens Network Coordination Centre) - Europa, Medio Oriente y Asia Central

---

### Segmentación de la red

Un dominio de difusión grande conecta muchos hosts, lo que puede generar exceso de tráfico de difusión. Esto provoca lentitud en la red y en los dispositivos, ya que cada uno debe recibir y procesar todos los paquetes de difusión enviados por los demás.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-10-16-06-image.png]]

La división en subredes reduce el tamaño de los dominios de difusión al separar una red grande en subredes más pequeñas. Así, el tráfico de difusión se limita a cada subred, mejorando el rendimiento. Por ejemplo, una red 172.16.0.0/16 puede dividirse en 172.16.0.0/24 y 172.16.1.0/24, evitando que las difusiones de una LAN afecten a la otra.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-10-28-42-image.png]]

La división en subredes consiste en tomar bits del campo de host para crear más subredes, aumentando así la longitud del prefijo (por ejemplo, de /16 a /24). En la práctica, los términos red y subred se usan de forma similar, ya que casi todas las redes forman parte de un bloque mayor de direcciones.



#### Razones para segmentar redes

La división en subredes mejora el rendimiento y la seguridad de la red al reducir el tráfico general y limitar las difusiones. También permite aplicar políticas de comunicación entre subredes y minimizar el impacto de errores, fallas o ataques. En general, las subredes facilitan la administración y control de los dispositivos de red.

División por ubicación, grupo o función y tipo de dispositivo:

- **Ubicación**

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-10-32-36-image.png]]

- **Grupo o función**

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-10-33-00-image.png]]

- **Tipo de dispositivo**

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-28-10-34-26-image.png]]

---

### División de subredes de una red IPv4

La segmentación de redes o subredificación es una habilidad esencial en la administración de redes IPv4. Consiste en tomar bits del campo de host para ampliar la máscara de subred y crear más subredes. Mientras más bits se tomen, más subredes habrá, pero menos hosts por subred. Generalmente, las divisiones se hacen en los límites /8, /16 y /24, donde un prefijo más largo implica menos hosts disponibles.

| Longitud de prefijo | Máscara de subred | Máscara de subred en sistema binario (n=red, h=host)                       | # de hosts |
| ------------------- | ----------------- | -------------------------------------------------------------------------- | ---------- |
| /8                  | 255.0.0.0         | nnnnnnnn.hhhhhhhh.hhhhhhhh.hhhhhhhh<br>11111111.00000000.00000000.00000000 | 16777214   |
| /16                 | 255.255.0.0       | nnnnnnnn.nnnnnnnn.hhhhhhhh.hhhhhhhh<br>11111111.11111111.00000000.00000000 | 65534      |
| /24                 | 255.255.255.0     | nnnnnnnn.nnnnnnnn.nnnnnnnn.hhhhhhhh<br>11111111.11111111.11111111.00000000 | 254        |

La empresa con la red 10.0.0.0/8 puede dividirla en subredes más pequeñas, por ejemplo, en /16, creando 256 subredes (de 10.0.0.0/16 a 10.255.0.0/16). 
Cada subred puede tener 65,534 hosts, ya que los dos primeros octetos identifican la red y los dos últimos se usan para los hosts. 
Esto mejora la organización y evita tener un dominio de difusión excesivamente grande.

- **Subred de la red 10.0.0.0/8 usando un /16**

| **Dirección de subred** (256 subredes posibles) | **Rango de host** (65,534 posibles hosts por subred) | **Dirección**      |
| ----------------------------------------------- | ---------------------------------------------------- | ------------------ |
| **10.0.0.0/16**                                 | 10.0.0.1 – 10.0.255.254                              | **10.0.255.255**   |
| **10.1.0.0/16**                                 | 10.1.0.1 – 10.1.255.254                              | **10.1.255.255**   |
| **10.2.0.0/16**                                 | 10.2.0.1 – 10.2.255.254                              | **10.2.255.255**   |
| **10.3.0.0/16**                                 | 10.3.0.1 – 10.3.255.254                              | **10.3.255.255**   |
| **10.4.0.0/16**                                 | 10.4.0.1 – 10.4.255.254                              | **10.4.255.255**   |
| **10.5.0.0/16**                                 | 10.5.0.1 – 10.5.255.254                              | **10.5.255.255**   |
| **10.6.0.0/16**                                 | 10.6.0.1 – 10.6.255.254                              | **10.6.255.255**   |
| **10.7.0.0/16**                                 | 10.7.0.1 – 10.7.255.254                              | **10.7.255.255**   |
| ...                                             | ...                                                  | ...                |
| **10.255.0.0/16**                               | 10.255.0.1 – 10.255.255.254                          | **10.255.255.255** |

La empresa también puede dividir la red 10.0.0.0/8 en subredes /24, obteniendo 65,536 subredes, cada una con 254 hosts disponibles. Este esquema es muy común porque ofrece un equilibrio adecuado entre cantidad de subredes y hosts, además de facilitar la gestión al dividirse justo en el límite del octeto.

- **División en subredes de la red 10.0.0.0/8 mediante el prefijo /24**

| **Dirección de subred** (65,536 subredes posibles) | **Rango de host** (254 posibles hosts por subred) | **Dirección**      |
| -------------------------------------------------- | ------------------------------------------------- | ------------------ |
| **10.0.0.0/24**                                    | **10.0.0.1 – 10.0.0.254**                         | **10.0.0.255**     |
| **10.0.1.0/24**                                    | **10.0.1.1 – 10.0.1.254**                         | **10.0.1.255**     |
| **10.0.2.0/24**                                    | **10.0.2.1 – 10.0.2.254**                         | **10.0.2.255**     |
| …                                                  | …                                                 | …                  |
| **10.0.255.0/24**                                  | **10.0.255.1 – 10.0.255.254**                     | **10.0.255.255**   |
| **10.1.0.0/24**                                    | **10.1.0.1 – 10.1.0.254**                         | **10.1.0.255**     |
| **10.1.1.0/24**                                    | **10.1.1.1 – 10.1.1.254**                         | **10.1.1.255**     |
| **10.1.2.0/24**                                    | **10.1.2.1 – 10.1.2.254**                         | **10.1.2.255**     |
| …                                                  | …                                                 | …                  |
| **10.100.0.0/24**                                  | **10.100.0.1 – 10.100.0.254**                     | **10.100.0.255**   |
| …                                                  | …                                                 | …                  |
| **10.255.255.0/24**                                | **10.255.255.1 – 10.255.255.254**                 | **10.255.255.255** |

#### Subred dentro de un límite de octeto

Una red con prefijo /24 puede subdividirse tomando prestados bits del último octeto para crear subredes más pequeñas, ajustando así la cantidad de hosts disponibles según las necesidades. 
Al aumentar la longitud del prefijo (por ejemplo, /25, /26, /27, etc.), se duplica el número de subredes pero se reduce a la mitad la cantidad de hosts por cada una.

- **Subred a /24 Red**

| **Longitud de prefijo** | **Máscara de subred** | **# de subredes** | **# de hosts por subred** | **Descripción breve**                                          |
| ----------------------- | --------------------- | ----------------- | ------------------------- | -------------------------------------------------------------- |
| /25                     | 255.255.255.128       | 2                 | 126                       | Divide la red en 2 subredes iguales.                           |
| /26                     | 255.255.255.192       | 4                 | 62                        | Crea 4 subredes con 62 hosts cada una.                         |
| /27                     | 255.255.255.224       | 8                 | 30                        | Aumenta las subredes a 8, reduciendo los hosts.                |
| /28                     | 255.255.255.240       | 16                | 14                        | Ideal para redes pequeñas con pocos dispositivos.              |
| /29                     | 255.255.255.248       | 32                | 6                         | Usada comúnmente para enlaces punto a punto o pequeños grupos. |
| /30                     | 255.255.255.252       | 64                | 2                         | Máxima división: solo 2 hosts por subred.                      |

Por cada bit que se toma prestado en el cuarto octeto, la cantidad de subredes disponible se duplica, al tiempo que se reduce la cantidad de
direcciones de host por subred.

- /25 fila - Tomar prestado 1 bit del cuarto octeto crea 2 subredes que admiten 126 hosts cada una.

- /26 fila - Tomar prestados 2 bits crea 4 subredes que admiten 62 hosts cada una.

- /27 fila - Tomar prestados 3 bits crea 8 subredes que admiten 30 hosts cada una.

- /28 fila - Tomar prestados 4 bits crea 16 subredes que admiten 14 hosts cada una.

- /29 fila - Tomar prestados 5 bits crea 32 subredes que admiten 6 hosts cada una.

- /30 fila - Tomar prestados 6 bits crea 64 subredes que admiten 2 hosts cada una.

---

### División de subredes con prefijos /16 y /8

La dirección 172.16.0.0/16 tiene 16 bits para red y 16 bits para host, lo que permite tomar prestados bits de host para crear más subredes. Al hacerlo, se pueden generar diferentes combinaciones según cuántos bits se tomen: a mayor cantidad de bits prestados, más subredes se obtienen, pero menos hosts por subred. Entonces, dividir un /16 permite ajustar el número de subredes y hosts según las necesidades de la red.

- **Red de subred a /16**

| Longitud de prefijo | Máscara de subred | Dirección de red (n = network, h = host)                                   | # de subredes | # de hosts |
| ------------------- | ----------------- | -------------------------------------------------------------------------- | ------------- | ---------- |
| /17                 | 255.255.128.0     | nnnnnnnn.nnnnnnnn.hhhhhhhh.hhhhhhhh<br>11111111.11111111.10000000.00000000 | 2             | 32766      |
| /18                 | 255.255.192.0     | nnnnnnnn.nnnnnnnn.nnhhhhhh.hhhhhhhh<br>11111111.11111111.11000000.00000000 | 4             | 16382      |
| /19                 | 255.255.224.0     | nnnnnnnn.nnnnnnnn.nnnhhhhh.hhhhhhhh<br>11111111.11111111.11100000.00000000 | 8             | 8190       |
| /20                 | 255.255.240.0     | nnnnnnnn.nnnnnnnn.nnnnhhhh.hhhhhhhh<br>11111111.11111111.11110000.00000000 | 16            | 4094       |
| /21                 | 255.255.248.0     | nnnnnnnn.nnnnnnnn.nnnnnhhh.hhhhhhhh<br>11111111.11111111.11111000.00000000 | 32            | 2046       |
| /22                 | 255.255.252.0     | nnnnnnnn.nnnnnnnn.nnnnnnhh.hhhhhhhh<br>11111111.11111111.11111100.00000000 | 64            | 1022       |
| /23                 | 255.255.254.0     | nnnnnnnn.nnnnnnnn.nnnnnnnh.hhhhhhhh<br>11111111.11111111.11111110.00000000 | 128           | 510        |
| /24                 | 255.255.255.0     | nnnnnnnn.nnnnnnnn.nnnnnnnn.hhhhhhhh<br>11111111.11111111.11111111.00000000 | 256           | 254        |
| /25                 | 255.255.255.128   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nhhhhhhh<br>11111111.11111111.11111111.10000000 | 512           | 126        |
| /26                 | 255.255.255.192   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnhhhhhh<br>11111111.11111111.11111111.11000000 | 1024          | 62         |
| /27                 | 255.255.255.224   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnhhhhh<br>11111111.11111111.11111111.11100000 | 2048          | 30         |
| /28                 | 255.255.255.240   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnnhhhh<br>11111111.11111111.11111111.11110000 | 4096          | 14         |
| /29                 | 255.255.255.248   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnnnhhh<br>11111111.11111111.11111111.11111000 | 8192          | 6          |
| /30                 | 255.255.255.252   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnnnnhh<br>11111111.11111111.11111111.11111100 | 16384         | 2          |

#### Cree 100 subredes con un prefijo Slash 16

Una empresa con la red 172.16.0.0/16 necesita al menos 100 subredes. Para lograrlo, se deben tomar bits del tercer octeto (de izquierda a derecha) de la porción de host. Cada bit prestado duplica la cantidad de subredes posibles.

Al calcular:

- 2⁶ = 64 subredes (insuficiente)

- 2⁷ = 128 subredes (suficiente)

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-09-45-36-image.png]]

Por tanto, se deben tomar 7 bits prestados del tercer octeto, lo que da una nueva máscara de /23 (255.255.254.0), permitiendo 128 subredes con 510 hosts por cada una.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-09-46-29-image.png]]

Al tomar 7 bits prestados del tercer octeto en la red 172.16.0.0/16, la máscara de subred se amplía a /23 (255.255.254.0). 
Esto significa que el tercer octeto en binario es 11111110, indicando los bits prestados. 
Como resultado, se obtienen 128 subredes, que van desde 172.16.0.0/23 hasta 172.16.254.0/23, cada una con 510 hosts disponibles.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-09-47-56-image.png]]

Al prestar 7 bits para la subred, quedan 9 bits para los hosts, lo que genera 512 direcciones por subred. 
Al restar las direcciones reservadas (red y difusión), quedan 510 hosts utilizables por cada /23. 
En la primera subred (172.16.0.0/23), las direcciones de host van desde 172.16.0.1 hasta 172.16.1.254.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-09-49-34-image.png]]

#### Cree 1000 subredes con un prefijo Slash 8

Un ISP pequeño con la red 10.0.0.0/8 necesita 1000 subredes. 
Como la dirección tiene 24 bits de host disponibles, se toman prestados 10 bits (8 del segundo octeto y 2 del tercero), lo que permite crear 1024 subredes (2¹⁰ = 1024). 
Así, la nueva máscara de subred es /18 (255.255.192.0), manteniendo suficiente espacio para hosts dentro de cada subred.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-09-52-23-image.png]]

Se muestra la dirección de red y la máscara de subred resultante, la cual se convierte en 255.255.192.0 o un prefijo /18.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-09-52-38-image.png]]

Se muestra las subredes resultantes de tomar prestados 10 bits, creando subredes de 10.0.0.0/18 a 10.255.192.0/18.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-09-54-36-image.png]]

Al prestar 10 bits para crear subredes en la red 10.0.0.0/8, quedan 14 bits para los hosts, lo que da 16 384 direcciones por subred.
Al restar las direcciones reservadas (red y difusión), quedan 16 382 hosts utilizables por subred. 
Así, cada una de las 1000 subredes puede soportar hasta 16 382 dispositivos.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-09-56-55-image.png]]

---

### División en subredes para cumplir con requisitos

#### Espacio de direcciones IPv4 privado de subred frente al espacio público

En una red empresarial, se utilizan tanto direcciones IPv4 privadas como públicas según la zona:

- **Intranet:** Red interna accesible solo dentro de la organización, usa direcciones privadas.

- **DMZ (zona desmilitarizada):** Área expuesta a Internet que aloja servicios públicos, como servidores web, y usa direcciones públicas.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-10-07-00-image.png]]

La intranet usa direcciones IPv4 privadas, como 10.0.0.0/8, que ofrece gran flexibilidad para crear subredes. 
Al aplicar una máscara /16, se obtienen 256 subredes, cada una con 65 534 hosts disponibles. 
Este esquema es ideal para organizaciones que requieren menos de 200 subredes, dejando margen para el crecimiento y simplificando la administración de la red.

- **Subred de la red 10.0.0.0/8 usando un /16**

| Dirección de subred (256 subredes posibles) | Rango de host (65,534 posibles hosts por subred) | Dirección          |
| ------------------------------------------- | ------------------------------------------------ | ------------------ |
| **10.0.0.0/16**                             | 10.0.0.1 - 10.0.255.254                          | **10.0.255.255**   |
| **10.1.0.0/16**                             | 10.1.0.1 - 10.1.255.254                          | **10.1.255.255**   |
| **10.2.0.0/16**                             | 10.2.0.1 - 10.2.255.254                          | **10.2.255.255**   |
| **10.3.0.0/16**                             | 10.3.0.1 - 10.3.255.254                          | **10.3.255.255**   |
| **10.4.0.0/16**                             | 10.4.0.1 - 10.4.255.254                          | **10.4.255.255**   |
| **10.5.0.0/16**                             | 10.5.0.1 - 10.5.255.254                          | **10.5.255.255**   |
| **10.6.0.0/16**                             | 10.6.0.1 - 10.6.255.254                          | **10.6.255.255**   |
| **10.7.0.0/16**                             | 10.7.0.1 - 10.7.255.254                          | **10.7.255.255**   |
| ...                                         | ...                                              | ...                |
| **10.255.0.0/16**                           | 10.255.0.1 - 10.255.255.254                      | **10.255.255.255** |

Al usar la red privada 10.0.0.0/8 con una máscara /24, se obtienen 65 536 subredes, cada una con 254 hosts disponibles. 
Este esquema es útil para organizaciones que requieren más de 256 subredes, sacrificando cantidad de hosts por subred a cambio de una mayor segmentación de red.

- **Subredes de la red 10.0.0.0/8 usando una subred /24**

| Dirección de subred (65,536 subredes posibles) | Rango de host (254 posibles hosts por subred) | Dirección          |
| ---------------------------------------------- | --------------------------------------------- | ------------------ |
| **10.0.0.0/24**                                | 10.0.0.1 - 10.0.0.254                         | **10.0.0.255**     |
| **10.0.1.0/24**                                | 10.0.1.1 - 10.0.1.254                         | **10.0.1.255**     |
| **10.0.2.0/24**                                | 10.0.2.1 - 10.0.2.254                         | **10.0.2.255**     |
| ...                                            | ...                                           | ...                |
| **10.0.255.0/24**                              | 10.0.255.1 - 10.0.255.254                     | **10.0.255.255**   |
| **10.1.0.0/24**                                | 10.1.0.1 - 10.1.0.254                         | **10.1.0.255**     |
| **10.1.1.0/24**                                | 10.1.1.1 - 10.1.1.254                         | **10.1.1.255**     |
| **10.1.2.0/24**                                | 10.1.2.1 - 10.1.2.254                         | **10.1.2.255**     |
| ...                                            | ...                                           | ...                |
| **10.100.0.0/24**                              | 10.100.0.1 - 10.100.0.254                     | **10.100.0.255**   |
| ...                                            | ...                                           | ...                |
| **10.255.255.0/24**                            | 10.255.255.1 - 10.255.255.254                 | **10.255.255.255** |

#### Minimizar las direcciones IPv4 de host no utilizadas y maximizar las subredes

Para optimizar el uso de direcciones IPv4, se deben considerar dos factores: cuántas direcciones de host necesita cada red y cuántas subredes se requieren.

Existe una relación inversa entre el número de subredes y el de hosts: al tomar más bits para subredes, quedan menos para hosts, y viceversa.

La subred más grande determina cuántos bits deben reservarse para la parte de host. Como no se pueden usar dos direcciones (la de red y la de broadcast), las direcciones utilizables se calculan con la fórmula **2ⁿ - 2**.

- **Subredes en una red /24**

| Longitud de prefijo | Máscara de subred | Máscara de subred en binario (n = network, h = host)                      | # de subredes | # hosts por subred |
| ------------------- | ----------------- | ------------------------------------------------------------------------- | ------------- | ------------------ |
| /25                 | 255.255.255.128   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nhhhhhhh → 11111111.11111111.11111111.10000000 | 2             | 126                |
| /26                 | 255.255.255.192   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnhhhhhh → 11111111.11111111.11111111.11000000 | 4             | 62                 |
| /27                 | 255.255.255.224   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnhhhhh → 11111111.11111111.11111111.11100000 | 8             | 30                 |
| /28                 | 255.255.255.240   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnnhhhh → 11111111.11111111.11111111.11110000 | 16            | 14                 |
| /29                 | 255.255.255.248   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnnnhhh → 11111111.11111111.11111111.11111000 | 32            | 6                  |
| /30                 | 255.255.255.252   | nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnnnnhh → 11111111.11111111.11111111.11111100 | 64            | 2                  |

Los administradores deben planificar un esquema de direccionamiento que equilibre el número máximo de hosts por red y la cantidad de subredes, asegurando capacidad para el crecimiento futuro en ambos aspectos.

#### Subredes IPv4 eficientes

El ISP asignó la red 172.16.0.0/22 a la sede central, proporcionando 1022 direcciones de host. Aunque es un ejemplo, esta dirección pertenece al espacio privado IPv4.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-10-22-53-image.png]]

La sede y cuatro sucursales necesitan su propio espacio IPv4 público, totalizando 10 subredes de la red 172.16.0.0/22. La subred más grande debe soportar 40 hosts, por lo que se busca optimizar al máximo el uso del espacio de direcciones disponible.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-10-27-10-image.png]]

La red 172.16.0.0/22 tiene 10 bits de host disponibles. 
Como la subred más grande necesita 40 hosts, se requieren 6 bits para los hosts, ya que con la fórmula **2⁶ - 2 = 62** se obtienen suficientes direcciones para cubrirlos.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-10-28-59-image.png]]

Al tomar 4 bits prestados de la parte de host (2 del tercer octeto y 2 del cuarto), se obtienen 16 subredes (2⁴ = 16), suficientes para las 10 requeridas y con margen para crecer. 
La nueva máscara es /26 (255.255.255.192), que permite asignar subredes específicas a cada sede y a las conexiones de los routers con el ISP.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-10-30-33-image.png]]

---

### VLSM

#### Conservación de direcciones IPv4

El agotamiento del espacio IPv4 hace necesario optimizar el uso de direcciones al crear subredes. El Subneteo tradicional asigna la misma cantidad de direcciones a cada red, lo que resulta ineficiente cuando las necesidades de hosts varían. En redes con varias LAN y conexiones WAN, el uso de Subneteo variable (VLSM) permite asignar solo las direcciones necesarias a cada subred, aprovechando mejor el espacio disponible.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-04-56-image.png]]

Al tomar prestados 3 bits de la dirección 192.168.20.0/24, se obtienen 8 subredes con 30 hosts utilizables cada una, cumpliendo así con el requisito de siete subredes y la cantidad necesaria de hosts para la LAN más grande.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-06-11-image.png]]

Estas siete subredes podrían asignarse a las redes LAN y WAN.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-11-37-image.png]]

La división en subredes tradicional cumple con los requisitos de la LAN, pero genera un gran desperdicio de direcciones. En los enlaces WAN, que solo requieren dos direcciones, se desperdician 28 de las 30 disponibles por subred, sumando un total de 84 direcciones sin usar.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-13-37-image.png]]

El uso de la división en subredes tradicional limita la expansión futura y desperdicia direcciones. Para solucionar esto, se creó la máscara de subred de longitud variable (VLSM), que permite dividir una subred en partes más pequeñas y aprovechar mejor las direcciones disponibles.

#### VLSM

En la división en subredes tradicional, todas las subredes tienen el mismo tamaño y usan la misma máscara. En cambio, con VLSM, las subredes pueden tener diferentes tamaños, ya que la máscara varía según las necesidades de cada red, permitiendo un uso más eficiente de las direcciones.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-15-47-image.png]]

VLSM permite dividir la red 192.168.20.0/24 en siete subredes de diferentes tamaños, adaptadas a las cuatro LAN y las tres conexiones entre routers, optimizando el uso de direcciones IP.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-18-14-image.png]]

La red 192.168.20.0/24 se divide en ocho subredes iguales, cada una con 30 hosts utilizables; cuatro se asignan a las LAN y tres a las conexiones entre routers.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-18-51-image.png]]

VLSM permite optimizar direcciones al subdividir la última subred 192.168.20.224/27 en subredes más pequeñas /30, ideales para los enlaces entre routers que solo necesitan dos direcciones por subred.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-22-11-image.png]]

Se usa una máscara/30 porque deja solo 2 bits para hosts, lo justo para obtener 2 direcciones utilizables (2² − 2 = 2). A partir de la subred 192.168.20.224/27, se toman 3 bits más prestados, dividiéndola en subredes /30. Así, las cuatro subredes /27 se asignan a las LAN, y tres subredes /30 a los enlaces entre routers, aprovechando al máximo las direcciones sin desperdicio.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-47-52-image.png]]

El uso de VLSM permite ajustar el tamaño de cada subred según sus necesidades, reduciendo el desperdicio de direcciones. En este caso, la subred 7 se usa para los enlaces entre routers, dejando libres las subredes 4, 5 y 6, además de cinco más, para futuras expansiones. Al aplicar VLSM, siempre se debe comenzar con la subred más grande y continuar subdividiendo hasta cubrir las más pequeñas.

#### Asignación de direcciones de topología VLSM

Usando las subredes VLSM, las redes LAN y entre routers se pueden abordar sin desperdicio innecesario.

![[Telematica I/Curso de Cisco/Módulo 11/ANEXOS/2025-10-29-11-49-06-image.png]]

En un esquema de direccionamiento común, la primera dirección de host de cada subred se asigna al router como gateway predeterminado. Los hosts usan direcciones dentro del rango de su subred y la del router como puerta de enlace. La tabla resume las redes, rangos de hosts y sus Gateways correspondientes para las cuatro LAN.

| Red / Edificio | Dirección de red  | Intervalo de direcciones de host | Dirección de puerta de enlace predeterminada |
| -------------- | ----------------- | -------------------------------- | -------------------------------------------- |
| **Edificio A** | 192.168.20.0/27   | 192.168.20.1 → 192.168.20.30     | 192.168.20.1                                 |
| **Edificio B** | 192.168.20.32/27  | 192.168.20.33 → 192.168.20.62    | 192.168.20.33                                |
| **Edificio C** | 192.168.20.64/27  | 192.168.20.65 → 192.168.20.94    | 192.168.20.65                                |
| **Edificio D** | 192.168.20.96/27  | 192.168.20.97 → 192.168.20.126   | 192.168.20.97                                |
| **R1 - R2**    | 192.168.20.224/30 | 192.168.20.225 → 192.168.20.226  | ------------------------------------         |
| **R2 - R3**    | 192.168.20.228/30 | 192.168.20.229 → 192.168.20.230  | ------------------------------------         |
| **R3 - R4**    | 192.168.20.232/30 | 192.168.20.233 → 192.168.20.234  | ------------------------------------         |

---

### Diseño estructurado

Antes de crear subredes, se debe planificar un esquema de direccionamiento IPv4 completo que tenga en cuenta el número de subredes necesarias, la cantidad de hosts por subred, qué dispositivos estarán conectados y qué partes usarán direcciones privadas o públicas.

Un buen plan de direccionamiento evita desperdicio, permite el crecimiento y refleja una buena administración de red.

La planificación comienza con un análisis de la red:

- Se estudian la intranet (red interna) y la DMZ (zona desmilitarizada o de acceso público).

- En la DMZ, se debe conservar direcciones porque normalmente usa direcciones IPv4 públicas, y allí es común aplicar VLSM para aprovechar mejor el espacio disponible.

- En la intranet, esto no es un problema porque se usan direcciones privadas (como 10.0.0.0/8) que ofrecen millones de direcciones disponibles.

Sin embargo, las redes muy grandes o los proveedores de Internet (ISP) pueden necesitar aún más direcciones, lo que impulsa la migración a IPv6, que tiene espacio prácticamente ilimitado.

Además, el plan debe definir:

- Cuántos hosts habrá en cada subred.

- Qué dispositivos tendrán IP estática y cuáles usarán DHCP.

- Cómo se evitarán conflictos o duplicaciones de direcciones.

Entonces, planificar el direccionamiento IPv4 significa diseñar una estructura eficiente, ordenada y escalable para las IP de toda la red, asegurando que haya suficientes direcciones para todos los equipos y evitando desperdicio o errores.

#### Asignación de direcciones de dispositivo

En una red, cada tipo de dispositivo necesita direcciones IP específicas, y su forma de asignarlas depende de su función:

- **Clientes o usuarios finales:** 
  Obtienen direcciones dinámicamente con DHCP, lo que evita errores y simplifica la gestión. Las direcciones se “alquilan” temporalmente y se pueden reutilizar. Si se cambia la subred, el servidor DHCP debe actualizarse. En IPv6 se puede usar DHCPv6 o SLAAC para lo mismo.

- **Servidores y periféricos:** 
  Deben tener IP estáticas y predecibles, para que los usuarios o servicios siempre sepan dónde encontrarlos.

- **Servidores accesibles desde Internet:** 
  Usan direcciones públicas, usualmente protegidas mediante NAT. 
  Si son servidores internos, se accede a ellos a través de una VPN, como si el usuario estuviera dentro de la red local.

- **Dispositivos intermediarios (switches, routers, firewalls, etc.):** 
  Necesitan IPs fijas para su administración, monitoreo y seguridad, ya que los administradores deben poder conectarse a ellos directamente.

- **Puertas de enlace (Gateways):** 
  Los routers o firewalls que conectan las redes suelen usar la primera o última dirección del rango de cada subred.

Un buen esquema de direccionamiento IP organiza cómo se asignan las direcciones según el tipo de dispositivo. Esto facilita el mantenimiento, mejora la seguridad, evita confusiones y simplifica la administración de la red.
