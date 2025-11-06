# Módulo 14 - Capa de transporte

---

## Contenido

- **Transporte de datos:** Explica el propósito de la capa de transporte en la administración del transporte de datos en comunicación extremo a extremo.

- **Descripción general de TCP:** Explica las características de TCP.

- **Visión general de UDP:** Explica las características de UDP.

- **Números de puerto:** Explica cómo TCP y UDP usan los números de puerto.

- **Proceso de comunicación TCP:** Explicar las características de TCP. Facilitar na comunicación fiable.

- **Confiabilidad y control de flujo:** Explica cómo se transmite y reconocen las unidades de datos del protocolo TCP a Entrega garantizada.

- **Comunicación UDP:** Compara las operaciones de los protocolos de la capa de transporte en el soporte comunicación de extremo a extremo.

---

### Transporte de datos

La capa de transporte permite la comunicación lógica entre aplicaciones en distintos hosts, estableciendo sesiones temporales y garantizando la transmisión confiable de datos. Actúa como enlace entre la capa de aplicación y las capas inferiores encargadas de la transmisión en la red.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-20-45-13-image.png]]

La capa de transporte no considera el tipo de host, medio, ruta, congestión ni tamaño de la red. Utiliza dos protocolos principales: TCP, que ofrece transmisión confiable, y UDP, que proporciona una comunicación más rápida pero sin garantía de entrega.



#### Responsabilidades de la capa de transporte

1. **Seguimiento de conversaciones individuales:** La capa de transporte se encarga de gestionar y seguir cada conversación entre aplicaciones de origen y destino, incluso si hay varias al mismo tiempo. 
   Como los paquetes tienen un tamaño limitado, esta capa divide los datos en partes más pequeñas para que puedan enviarse correctamente por la red y luego sean reensamblados al llegar al destino.
   
   **Analogía:** 
   Es como un operador telefónico que mantiene activas varias llamadas al mismo tiempo y sabe a quién pertenece cada una. 
   **Ejemplo:** 
   Mientras descargas un archivo y haces una videollamada, la capa de transporte mantiene ambas conexiones sin mezclarlas.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-20-51-39-image.png]]

2. **Segmentación de datos y rearmado de segmentos:** La capa de transporte divide los datos en bloques más pequeños llamados segmentos (TCP) o datagramas (UDP), según el protocolo usado. 
   Esto permite que la información sea más fácil de enviar, manejar y reconstruir cuando llega al destino, asegurando una comunicación eficiente entre aplicaciones.
   
   **Analogía:** 
   Es como dividir un libro grande en varios sobres para enviarlo por correo; cada sobre lleva una parte del libro. 
   **Ejemplo:** 
   Un correo electrónico grande se divide en varios paquetes que se envían por separado y luego se reconstruyen en el destino.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-20-55-52-image.png]]

3. **Agregar información de encabezado:** La capa de transporte agrega encabezados a cada bloque de datos, con información que permite administrar y controlar la comunicación. 
   El host receptor usa estos encabezados para reensamblar los datos* en el orden correcto y entregarlos a la aplicación correspondiente, asegurando que cada programa reciba su información sin errores ni confusión.
   
   **Analogía:** 
   Como si cada sobre tuviera una etiqueta con el número de página y el destinatario, para poder armar el libro en el orden correcto. 
   **Ejemplo:** 
   Los paquetes de un archivo descargado se numeran y reordenan al llegar para que el archivo no se dañe.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-20-57-02-image.png]]

4. **Identificación de las aplicaciones:** La capa de transporte usa números de puerto para identificar y dirigir los datos a la aplicación correcta dentro de un host. 
   Cada programa que se comunica por la red tiene un número de puerto único, lo que permite manejar varias conexiones simultáneas con distintos requisitos de transporte sin que los datos se mezclen. 
   
   **Analogía:** 
   Es como un edificio con muchos apartamentos, donde la dirección (IP) es el edificio y el número de apartamento es el puerto. 
   **Ejemplo:** 
   El navegador usa el puerto 80 o 443 (HTTP/HTTPS), mientras el correo usa 25 o 587 (SMTP); ambos pueden funcionar al mismo tiempo.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-20-58-12-image.png]]

