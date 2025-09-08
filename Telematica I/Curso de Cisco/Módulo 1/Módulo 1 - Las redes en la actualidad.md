# Módulo 1: Las redes en la actualidad

---

## Contenido

- **Las redes afectan nuestras vidas:** Explique la forma en que las redes afectan nuestra vida diaria.

- **Componentes de la red:** Explique la forma en que se utilizan los dispositivos host y de red.

- **Topología y representaciones de red:** Explique las representaciones de la red y cómo se usan en la red. Topologias

- **Tipos comunes de redes:** Compare las características de los tipos comunes de redes.

- **Conexiones a internet:** Explique la forma en que las LAN y las WAN se interconectan a Internet.

- **Redes confiables:** Describa los cuatro requisitos básicos de una red confiable.

- **Tendencias de red:** Explique cómo tendencias como BYOD, colaboración en línea, video y nube la informática está cambiando la forma en que interactuamos.

- **Seguridad de red:** Identifique algunas amenazas y soluciones de seguridad básicas para todas las redes. 

---

### Las redes afectan nuestras vidas

La comunicación es casi tan vital como las necesidades básicas para la vida. Gracias a las redes e Internet, hoy las personas pueden interactuar instantáneamente, compartir ideas, acceder a noticias y conectarse sin importar fronteras, distancias o zonas horarias. Estos avances han transformado las interacciones sociales, comerciales y políticas, fomentando comunidades globales. Además, la nube permite almacenar y acceder a información y aplicaciones desde cualquier lugar y dispositivo, aumentando la productividad y la conexión mundial.

---

### Componentes de la red

- **Host:** Es el sistema inteligente con una dirección IP que sirve para identificar ala Host conectado por la red, ya que la red se conecta al Host, tambien llamados **dispositivos finales** o clientes, donde un Host es un dispositivo en la red que se le asigna un número para fines de comunicación.

- **Servidor:** Los servidores son computadoras que, mediante software especializado, ofrecen información o servicios como correo electrónico o páginas web a otros dispositivos en la red. Cada servicio necesita un software de servidor específico (por ejemplo, un servidor web para ofrecer páginas web). Un mismo servidor puede atender a muchos clientes a la vez. 

![](C:\Users\Molina211\OneDrive\Imágenes\Screenshots\Captura%20de%20pantalla%202025-08-22%20174822.png)

Para poder ingresar a la petición especifica que necesita el cliente del servidor, el PC cuenta con diferentes tipos de softwares para el uso de cada una de las opciones que proporciona el mismo. Un PC puede ejecutar varios tipos de software de cliente, tales como el envío de un correo mientras se ve otra pagina web escuchando música, ahí se pueden puntuar 3 tipos de software, el de correo electronico, el de Web y el de Reproductor de música.

- **Entre pares**
  
  Dentro de los software de cliente existe el **Entre pares**, que se basa en un tipo de red donde todos los dispositivos conectados son cliente y servidor a la vez. Se puede resaltar que:
  
  - **Ventajas:** Son fáciles de configurar, económicas y útiles para compartir recursos básicos.
  
  - **Desventajas:** No tienen administración centralizada, son poco seguras, no escalan bien y su rendimiento puede verse afectado.

- **Dispositivos finales**
  
  Se denomina como **Dispositivo final** aquel sistema conectado a la red que posee una direccion (IP), siendo tambien los que las personas se han familiarizado más como Portátiles, Computadoras de mesa, Celulares, etc.

- **Dispositivos intermedios**
  
  Los **Dispositivos Intermedios** son los encargados de controlar principalmente el flujo de datos en la red, capaces de estar conectados a multiples redes individuales para formar una red interna. Algunos de los dispositivos intermedios más comunes son:
  
  - *Router inalámbrico*
  
  - *Switch LAN*
  
  - *Router*
  
  - *Swith Multicapa*
  
  - *Dispositivos de firewall*
  
  Algunas de sus **Funciones** son regenerar y retransmitir señales, administrar rutas, detectar y notificar fallas, redirigir datos por rutas alternativas, clasificar mensajes según prioridad y controlar el flujo de datos con base en parámetros de seguridad.

