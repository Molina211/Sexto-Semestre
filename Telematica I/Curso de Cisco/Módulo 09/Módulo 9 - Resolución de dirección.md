# Módulo 9 - Resolución de dirección

---

## Contenido

- **MAC e IP:** Compara las funciones de la dirección MAC y de la dirección IP.

- **ARP:** Describe el propósito de ARP.

- **Detección de vecinos:** Describe el funcionamiento de la detección de vecinos IPv6.

---

### MAC e IP

Cuando un host solo conoce la dirección IP del destino, necesita descubrir su dirección MAC para poder comunicarse. 
En una red Ethernet, cada dispositivo tiene:

- **Dirección física (MAC):** Usada para la comunicación directa entre interfaces de red dentro de la misma LAN.

- **Dirección lógica (IP):** Usada para enviar paquetes entre redes.

Si el destino está en la misma red, la trama usa la MAC del dispositivo destino para la entrega local.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-10-20-50-image.png]]

PC1 quiere enviar un paquete a PC2. 
En la trama Ethernet (Capa 2) se usan las direcciones MAC:

- **Destino:** 55-55 (PC2)

- **Origen:** aa-aa-aa (PC1)

En el paquete IP (Capa 3) se usan las direcciones IPv4:

- **Origen:** 192.168.10.10 (PC1)

- **Destino:** 192.168.10.11 (PC2)



#### Destino en una red remota

Si la dirección IP de destino está en una red remota, el host usa como dirección MAC de destino la del gateway predeterminado (la interfaz del router), no la del dispositivo final.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-10-33-51-image.png]]

Cuando PC1 envía un paquete a PC2 en una red remota, usa la dirección MAC del router (gateway predeterminado) como destino. 
El router recibe la trama, la des encapsula, analiza la IP de destino y luego vuelve a encapsular el paquete con nuevas direcciones MAC para enviarlo al siguiente salto hacia PC2.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-10-35-28-image.png]]

En cada enlace del recorrido, el paquete IP se vuelve a encapsular en una trama nueva según la tecnología del enlace (por ejemplo, Ethernet). 
En este caso, la dirección MAC de destino pasa a ser la de la interfaz R2 G0/0/1, y la MAC de origen la de la interfaz R1 G0/0/1. 
Si el siguiente salto es el destino final, la MAC de destino será la del NIC del dispositivo receptor.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-10-36-53-image.png]]

Las direcciones IP de los paquetes se asocian con las direcciones MAC en cada enlace mediante ARP en IPv4 y ICMPv6 Neighbor Discovery (ND) en IPv6, permitiendo que los dispositivos encuentren la dirección física correspondiente a una dirección IP.

---

### ARP

En una red IPv4, ARP (Protocolo de Resolución de Direcciones) se encarga de asociar direcciones IPv4 con direcciones MAC. Cada dispositivo tiene una MAC única, y las tramas Ethernet incluyen:

- **MAC de destino:** Corresponde al dispositivo final en la misma red, o al gateway si está en otra red.

- **MAC de origen:** Corresponde a la tarjeta de red del dispositivo que envía la trama.

En pocas palabras: ARP traduce IP a MAC para que los dispositivos puedan comunicarse a nivel de Ethernet.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-14-33-30-image.png]]

Para enviar un paquete dentro de la misma red IPv4, un host necesita la IP y la MAC del destino. Mientras que la IP puede conocerse o resolverse por nombre, la MAC se obtiene usando ARP.

Las funciones principales de ARP son:

1. Resolver direcciones IPv4 a direcciones MAC.

2. Mantener una tabla con las asignaciones IP → MAC para uso futuro.



#### Funciones del ARP

Cuando un paquete llega a la capa de enlace para enviarse como trama Ethernet, el dispositivo revisa su tabla ARP (cache temporal en RAM) para asociar la IP de destino con su MAC.

- Si la IP de destino está en la misma red, busca directamente esa IP en la tabla ARP.

- Si la IP de destino está en otra red, busca la IP del gateway predeterminado.

Cada entrada de la tabla ARP enlaza una IP con una MAC (un “mapa”).

- Si la IP se encuentra, se usa la MAC correspondiente.

- Si no, se envía una solicitud ARP para descubrirla.



#### Solicitud ARP

Se envía una solicitud ARP cuando un dispositivo necesita la MAC asociada a una IP y no la tiene en su tabla ARP.

- La solicitud se encapsula en una trama Ethernet, sin usar IPv4, con:
  
  - **MAC de destino:** Broadcast (todas las NIC de la LAN reciben la solicitud).
  
  - **MAC de origen:** Del remitente.
  
  - **Tipo:** 0x806, indicando que es ARP.

- Los switches envían el broadcast a todos los puertos excepto al de recepción.

- Todas las NIC reciben la solicitud y solo el dispositivo cuya IP coincide responde.

- Los routers no reenvían broadcasts a otras redes.



#### Respuesta ARP

Solo el dispositivo cuya IP coincide con la solicitud ARP responde con una respuesta ARP encapsulada en una trama Ethernet:

- **MAC de destino:** Del remitente de la solicitud.

- **MAC de origen:** Del dispositivo que responde.

- **Tipo:** 0x806 (indica ARP).

La respuesta se envía por unicast al solicitante, que luego actualiza su tabla ARP con la IP y MAC correspondientes. Si no hay respuesta, el paquete se descarta.