5. **Multiplexión de conversaciones:** La capa de transporte utiliza segmentación y multiplexación para dividir los datos y enviar múltiples conversaciones simultáneamente sin saturar la red. 
   Esto permite compartir el ancho de banda entre varias aplicaciones y verificar errores en cada segmento, garantizando que los datos no se hayan dañado durante la transmisión.
   
   **Analogía:** 
   Es como una autopista donde varios autos (conversaciones) usan distintos carriles pero comparten el mismo camino, y un peaje revisa los autos dañados (verificación de errores). 
   **Ejemplo:** 
   Puedes ver un video en streaming mientras chateas, y la capa de transporte mantiene ambas transmisiones sin interferencias y detecta si algún paquete se corrompe.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-20-59-14-image.png]]



#### Protocolos de capa de transporte

El protocolo IP se encarga de direccionar y enrutar los paquetes, pero no de su entrega confiable. 
Esa función corresponde a la capa de transporte, que define cómo se transfieren los mensajes entre hosts y gestiona la fiabilidad de la comunicación. 
Por eso, existen dos protocolos principales: TCP, que ofrece transmisión confiable, y UDP, que brinda una comunicación más rápida pero sin verificación de entrega.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-21-05-40-image.png]]



#### Protocolo de control de transmisión (TCP)

El protocolo IP solo se encarga de enrutar y direccionar los paquetes, pero no garantiza su entrega ni establece conexiones entre los hosts. 
En cambio, el protocolo TCP sí ofrece transmisión confiable y controlada, asegurando que todos los datos lleguen correctamente al destino.

TCP divide los datos en segmentos y utiliza mecanismos como:

- Numeración y seguimiento de los segmentos enviados.

- Confirmaciones (ACKs) para verificar la recepción.

- Retransmisión de datos perdidos.

- Reordenamiento de paquetes que lleguen fuera de secuencia.

- Control de flujo, ajustando la velocidad según lo que el receptor pueda manejar.

Por eso, TCP se denomina protocolo orientado a la conexión, ya que establece una sesión previa entre emisor y receptor antes de transmitir los datos, garantizando entrega ordenada, completa y confiable, como si se rastrearan paquetes en un envío con seguimiento.

---
### Protocolo de datagramas de usuario (UDP)

UDP (User Datagram Protocol) es un protocolo de transporte simple y rápido que no garantiza la entrega ni controla el flujo de datos.

A diferencia de TCP, no establece una conexión entre el emisor y el receptor, por lo que se considera un protocolo sin conexión y sin estado. Esto significa que no se verifica si los datos llegan correctamente ni en qué orden.

Los datos se envían en datagramas, que son unidades independientes de información. UDP simplemente los entrega a la aplicación destino sin comprobar errores o pérdidas.

Por su bajo consumo de recursos y rapidez, UDP se usa en aplicaciones donde la velocidad es más importante que la confiabilidad, como transmisión de video, voz o juegos en línea.



#### Protocolo de la capa de transporte correcto para la aplicación adecuada

**UDP (User Datagram Protocol):**

- Ideal para aplicaciones en tiempo real donde la velocidad es más importante que la fiabilidad, como Voz sobre IP (VoIP) o video en vivo.

- Tolera la pérdida de algunos datos, pero no acepta retrasos.

- No utiliza reconocimientos ni retransmisiones, lo que reduce la sobrecarga de red.

- También se usa en aplicaciones simples con pocos datos, como DNS, donde si no hay respuesta, el cliente simplemente vuelve a enviar la solicitud.

- En transmisiones en vivo, algunos datos perdidos solo causan pequeñas distorsiones que no siempre se notan.

**TCP (Transmission Control Protocol):**

- Se usa cuando la confiabilidad y el orden de los datos son esenciales.

- Ideal para navegadores web, correo electrónico, bases de datos o transacciones bancarias, donde cada dato debe llegar completo y en orden.

- Incluye mecanismos de control de flujo, congestión y retransmisión, lo que garantiza precisión pero introduce más retraso.

- En videos almacenados (como películas bajo demanda), TCP permite pausar la reproducción para almacenar en búfer hasta que la conexión se estabilice.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-21-15-56-image.png]]