- **Medios de red**
  
  Para poder interconectar los dispositivos se usan actualmente 3 tipos de medios moderno:
  
  - **Hilos metálicos dentro de cables (Cobre)** - Los datos se codifican en impulsos eléctricos.
  
  - **Fibras de vidrio o plástico (cable de fibra óptica)** - Los datos se codifican como pulsos de luz.
  
  - **Transmisión inalámbrica (Tecnología inalámbrica)** - Los datos se codifican a través de la modulación de frecuencias específicas de ondas electromagnéticas.

---

### Topología y representaciones de red

Se trata de la forma en la que muestra el como se ven los componentes que se conectaran a otros componentes, donde se ubicarán y como se conectarán. Aquí vemos lo que se llama **Topología**, que usa simbolos para la **representacion de red**.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-12-25-09-image.png)

Además de estas representaciones, se utiliza una terminología especializada para describir cómo cada uno de estos dispositivos y medios se conectan entre sí:

- **Tarjeta de interfaz de red (Network Interface Card) (NIC)** - Permite que un dispositivo se conecte físicamente a la red.

- **Puerto físico** - Es el conector donde se enchufa el cable de red u otro medio.

- **Interfaz** - Es el puerto de un dispositivo (como un router) que lo conecta con una red específica.

Se conoce como **Diagramas de topología** la forma de documentación en la que se proporciona un especie de esquema de como se conecta la red. Existe la física y la logica.

La **física** representa la ubicación real de dispositivos y la instalación de los cables. Marcando las habitaciones de los grupos de dispositivos.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-12-35-23-image.png)

La **lógica** ilustran la conexión entre dispositivos, puertos y direcciones de red. Marcando los dispositivos intermediarios y qué medios se están utilizando.

---

### Tipos comunes de redes

Las redes se clasifican en 4 tipos:

1. **Redes domésticas pequeñas:** Las redes domésticas pequeñas conectan algunas computadoras entre sí y a Internet.

2. **Redes domésticas/de oficinas pequeñas:** La red SOHO permite que las computadoras en una oficina hogareña o remota se conecten a una red corporativa o accedan a recursos compartidos centralizados.

3. **Redes medianas a grandes:** Las redes medianas a grandes, como las que se utilizan en corporaciones y escuelas, pueden tener muchas ubicaciones con cientos o miles de hosts interconectados.

4. **Redes mundiales:** Internet es una red de redes que conecta cientos de millones de computadoras en todo el mundo.
- **LAN y WAN**
  
  Hay terminos que se utilizan para describir la infrastructura de una red, como su tamaño de area, cantidad de usuarios conectados, cantidad de servicios y dispositivos, y el area de responsabilidad, con estas se ha llegado a crear las 2 clasificaciones más usadas en la actualidad, LAN y WAN
  
  - **LAN**
    
    Se entiende como una red que proporciona acceso a usuarios y dispositivos finales en un área geográfica pequeña como una empresa o un hogar.
    
    **Características:**
    
    - Conecta dispositivos en un área limitada (casa, escuela, oficina).
    
    - Es administrada por una sola organización o persona.
    
    - Ofrece ancho de banda de alta velocidad a los equipos conectados.
  
  - **WAN**
    
    Se entiende como una red que proporciona acceso a otras redes en un área geográfica amplia como una propiedad que esta administrada por corporación o un proveedor de servicios de telecomunicaciones. Son administradas por **proveedores de servicios (SP)** o **proveedores de servicios de Internet (ISP)**.
    
    **Características:**
    
    - Conectan LAN en grandes áreas geográficas.
    
    - Son gestionadas por múltiples proveedores de servicios.
    
    - Tienen enlaces más lentos que las LAN.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-14-06-27-image.png)

Tambien, esta el **Internet**, que es una colección global de redes interconectadas. Algunas LAN se conectan entre sí mediante una WAN, y estas WAN también pueden interconectarse usando cables de cobre, fibra óptica o transmisiones inalámbricas entre si mismas.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-14-18-15-image.png)

- **Intranets y Extranets**
  
  El Internet se divide en 2 terminologías:
  
  - **Intranets:** Se refiere a la conexíon privada de LAN y WAN que pertenece a una organización. Esta diseñada unicamente para los individuos que tiene acceso a autorizado.
  
  - **Extranets:** Se refiere a la extensión de la intranet, que permite a usuarios externos (como proveedores, contratistas o aliados) acceder de forma segura a cierta información o servicios de la empresa, como una empresa da acceso a sus proveedores o un hospital deja que los médicos reserven citas.

