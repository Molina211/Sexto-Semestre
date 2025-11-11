# Módulo 13 - ICMP

---

## Contenido

- **Mensajes ICMP:** Explica la forma en que se usa ICMP para probar la conectividad de red.

- **Pruebas de ping y traceroute:** Utiliza las utilidades de ping y traceroute para probar la conectividad de red.

---

### Mensajes ICMP

El protocolo ICMP (para IPv4 e IPv6) se usa para enviar mensajes de control e información relacionados con el procesamiento de paquetes IP. 
Aunque IP no garantiza la entrega, ICMP permite reportar errores y condiciones de red, pero no hace que IP sea confiable. 
Por motivos de seguridad, a veces se bloquea su uso en redes. 
Entre los mensajes ICMP más comunes están:

- **Accesibilidad al host**

- **Destino o servicio inaccesible**

- **Tiempo superado**

#### Accesibilidad al host

El mensaje de eco ICMP se utiliza para comprobar la accesibilidad de un host en una red IP. 
El host local envía una solicitud de eco ICMP y, si el host de destino está disponible, responde con una respuesta de eco. 
Este intercambio es la base del comando ping, que permite verificar la conectividad de red.

#### Destino o servicio inaccesible

Cuando un host o gateway no puede entregar un paquete, envía un mensaje ICMP de destino inalcanzable al origen para informar el motivo del fallo.

**Códigos ICMPv4 más comunes:**

- 0: red inalcanzable

- 1: host inalcanzable

- 2: protocolo inalcanzable

- 3: puerto inalcanzable

**Códigos ICMPv6 más comunes:**

- 0: no hay ruta al destino

- 1: comunicación prohibida (por firewall u otra restricción)

- 2: destino fuera del alcance

- 3: dirección inalcanzable

- 4: puerto inalcanzable

#### Tiempo excedido

Los mensajes ICMP de tiempo superado se envían cuando un paquete expira antes de llegar a su destino. 
En IPv4, esto ocurre cuando el TTL llega a 0, y en IPv6, cuando el límite de salto se agota. 
El router descarta el paquete y notifica al origen con un mensaje de tiempo excedido. 
Esta función es la base de la herramienta traceroute, que permite rastrear la ruta de un paquete a través de la red.

#### Mensajes ICMPv6

ICMPv6 es similar a ICMPv4, pero incluye nuevas funciones mediante el Protocolo de Detección de Vecinos (NDP). 
Estos mensajes permiten la asignación dinámica de direcciones, la detección de direcciones duplicadas y la resolución de direcciones.

**Mensajes entre router y dispositivo:**

- RS (Router Solicitation)

- RA (Router Advertisement)

**Mensajes entre dispositivos:**

- NS (Neighbor Solicitation)

- NA (Neighbor Advertisement)

También incluye un mensaje de redirección, equivalente al de ICMPv4, para optimizar el enrutamiento.

1. **Mensaje RA:** Los mensajes de Anuncio de Router (RA) son enviados por los enrutadores IPv6 cada 200 segundos para informar a los hosts sobre parámetros de red, como el prefijo, longitud del prefijo, dirección DNS y nombre de dominio  
   Un host que usa SLAAC configura su puerta de enlace predeterminada con la dirección de enlace local del enrutador que envió el mensaje RA.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-11-01-01-59-02-image.png" title="" alt="" data-align="center">

*R1 envia un mensaje de RA, «Hola a todos los dispositivos habilitados para IPv6. Soy R1 y puedes usar SLAAC para crear una dirección de unidifusión global IPv6. El prefijo es 2001:db8:acad:1: :/64. Por cierto, use mi dirección local de enlace fe80: :1 como su puerta de enlace predeterminada.*

2. **Mensajes RS:** Un router IPv6 envía un mensaje RA en respuesta a un mensaje de Solicitud de Router (RS) enviado por un host, como PC1, para obtener de forma dinámica su información de dirección IPv6.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-11-01-02-03-18-image.png" title="" alt="" data-align="center">

*R1 responde a la RS con un mensaje de RA.*

1. *PC1 envia un mensaje RS, «Hola, acabo de arrancar. ¿Hay un enrutador IPv6 en la red? Necesito saber como obtener la información de mi dirección IPv6 de forma dinámica».*
2. *R1 responde con un mensaje de RA. «Hola a todos los dispositivos habilitados para IPv6. Soy R1 y puedes usar SLAAC para crear una dirección de unidifusión global IPv6. El prefijo es 2001:db8:acad:1: :/64. Por cierto, use mi dirección
   local de enlace fe80: :1 como su puerta de enlace predeterminada.*

3. **Mensaje NS:** La Detección de Dirección Duplicada (DAD) permite verificar que una dirección IPv6 sea única. 
   El dispositivo envía un mensaje de Solicitud de Vecino (NS) usando su propia dirección como objetivo. 
   Si otro dispositivo tiene esa dirección, responde con un mensaje de Anuncio de Vecino (NA) indicando que está en uso. 
   Si no hay respuesta, la dirección se considera única y válida. 
   Aunque no es obligatoria, laRFC 4861 recomienda realizar DAD para las direcciones unicast.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-11-01-02-07-39-image.png" title="" alt="" data-align="center">