---

### Descripción general de TCP

TCP (Transmission Control Protocol) es un protocolo de transporte confiable y orientado a la conexión, usado cuando es necesario garantizar que los datos lleguen completos y en el orden correcto.

Además de dividir y reensamblar los datos, TCP ofrece servicios adicionales que aseguran una comunicación estable y segura:

1. **Establecimiento de sesión:**
   
   - Antes de enviar datos, TCP crea una conexión entre el emisor y el receptor.
   
   - Ambos dispositivos negocian cuánta información pueden enviarse a la vez.

2. **Entrega confiable:**
   
   - TCP verifica que cada segmento llegue correctamente al destino.
   
   - Si un segmento se pierde o se daña, se retransmite.

3. **Entrega en orden:**
   
   - Numerando los segmentos, TCP reordena los datos si llegan fuera de secuencia, garantizando que el mensaje final sea correcto.

4. **Control de flujo:**
   
   - TCP regula la velocidad de transmisión para evitar que el receptor se sature si tiene pocos recursos.



#### Encabezade TCP

TCP es un protocolo con estado, lo que significa que mantiene un registro de toda la comunicación entre el emisor y el receptor. 
Durante la sesión, TCP controla qué datos se enviaron y cuáles fueron confirmados (reconocidos), garantizando una transmisión ordenada y confiable.

La sesión con estado comienza cuando se establece la conexión y finaliza cuando se cierra correctamente.

Además, cada segmento TCP incluye un encabezado de 20 bytes que contiene información necesaria para gestionar esta conexión, como números de secuencia, confirmaciones y control de flujo.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-21-20-50-image.png]]



#### Campos de encabezado TCP

| Campo de Encabezado TCP   | Descripción                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Puerto de Origen          | Campo de 16 bits utilizado para identificar la aplicación de origen por número de puerto.                        |
| Puerto de Destino         | Campo de 16 bits utilizado para identificar la aplicación de destino por número de puerto.                       |
| Secuencia de Números      | Campo de 32 bits utilizado para reensamblar datos.                                                               |
| Número de Acuse de Recibo | Campo de 32 bits utilizado para indicar que se han recibido datos y el siguiente byte esperado de la fuente.     |
| Longitud del Encabezado   | Campo de 4 bits conocido como «desplazamiento de datos» que indica la longitud del encabezado del segmento TCP.  |
| Reservado                 | Campo de 6 bits que está reservado para uso futuro.                                                              |
| Bits de Control           | Campo de 6 bits que incluye códigos de bits, o indicadores, que indican el propósito y función del segmento TCP. |
| Tamaño de la ventana      | Campo de 16 bits utilizado para indicar el número de bytes que se pueden aceptar a la vez.                       |
| Suma de Comprobación      | Campo de 16 bits utilizado para la verificación de errores del encabezado y datos del segmento.                  |
| Urgente                   | Campo de 16 bits utilizado para indicar si los datos contenidos son urgentes.                                    |



#### Aplicaciones que utilizan TCP

TCP se encarga de gestionar todo el proceso de transmisión de datos, dividiendo la información en segmentos, asegurando su entrega confiable, manteniendo el orden correcto y controlando el flujo.

De esta forma, las aplicaciones no necesitan preocuparse por estos detalles, ya que TCP realiza todas esas funciones automáticamente. 
Las aplicaciones solo envían los datos a la capa de transporte, y TCP se encarga del resto.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-21-24-35-image.png]]

---

### Visión general UDP

UDP es un protocolo de transporte simple y liviano, conocido como protocolo de mejor esfuerzo, ya que no garantiza la entrega ni el orden de los datos.

Ofrece segmentación y reensamblado como TCP, pero sin confiabilidad ni control de flujo.

Sus principales características son:

- No establece conexión previa entre emisor y receptor.

- No retransmite los segmentos perdidos.

- Reconstruye los datos en el orden recibido, sin correcciones.

- No verifica la disponibilidad de recursos en el destino.



#### Encabezado UDP

UDP es un protocolo sin estado, lo que significa que no guarda información sobre la comunicación* entre el cliente y el servidor. 
Si una aplicación necesita confiabilidad, debe gestionarla por sí misma, no mediante UDP.