---

### Conexiones a Internet

Los usuarios domésticos y oficinas pequeñas acceden a Internet mediante un ISP usando opciones como cable, DSL, redes inalámbricas o móviles. En cambio, las organizaciones requieren conexiones más rápidas y seguras para servicios como telefonía IP y videoconferencias, por lo que utilizan soluciones empresariales como DSL corporativo, líneas arrendadas o Metro Ethernet.

- **Conexiones a Internet domésticas y de oficinas pequeñas**
  
  - **Cable:** Usa el mismo cable de la TV, ofrece buena velocidad y conexión siempre activa.
  
  - **DSL:** Usa la línea telefónica, es rápido y común en casas u oficinas pequeñas (ADSL tiene más descarga que subida).
  
  - **Celular:** Se conecta a través de la red móvil, depende de la cobertura y de la torre celular.
  
  - **Satelital:** Funciona en zonas remotas usando antena parabólica, necesita vista directa al satélite.
  
  - **Dial-up:** Conexión antigua y lenta que usa la línea telefónica y un módem, sirve como opción básica y de bajo costo.
  
  La disponibilidad depende del lugar y del proveedor de Internet.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-16-03-41-image.png)

- **Conexiones a Internet empresariales**
  
  - **Líneas arrendadas:** Conexiones privadas y dedicadas que enlazan oficinas en distintas ubicaciones, se pagan mensualmente o al año.
  
  - **Metro Ethernet:** Extiende la tecnología de red local (Ethernet) a la red amplia (WAN), muy usada en empresas.
  
  - **DSL empresarial:** Similar al DSL normal, pero con la misma velocidad de subida y descarga (SDSL).
  
  - **Satelital:** Opción útil en lugares donde no hay conexión por cable.
  
  **Nota:** Las opciones de conexión corporativas difieren de las domésticas, ya que las empresas suelen necesitar mayor ancho de banda, conexiones dedicadas y servicios administrados, los cuales dependen de los proveedores disponibles en la zona.
  
  La disponibilidad depende del lugar y del proveedor de Internet.

Anteriormente se usaban redes que utilizaban tecnologías diferentes para transportar la señal de comunicación. Cada red tenía su propio conjunto de reglas y estándares para asegurar una comunicación satisfactoria. Múltiples servicios se ejecutaron en múltiples redes. Estas redes no podian comunicarse entre si, cada una era individual y unicamente destinada para el tipo de servicio corresponiente, estas redes se llaman ****Redes separadas tradicionales****. Pero actualmente, las redes separadas de datos, telefonía y vídeo están convergiendo, permiten transmitir datos, voz y video en una misma infraestructura con reglas y estándares unificados, reemplazando a las redes separadas y transportando múltiples servicios en una sola red.

---

### Redes confiables

La red pasó de manejar solo datos a conectar personas, dispositivos e información en un entorno convergente, por lo que debe basarse en una arquitectura estándar que soporte la infraestructura, servicios y protocolos. Además, las redes deben considerar cuatro características clave: **tolerancia a fallas**, **escalabilidad**, **calidad de servicio (QoS)** y **seguridad**.

- **Tolerancia a fallas:** Una red tolerante a fallas limita el impacto de una avería y permite recuperarse rápidamente gracias a la **redundancia**, es decir, múltiples rutas entre origen y destino. Con la **conmutación de paquetes**, los mensajes se dividen en paquetes con su propia dirección, que pueden viajar por diferentes rutas según el estado de la red, garantizando que el usuario no note la falla ni el cambio de trayecto.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-17-08-53-image.png)

- **Escalabilidad:** Una red escalable puede crecer fácilmente para admitir más usuarios y aplicaciones sin afectar el rendimiento. Esto es posible gracias al uso de estándares y protocolos comunes, que permiten integrar nuevas redes y facilitan que los proveedores mejoren sus productos sin crear reglas nuevas.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-17-10-34-image.png)

- **Calidad de servicio:** Es clave en las redes modernas porque asegura que aplicaciones sensibles, como llamadas de voz o transmisiones de video en vivo, funcionen sin interrupciones. A medida que datos, voz y video comparten la misma red, QoS gestiona la congestión y garantiza que los contenidos lleguen de forma confiable a los usuarios.
  
  La **congestión** ocurre cuando la demanda de ancho de banda (la cantidad de datos que se pueden transmitir por segundo) supera la capacidad disponible de la red. En esos casos, los paquetes de datos deben esperar en cola hasta que haya recursos para enviarlos, lo que genera retrasos o cortes. Con QoS, la red puede priorizar ciertos tipos de tráfico (por ejemplo, llamadas de voz sobre descargas), reduciendo los efectos de la congestión.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-17-13-51-image.png)