*PC1 envia un mensaje NS para comprobar la singularidad de una direccion, «¿Quién tiene la direccion IPv6 2001:db8:acad:1::10, me enviará su dirección MAC? «*

---

### Pruebas de ping y traceroute

El comando ping se usa en IPv4 e IPv6 para probar la conectividad entre hosts mediante mensajes ICMP de solicitud y respuesta de eco. 
Permite medir el tiempo de ida y vuelta (latencia) y verificar el rendimiento de la red.

Si no hay respuesta dentro del tiempo de espera, puede indicar un problema de red o bloqueo por seguridad. 
El primer ping puede fallar debido a la resolución de direcciones (ARP o ND).

Al finalizar, muestra un resumen con la tasa de éxito y el tiempo promedio. 
Se puede usar para tres tipos de pruebas:

1. **Ping al loopback local** (verifica la pila TCP/IP).

2. **Ping a la puerta de enlace predeterminada** (verifica la red local).

3. **Ping a un host remoto** (verifica la conectividad fuera de la red local).



#### Hacer ping al loopback

El ping al loopback local (127.0.0.1 en IPv4 o ::1 en IPv6) verifica que el protocolo IP esté instalado y funcionando correctamente en el host. 
Confirma el funcionamiento de la capa de red, pero no valida la configuración de direcciones, máscaras o puertas de enlace, ni el estado de las capas inferiores. 
Si aparece un mensaje de error, significa que TCP/IP no funciona correctamente en el dispositivo.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-11-01-19-06-45-image.png" title="" alt="" data-align="center">

1. *Hacer ping al host local permite confirmar que el protocolo TCP/IP se encuentra instalado en el host y que funciona.*

2. *Hacer ping a 127.0.0.1 ocasiona que un dispositivo se haga ping a sí mismo.*



#### Hacer ping al gateway predeterminado

El ping a la puerta de enlace predeterminada verifica si el host puede comunicarse dentro de la red local.

- Si la puerta de enlace responde, el host y el router funcionan correctamente.

- Si no responde, se puede probar con otro host de la red.

- Si otro host responde pero la puerta de enlace no, puede haber un problema en la interfaz del router o una configuración incorrecta de la puerta de enlace en el host.

- También es posible que el router tenga medidas de seguridad que bloqueen las solicitudes de ping.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-11-01-19-08-56-image.png" title="" alt="" data-align="center">

*El host hace ping a su puerta de enlace predeterminada, enviando una solicitud de eco ICMP. La puerta de enlace predeterminada envía una respuesta de eco confirmando la conectividad.*



#### Hacer ping a un Host Remoto

El ping a un host remoto permite comprobar la conectividad entre redes.

- Si tiene éxito, confirma el funcionamiento de toda la ruta, incluyendo la red local, la puerta de enlace predeterminada, y todos los routers intermedios hasta el destino.

- También verifica que el módulo remoto de E/S puede comunicarse fuera de su red local.

- Si no hay respuesta, puede deberse a restricciones de seguridad que bloquean mensajes ICMP en la red corporativa.



#### Traceroute - Prueba el Camino

El comando ping sirve para comprobar si hay conectividad entre dos dispositivos (hosts), pero no muestra qué hay en medio de la ruta.

En cambio, traceroute (o tracert en Windows) muestra cada salto (router) por el que pasa un paquete hasta llegar al destino. Esto permite identificar dónde hay retrasos o fallas en la red.

Cada salto muestra su tiempo de ida y vuelta (RTT), es decir, cuánto tarda el paquete en ir y volver.

- Si aparece un asterisco (*), significa que ese salto no respondió o el paquete se perdió.

- Si los tiempos son altos o hay pérdidas, puede indicar sobrecarga o problemas en ese router o enlace.

Traceroute funciona modificando el campo TTL (Time To Live) en IPv4 o el Límite de salto en IPv6. 
Cuando el TTL llega a cero, el router envía un mensaje ICMP Time Exceeded, lo que permite identificarlo y mostrarlo en la lista de saltos.

Entonces, traceroute permite diagnosticar el recorrido y rendimiento de la ruta entre dos hosts, detectando dónde puede estar el problema en la red.

<img src="file:///C:/Users/Molina211/AppData/Roaming/marktext/images/2025-11-01-19-14-07-image.png" title="" alt="" data-align="center">

Traceroute envía paquetes con un TTL inicial de 1, que expira en el primer router, generando un mensaje ICMP “Tiempo excedido". Luego aumenta el TTL (2, 3, 4, …) para descubrir cada salto intermedio.

El proceso continúa hasta que los paquetes llegan al destino final, que responde con un mensaje ICMP de eco o puerto inalcanzable.