Es ideal para video y voz en vivo, donde la velocidad es más importante que la precisión, y se puede tolerar cierta pérdida de datos sin afectar mucho la calidad.

Los datos se envían en datagramas, transmitidos con entrega de mejor esfuerzo. 
Además, su encabezado es muy simple, con solo 4 campos y 8 bytes, lo que hace que UDP sea más rápido y liviano que TCP.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-21-29-39-image.png]]



#### Campos de encabezado UDP

| Campo de Encabezado UDP | Descripción                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Puerto de Origen        | Campo de 16 bits utilizado para identificar la aplicación de origen por número de puerto.            |
| Puerto de Destino       | Campo de 16 bits utilizado para identificar la aplicación de destino por número de puerto.           |
| Longitud                | Campo de 16 bits que indica la longitud del encabezado del datagrama UDP.                            |
| Suma de Comprobación    | Campo de 16 bits utilizado para la comprobación de errores del encabezado y los datos del datagrama. |



#### Aplicaciones que utilizan UDP

UDP se usa principalmente en tres tipos de aplicaciones:

1. **Video y multimedia en vivo:**
   
   - Requieren bajo retraso y pueden tolerar pérdidas de datos.
   
   - Ejemplos: VoIP y transmisión de video en vivo.

2. **Solicitudes simples de respuesta:**
   
   - Realizan transacciones rápidas donde puede o no haber respuesta.
   
   - Ejemplos: DNS y DHCP.

3. **Aplicaciones que gestionan su propia confiabilidad:**
   
   - No necesitan que UDP controle errores o flujo porque la aplicación lo hace.
   
   - Ejemplos: SNMP y TFTP.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-21-31-45-image.png]]

Aunque DNS y SNMP usan UDP por defecto, también pueden usar TCP en ciertos casos:

- DNS usa TCP cuando la solicitud o respuesta supera los 512 bytes, por ejemplo, si hay muchas resoluciones de nombre.

- SNMP puede configurarse para usar TCP si el administrador de red lo considera necesario.

---

### Número de puerto

Tanto TCP como UDP usan números de puerto para identificar las aplicaciones que envían y reciben datos, y así manejar varias conexiones al mismo tiempo.

Cada encabezado de estos protocolos incluye un puerto de origen y un puerto de destino, que permiten dirigir correctamente los datos entre los distintos procesos o servicios de red.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-01-21-34-55-image.png]]

El puerto de origen identifica la aplicación que envía los datos desde el host local, mientras que el puerto de destino identifica la aplicación o servicio en el host remoto.

Cuando un cliente hace una solicitud (por ejemplo, abrir una página web), se genera dinámicamente un puerto de origen para diferenciar esa conexión. Así, un mismo host puede mantener múltiples conversaciones simultáneas.

El puerto de destino indica el servicio solicitado, como:

- **Puerto 80:** servicio web (HTTP).

- **Puerto 21:** servicio FTP.



#### Pares de sockets

Los puertos de origen y destino van dentro del segmento TCP o UDP, y este segmento se encapsula en un paquete IP, que contiene las direcciones IP de origen y destino.

La combinación de una dirección IP y un número de puerto se llama socket, y sirve para identificar de forma única cada conexión entre dos dispositivos.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-02-13-16-38-image.png]]

En una comunicación, cada solicitud del cliente incluye direcciones MAC (Capa 2), direcciones IP (Capa 3) y números de puerto (Capa 4).

Por ejemplo:

- Una solicitud FTP usa el puerto de destino 21 y un puerto de origen dinámico (como 1305).

- Una solicitud web (HTTP) usa el puerto de destino 80 y otro puerto de origen dinámico (como 1099).

La combinación de dirección IP + número de puerto forma un socket:

- Cliente: `192.168.1.5:1099`

- Servidor: `192.168.1.7:80` 
  Juntos forman un par de sockets que identifica de manera única la conexión entre ambos.



#### Grupos de números en puertos

La IANA (Autoridad de Números Asignados de Internet) es la entidad encargada de asignar los números de puerto usados en las comunicaciones de red.