- **Seguridad de la red:** La red y la información que circula en ella son activos muy valiosos, por lo que la seguridad es esencial. Existen dos aspectos principales:
  
  - **Seguridad de la infraestructura:** Proteger físicamente los dispositivos de red (routers, switches, servidores) y evitar accesos no autorizados a su software de administración.
  
  - **Seguridad de la información:** Garantizar que los datos transmitidos y almacenados estén protegidos contra accesos indebidos o pérdidas.
  
  La seguridad de la información en la red busca proteger tanto los datos transmitidos como los almacenados en los dispositivos. Para lograrlo, se deben cumplir tres requisitos esenciales:
  
  1. **Confidencialidad** - Asegura que solo los usuarios autorizados puedan acceder y leer los datos.
  
  2. **Integridad** - Garantiza que la información no sea modificada durante su transmisión. 
  
  3. **Disponibilidad** - Permite a los usuarios autorizados acceder de manera confiable y oportuna a los servicios y datos necesarios.

![](C:\Users\Molina211\AppData\Roaming\marktext\images\2025-08-24-17-20-45-image.png)

---

### Tendencias de red

Las redes están en constante evolución y deben adaptarse a nuevas tecnologías y necesidades. Algunas de las principales tendencias actuales son:

- **BYOD (Bring Your Own Device):** es una tendencia que permite a las personas usar sus propios dispositivos (como laptops, tablets, smartphones o lectores electrónicos) para acceder a la red de una empresa o institución. Esto da libertad a los usuarios para trabajar y comunicarse desde cualquier lugar, con cualquier dispositivo, aprovechando que hoy estos equipos son más accesibles y avanzados.

- **Colaboración en línea:** Facilita el trabajo en equipo desde diferentes lugares a través de plataformas digitales.

- **Comunicaciones de video:** Uso de videollamadas y videoconferencias para reuniones, educación y comunicación.

- **Computación en la nube:** Permite acceder y almacenar datos por Internet, usar aplicaciones sin instalarlas y hacer **copias de seguridad**. En las empresas, facilita ampliar capacidades de TI sin grandes inversiones, ofreciendo servicios económicos, seguros y accesibles.
  
  Los **centros de datos** son instalaciones utilizadas para alojar sistemas informáticos y componentes asociados, aunque su mantenimiento es costoso; por eso, las organizaciones pequeñas suelen arrendar recursos a **proveedores de nube**. Además, los datos se guardan en **múltiples ubicaciones**, garantizando seguridad, fiabilidad y continuidad.
  
  Existen cuatro tipos principales de nubes:

- **Nubes públicas:** Infraestructura ofrecida por un proveedor externo (como Google Cloud, AWS, Microsoft Azure) y compartida por múltiples clientes.
  
  **Características:**
  
  - Bajo costo (se paga por uso).
  
  - Escalable de forma rápida.
  
  - No requiere que la empresa administre servidores.
  
  **Ejemplo:** Usar Google Drive o Dropbox para guardar archivos.

- **Nube Privada:** Infraestructura exclusiva para una sola organización, ya sea gestionada internamente o por un proveedor externo.
  
  **Características:**
  
  - Mayor seguridad y control.
  
  - Personalización según necesidades de la empresa.
  
  - Costos más altos que la nube pública.
  
  **Ejemplo:** Un banco que monta su propio centro de datos en la nube para proteger información financiera.

- **Nube Híbrida:** Combinación de nube pública y privada, permitiendo mover datos y aplicaciones entre ambas.
  
  **Características:**
  
  - Flexibilidad para usar lo mejor de cada nube.
  
  - Permite equilibrar costos y seguridad.
  
  - Ideal para empresas que manejan datos sensibles y aplicaciones públicas al mismo tiempo.
  
  **Ejemplo:** Una empresa que guarda datos críticos en una nube privada pero usa AWS para escalar sus aplicaciones.