- Las entradas ARP tienen marca de tiempo y caducan si no se usan.

- Se pueden crear entradas ARP estáticas, que no caducan y deben eliminarse manualmente.

En IPv6, un proceso similar llamado ICMPv6 Neighbor Discovery cumple la misma función.



#### Rol ARP en Comunicaciones Remotas

Cuando un host necesita enviar un paquete a una IP que está en otra red, no puede enviarlo directamente al dispositivo destino, sino que debe enviarlo al gateway predeterminado (la interfaz del router local que conecta su red con otras redes).

- El host encapsula el paquete en una trama Ethernet usando la MAC del gateway predeterminado como destino.

- La IP del gateway ya está configurada en el host como parte de su configuración IPv4.

- El host compara la IP de destino con la suya propia para ver si están en la misma red.
  
  - Si no lo están, busca en su tabla ARP la MAC del gateway.
  
  - Si no encuentra la MAC, envía una solicitud ARP para obtenerla.

Entonces, cuando la IP de destino está fuera de la red local, el paquete se envía al router local usando ARP si es necesario para conocer la MAC del gateway. Esto asegura que los datos lleguen a la red correcta aunque el host no conozca la MAC del dispositivo final.



#### Eliminación de entradas de una tabla ARP

Cada dispositivo tiene un temporizador de la cache ARP que elimina automáticamente las entradas que no se usan durante un tiempo determinado.

- La duración varía según el sistema operativo.

- Por ejemplo, en Windows recientes, las entradas ARP se mantienen entre 15 y 45 segundos antes de caducar.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-16-10-04-image.png]]

Se pueden eliminar manualmente algunas o todas las entradas de la tabla ARP mediante comandos.

- Después de eliminar una entrada, el dispositivo debe realizar de nuevo el proceso ARP (solicitud y respuesta) para volver a registrar la asignación IP → MAC en la tabla.



#### Tablas ARP en dispositivos de red

En un router Cisco, el `show ip arp` comando se utiliza para mostrar la tabla ARP, como se muestra en la figura.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-16-15-39-image.png]]

En una PC con Windows 10, el `arp -a` comando se usa para mostrar la tabla ARP, como se muestra en la figura.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-16-16-31-image.png]]



#### Problemas de ARP - Difusión ARP y suplantación ARP

Todos los dispositivos de la red local reciben las solicitudes ARP porque son tramas de difusión. En una red comercial esto normalmente no afecta el rendimiento. Sin embargo, si muchos dispositivos se conectan al mismo tiempo, puede haber una breve disminución de rendimiento debido al aumento de solicitudes ARP. Una vez que los dispositivos aprenden las direcciones MAC necesarias, el impacto en la red desaparece.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-16-17-46-image.png]]

El uso de ARP puede ser aprovechado por atacantes para realizar suplantación o envenenamiento ARP, una técnica en la que un atacante envía respuestas ARP falsas para asociar su dirección MAC con la IP de otro dispositivo, como la puerta de enlace. Esto hace que el tráfico se redirija hacia el atacante. Para evitarlo, los switches empresariales utilizan medidas de protección como la Inspección Dinámica de ARP (DAI), aunque este tema no se profundiza en este curso.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-16-25-29-image.png]]

---

### Detección de vecinos IPv6

En redes que usan IPv6, el protocolo ARP no se utiliza. En su lugar se usa el Protocolo de Detección de Vecinos (ND), que se encarga de asociar direcciones IPv6 con direcciones MAC.

El descubrimiento de vecinos (ND) en IPv6 usa mensajes ICMPv6 para funciones como resolver direcciones, detectar routers y redirigir tráfico. Utiliza cinco tipos de mensajes:

- **NS** (Neighbor Solicitation)

- **NA** (Neighbor Advertisement)

- **RS** (Router Solicitation)

- **RA** (Router Advertisement)

- **Redirect**

Los mensajes NS y NA permiten que los dispositivos obtengan la dirección MAC correspondiente a una dirección IPv6, similar a cómo ARP funciona en IPv4.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-16-41-47-image.png]]

Los mensajes RS y RA permiten que los dispositivos descubran routers en la red. Estos mensajes se usan principalmente para asignar direcciones IPv6 de forma automática mediante SLAAC.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-16-42-25-image.png]]

El quinto mensaje de ND, llamado Redirect, sirve para indicar a un dispositivo una mejor ruta para enviar sus paquetes, mejorando el tráfico en la red. Aunque existe, no se estudia en este curso. Todo el funcionamiento de ND está definido en el estándar RFC 4861 del IETF.



#### Descubrimiento de vecinos IPv6 - Resolución de direcciones

En IPv6, la resolución de direcciones MAC se hace con el protocolo ND, usando los mensajes **Neighbor Solicitation (NS)** y **Neighbor Advertisement (NA)**, que cumplen la misma función que ARP en IPv4. Por ejemplo, si una PC quiere comunicarse con otra usando su dirección IPv6, primero envía un mensaje NS para averiguar la dirección MAC del destino.

![[Telematica I/Curso de Cisco/Módulo 09/ANEXOS/2025-10-22-16-44-49-image.png]]

Los mensajes Neighbor Solicitation se envían a direcciones multicast especiales para que solo el dispositivo correspondiente los procese. Luego, el dispositivo destino responde con un mensaje Neighbor Advertisement que contiene su dirección MAC.