Cada puerto se identifica con un número de 16 bits, por lo que existen 65,536 puertos posibles (del 0 al 65,535).

| Grupo de puertos               | Rango de números | Descripción                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Puertos bien conocidos         | 0 a 1,023        | • Estos números de puerto están reservados para servicios comunes o populares y aplicaciones como navegadores web, clientes de correo electrónico y acceso remoto clientes.<br>• Los puertos conocidos definidos para aplicaciones de servidor comunes permiten identificar fácilmente el servicio asociado requerido.                                                                                                   |
| Puertos registrados            | 1,024 a 49,151   | • Estos números de puerto son asignados por IANA a una entidad solicitante para utilizar con procesos o aplicaciones específicos.<br>• Estos procesos son principalmente aplicaciones individuales que un usuario ha elegido instalar, en lugar de aplicaciones comunes que reciben un número de puerto conocido.<br>• Por ejemplo, Cisco ha registrado el puerto 1812 para su servidor RADIUS proceso de autenticación. |
| Puertos privados y/o dinámicos | 49,152 a 65,535  | • Estos puertos también se conocen como puertos efímeros.<br>• El sistema operativo del cliente generalmente asigna números de puerto dinámicamente cuando se inicia una conexión a un servicio.<br>• El puerto dinámico se utiliza para identificar la aplicación del cliente durante la comunicación.                                                                                                                  |

Algunos sistemas operativos pueden usar puertos registrados (en lugar de los dinámicos) como puertos de origen al iniciar conexiones.

Además, existen puertos bien conocidos asignados a servicios específicos, como:

| Número de puerto | Protocolo | Aplicación                                                   |
| ---------------- | --------- | ------------------------------------------------------------ |
| 20               | TCP       | Protocolo de transferencia de archivos (FTP) - Datos         |
| 21               | TCP       | Protocolo de transferencia de archivos (FTP) - Control       |
| 22               | TCP       | Secure Shell (SSH)                                           |
| 23               | TCP       | Telnet                                                       |
| 25               | TCP       | Protocolo simple de transferencia de correo (SMTP)           |
| 53               | UDP, TCP  | Servicio de nombres de dominio (DNS)                         |
| 67               | UDP       | Protocolo de configuración dinámica de host (DHCP): servidor |
| 68               | UDP       | Protocolo de configuración dinámica de host (DHCP): cliente  |
| 69               | UDP       | Protocolo trivial de transferencia de archivos (TFTP)        |
| 80               | TCP       | Protocolo de transferencia de hipertexto (HTTP)              |
| 110              | TCP       | Protocolo de oficina de correos, versión 3 (POP3)            |
| 143              | TCP       | Protocolo de acceso a mensajes de Internet (IMAP)            |
| 161              | UDP       | Protocolo simple de administración de redes (SNMP)           |
| 443              | TCP       | Protocolo seguro de transferencia de hipertexto (HTTPS)      |

Algunas aplicaciones usan tanto TCP como UDP. 
Por ejemplo, DNS utiliza UDP para las consultas de los clientes, pero TCP para la comunicación entre servidores DNS. 
La IANA mantiene una lista oficial de los números de puerto y las aplicaciones asociadas que se puede consultar en su sitio web.



#### El comando netstat

Las conexiones TCP no identificadas pueden ser una amenaza de seguridad, ya que podrían indicar accesos no autorizados al host. 
La utilidad Netstat permite verificar las conexiones TCP activas, mostrando los protocolos en uso, direcciones locales y remotas, números de puerto y el estado de cada conexión mediante el comando `netstat`.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-02-13-26-34-image.png]]

Por defecto, el comando Netstat intenta resolver las direcciones IP y números de puerto a sus nombres de dominio y aplicaciones conocidas. 
Usar la opción `-n` muestra las direcciones IP y puertos en formato numérico, evitando esa resolución.

---

### Proceso de comunicación TCP

Cada proceso de aplicación en un servidor utiliza un número de puerto, asignado automáticamente o configurado por un administrador.

- No se pueden asignar dos servicios al mismo puerto dentro de la misma capa de transporte. Por ejemplo, un servidor no puede usar el puerto 80 para HTTP y FTP al mismo tiempo.