- **Nube Comunitaria:** Infraestructura compartida por varias organizaciones con intereses o necesidades comunes.
  
  **Características:**
  
  - Compartida entre varias entidades (gobiernos, universidades, hospitales, etc.).
  
  - Costos y recursos distribuidos.
  
  - Más segura que la nube pública, pero menos que la privada.
  
  **Ejemplo:** Varias universidades que comparten una nube comunitaria para investigación y almacenamiento de datos académicos.

Viendolo por otro lado, la **tecnología del hogar inteligente** está transformando la vida cotidiana al integrar electrodomésticos con redes domésticas e internet de alta velocidad, permitiendo que funcionen de manera automatizada y conectada.

Por ejemplo, un horno inteligente puede programarse según el calendario de eventos, ajustar automáticamente tiempos y temperaturas de cocción, y enviar alertas al teléfono inteligente o tableta cuando la comida esté lista.

Otro metodo para esto son las **redes powerline**, que permite que los dispositivos se conecten a la **LAN** usando un **adaptador estándar de línea eléctrica**, aprovechando los tomacorrientes de la casa. No requiere instalar **cables de datos adicionales** ni consume mucha electricidad extra, ya que transmite la información a través de las frecuencias de los mismos cables eléctricos.

Es especialmente útil cuando la señal inalámbrica (Wi-Fi) no llega a todos los dispositivos. Aunque no reemplaza al cableado dedicado, sí es una alternativa práctica en lugares donde no es posible o efectivo usar redes cableadas o inalámbricas.

- **Banda ancha inalámbrica**
  
  El **Proveedor de Servicios de Internet Inalámbrico (WISP)** ofrece conexión a Internet en zonas rurales donde no hay cable o DSL, usando antenas instaladas en torres y una pequeña antena en el hogar del usuario.
  
  La **banda ancha inalámbrica** utiliza tecnología celular similar a la de los smartphones; se instala una antena en la vivienda que brinda conexión a los dispositivos.
  
  Estas dos alternativas son ultiles cuando no se tiene la disponibilidad de cable o DLS.

---

### Seguridad en la red

Es el conjunto de protocolos, tecnologías, dispositivos y técnicas que protegen los datos y la infraestructura de una red frente a amenazas internas y externas. Su objetivo es garantizar confidencialidad, integridad y disponibilidad de la información.

Existen varias amenazas externas comunes a las redes:

- **Virus, gusanos y caballos de Troya** - Estos contienen software malicioso o código que se ejecuta en un dispositivo de usuario.

- **Spyware y adware** - Estos son tipos de software que se instalan en el dispositivo de un usuario. El software recopila en secreto información sobre el usuario.

- **Ataques de día cero** - También llamados ataques de hora cero, se producen el primer día que se conoce una vulnerabilidad

- **Amenazas de Atacantes** - una persona malintencionada ataca dispositivos de usuario o recursos de red.

- **Ataques por denegación de servicio** - Estos ataques ralentizan o bloquean las aplicaciones y procesos en un dispositivo de red.

- **Intercepción y robo de datos** - Este ataque captura información privada de la red de una organización.

- **Robo de identidad** - Este ataque roba las credenciales de inicio de sesión de un usuario para acceder a datos privados.

No existe una única solución que proteja contra todas las amenazas. Por eso, la seguridad debe aplicarse en múltiples capas (defensa en profundidad). Si una capa falla, otras pueden detener el ataque.

**Seguridad en redes domésticas o pequeñas oficinas**

La seguridad suele ser más básica y limitada, pero suficiente para el entorno:

- **Antivirus y antispyware** - Protegen dispositivos contra malware.

- **Firewall** - Bloquea accesos no autorizados, ya sea en el router o en el propio dispositivo.

- **ISP** - A veces el proveedor de internet ofrece servicios de protección básicos.

**Seguridad en redes empresariales**

Las empresas requieren medidas más avanzadas y completas, ya que manejan más usuarios y datos sensibles:

- **Firewalls dedicados** - Más potentes, capaces de filtrar tráfico de forma granular.

- **Listas de control de acceso (ACLs)** - Restringen tráfico según IPs, puertos o aplicaciones.

- **Sistemas de prevención de intrusiones (IPS)** - Detectan y bloquean amenazas avanzadas como ataques de día cero.

- **Redes Privadas Virtuales (VPNs)** - Permiten conexión segura para empleados remotos.

---