- Un puerto de servidor activo se considera abierto, lo que significa que la capa de transporte acepta y procesa los segmentos dirigidos a ese puerto.

- Un servidor puede tener varios puertos abiertos simultáneamente, uno por cada aplicación activa, permitiendo múltiples servicios al mismo tiempo.

Los procesos del servicio TCP son:

1. **Clientes envía solicitudes TCP:**
   
   El Cliente 1 esta solicitando servicios web y el Cliente 2 esta solicitando servicio de correo electronico del mismo servidor.
   
![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-02-14-03-42-image 1.png]]

2. **Solicitar puertos de destino:**
   
   Las solicitudes generan dinamicamente un número de puerto de origen. En este caso, el Cliente 1 esta utilizando el puerto de origen 49152 y el cliente 2 esta utilizando el puerto de origen 51152.
   
![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-02-14-04-42-image.png]]

3. **Solicitar puertos de origen:**
   
   Las solicitudes de Cliente generan dinamicamente un número de puerto de origen. En este caso, el Cliente 1 esta utilizando el puerto de origen 49152 y el Cliente 2 esta utilizando el puerto de origen 51152.
   
![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-02-14-05-37-image.png]]

4. **Respuesta de puertos de destino:**
   
   Cuando el servidor responde a las solicitudes del Cliente, invierte los puertos de destino y origen de la solicitud inicial. Observe que la respuesta del servidor a la solicitud web ahora tiene el puerto de destino 49152 y la respuesta de correo electrónico ahora tiene el puerto de destino 51152.
   
![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-02-14-06-45-image.png]]

5. **Respuesta de puertos de origen:**
   
   El puerto de origen en la respuesta del servidor es el puerto de destino original en las solicitudes iniciales.
   
![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/2025-11-02-14-08-10-image.png]]



#### Establecimiento de conexiones TCP

En TCP, el establecimiento de una conexión funciona como un apretón de manos: el cliente y el servidor acuerdan iniciar la comunicación mediante el proceso de enlace de tres vías (three-way handshake), que asegura que ambos estén listos para transmitir datos.

1. **SYN:**

   El cliente de origen solicita una sesión de comunicación con el servidor.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251102235620.png]]

2. **ACK y SYN:**

   El servidor acusa recibo de la sesión de comunicación de cliente a servidor y solicita una sesión de comunicación de servidor a cliente.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251102235926.png]]

3. **ACK**

   El cliente de origen acusa recibo de la sesión de comunicación de servidor a cliente.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103000029.png]]



#### Terminación de sesión

Para cerrar una conexión TCP, se usa el marcador FIN en el encabezado del segmento.  
La finalización completa requiere cuatro intercambios (FIN y ACK por cada lado), ya que cada dirección de la comunicación se cierra por separado.  
Tanto el cliente como el servidor pueden iniciar este proceso.

1. **FIN**

   Cuando el cliente no tiene mas datos para enviar en la transmisión, envía un segmento con el indicador FIN establecido.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103000319.png]]

2. **ACK**

   El servidor envía un ACK para acusar recibo del FIN para terminar la sesión de cliente a servidor.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103000416.png]]

3. **FIN**

   El servidor envía un FIN al cliente para terminar la sesión de servidor a cliente.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103000458.png]]

4. **ACK**

   El cliente responde con un ACK para dar acuse de recibo del FIN desde el servidor.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103000533.png]]



#### Análisis del enlace de tres vías de TCP

TCP es un protocolo full-duplex que mantiene el estado de la conexión y rastrea los datos mediante su encabezado.  
La conexión se establece con un enlace de tres vías (three-way handshake), que:

1. Confirma que el destino está disponible en la red.
2. Verifica que el servicio en el puerto de destino esté activo.
3. Notifica la intención del cliente de iniciar una sesión.

Una vez terminada la comunicación, las sesiones se cierran para garantizar la confiabilidad del protocolo.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103001234.png]]

Los seis indicadores (flags) del encabezado TCP controlan el estado y el flujo de una conexión:

1. **URG (Urgent):** Indica que los datos en el campo de puntero urgente deben procesarse de inmediato (tienen prioridad sobre otros datos).
2. **ACK (Acknowledgment):** Confirma la recepción de datos; se usa en casi todos los segmentos después del establecimiento de la conexión.
3. **PSH (Push):** Ordena entregar los datos al instante a la aplicación receptora sin esperar más segmentos.
4. **RST (Reset):** Restablece o cancela una conexión cuando hay errores o un intento de conexión no válido.
5. **SYN (Synchronize):** Inicia una conexión y sincroniza los números de secuencia entre cliente y servidor.
6. **FIN (Finish):** Indica que el emisor ha terminado de enviar datos y desea cerrar la conexión de manera ordenada.

Entonces, SYN y ACK se usan para conectar, PSH y URG para controlar el envío de datos, y FIN y RST para finalizar o reiniciar conexiones.

---

### Confiabilidad y control de flujo

#### Fiabilidad de TCP - Entrega garantizada y ordenada

TCP garantiza una comunicación confiable porque numera y reordena los segmentos de datos antes de entregarlos a la aplicación.

Cada segmento incluye un número de secuencia, que indica la posición del primer byte de datos dentro del flujo.  
Durante la conexión, se genera un Número de Secuencia Inicial (ISN) —un valor aleatorio que sirve como punto de partida—.

A medida que se transmiten los datos, TCP incrementa el número de secuencia según los bytes enviados, lo que permite:

- Detectar segmentos perdidos.
- Reensamblar los datos en el orden correcto.
- Evitar ataques al usar ISN aleatorios.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103020134.png]]

El receptor TCP almacena los segmentos en un búfer de recepción, los ordena según su número de secuencia y los entrega a la capa de aplicación una vez que están completos.  
Si algunos segmentos llegan fuera de orden, se guardan temporalmente hasta que lleguen los faltantes, y luego se reensamblan correctamente antes de procesarse.



#### Fiabilidad de TCP - Pérdida y retransmisión de datos

TCP utiliza los números de secuencia (SEQ) y acuse de recibo (ACK) para asegurar que los datos lleguen correctamente.  
El número SEQ identifica el primer byte del segmento enviado, y el ACK indica el siguiente byte que el receptor espera recibir (acuse de recibo de expectativa).

Antes de las mejoras modernas, si se perdían algunos segmentos, TCP solo reconocía el siguiente segmento esperado, lo que hacía que el emisor retransmitiera varios segmentos innecesariamente, generando duplicados, retrasos y congestión en la red.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103021025.png]]

La característica SACK (Selective Acknowledgment) permite que TCP reconozca qué segmentos se recibieron correctamente, incluso si llegan fuera de orden.  
Así, el receptor puede informar exactamente qué datos faltan, y el emisor solo retransmite los segmentos perdidos, evitando duplicaciones y mejorando la eficiencia y velocidad de la comunicación.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103021137.png]]

TCP usa temporizadores para determinar cuánto tiempo esperar antes de retransmitir un segmento no reconocido.  
Normalmente, envía un ACK por cada dos paquetes, aunque este comportamiento puede variar según las condiciones de la red.



#### Control de flujo de TCP - Tamaño de la ventana y reconocimientos

TCP implementa control de flujo para evitar que el emisor envíe más datos de los que el receptor puede manejar.  
Esto se logra mediante el campo “tamaño de ventana” en el encabezado TCP, que indica la cantidad de datos (en bytes) que el receptor puede aceptar antes de necesitar un nuevo reconocimiento (ACK).

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103021744.png]]

El tamaño de la ventana TCP define cuántos bytes puede enviar el emisor sin recibir un reconocimiento del receptor.  
Durante la conexión, ambos equipos acuerdan este valor inicial, que puede ajustarse dinámicamente según la capacidad del búfer del receptor.

El receptor envía ACKs conforme procesa los datos, permitiendo que el emisor deslice su ventana de envío (ventanas deslizantes) y continúe transmitiendo sin detenerse.  
Si el receptor tiene menos espacio disponible, reduce el tamaño de la ventana para que el emisor disminuya su ritmo de envío.



#### Control de flujo TCP - Tamaño máximo de segmento (MSS)

El Tamaño Máximo de Segmento (MSS) indica la máxima cantidad de datos (en bytes) que un dispositivo puede recibir en un solo segmento TCP, sin contar el encabezado.  
Este valor, generalmente de 1.460 bytes, se negocia durante el enlace de tres vías y permite optimizar la transmisión evitando fragmentación en la red.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103022040.png]]

El MSS típico es de 1.460 bytes en IPv4, calculado restando los encabezados IP (20 bytes) y TCP (20 bytes) del MTU de Ethernet (1500 bytes).  
Así, 1500−20−20=1460, que representa la cantidad máxima de datos que puede enviarse en un segmento TCP sin fragmentación.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103022220.png]]


#### Control de flujo de TCP - Prevención de congestiones

Cuando hay congestión en la red, los routers comienzan a descartar paquetes, lo que causa que algunos segmentos TCP no sean confirmados.  
El origen detecta la congestión al notar retrasos o falta de reconocimientos (ACK) y, para evitar empeorarla, reduce la cantidad de datos enviados antes de recibir una nueva confirmación.  
TCP utiliza algoritmos y temporizadores de control de congestión para ajustar dinámicamente el flujo de datos y evitar saturar la red.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103022355.png]]

Los números de acuse de recibo (ACK) indican el siguiente byte esperado, no un segmento.  
En caso de congestión, el origen es quien reduce la cantidad de bytes no reconocidos que envía, sin cambiar el tamaño de la ventana definido por el destino.  
Los detalles de los algoritmos y temporizadores de control de congestión no se abordan en este curso.

---

### Comunicación UDP

UDP es ideal para transmisiones rápidas, como VoIP, porque no establece conexión y tiene baja sobrecarga. Su encabezado pequeño y la ausencia de tráfico de control permiten un transporte de datos más ágil y eficiente.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103022826.png]]



#### Reensamblaje de datagramas de UDP

UDP no controla el orden de los datagramas ni usa números de secuencia como TCP. Los datos se reensamblan en el orden recibido y se envían directamente a la aplicación. Si el orden es importante, la aplicación debe encargarse de organizar los datos correctamente.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103022946.png]]



#### Procesos y solicitudes del servidor UDP

Las aplicaciones de servidor basadas en UDP usan números de puerto conocidos o registrados, al igual que las basadas en TCP.  
Cuando el servidor recibe un datagrama UDP, este se entrega a la aplicación correspondiente según el número de puerto asignado.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103024233.png]]

El servidor RADIUS ofrece servicios de autenticación, autorización y contabilidad para controlar el acceso de los usuarios, aunque su funcionamiento no se aborda en este curso.



#### Procesos de cliente UDP

En UDP, la comunicación cliente-servidor comienza cuando el cliente elige un puerto de origen dinámico y envía datos al puerto de destino conocido del servidor. Todos los datagramas usan el mismo par de puertos, y al responder, el servidor invierte los puertos de origen y destino en el encabezado.

1. **Clientes que envían solicitudes UDP**

   El cliente 1 esta enviando una solicitud DNS utilizando el conocido puerto 53, mientras que el cliente 2 solicita servicios de autenticación RADIUS mediante el puerto registrado 1812.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103024553.png]]

2. **Puertos de destino de solicitud UDP**

   Las solicitudes de los clientes generan dinamicamente números de puerto de origen. En este caso, el cliente 1 esta utilizando el puerto de origen 49152 y el cliente 2 esta utilizando el puerto de origen 51152.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103024716.png]]

3. **Puertos de origen de solicitud UDP**

   Cuando el servidor responde a las solicitudes del cliente, invierte los puertos de destino y origen de la solicitud inicial.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103024800.png]]

4. **Destino de respuesta UDP**

   En la respuesta del servidor a la solicitud DNS ahora es el puerto de destino 49152 y la respuesta de autenticación RADIUS ahora es el puerto de destino 51152.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103024904.png]]

5. **Puertos de origen de respuesta UDP**

   Los puertos de origen en la respuesta del servidor son los puertos de destino originales en las solicitudes iniciales.

![[Telematica I/Curso de Cisco/Módulo 14/ANEXOS/Pasted image 20251103024952.png]]

