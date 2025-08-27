# Exposiciones

---

## Arquitectura de software monolito

Es un estilo de arquitectura de software donde toda la aplicación se desarrolla como una sola unidad indivisible. Esto significa que la interfaz de usuario, la lógica de negocio y el acceso a datos están empaquetados y desplegados juntos en un único bloque (generalmente un solo archivo ejecutable o un único servicio).

---

### ¿Para qué sirve?

- Sirve para desarrollar aplicaciones pequeñas o medianas de manera rápida.

- Es ideal cuando se busca simplicidad en la gestión, el despliegue y el desarrollo inicial.

- Se utiliza en sistemas donde no se prevé gran crecimiento ni escalabilidad compleja.

---

### ¿Cómo funciona?

1. Todo el código está en una única base de código.

2. Cuando el usuario interactúa (ej: hace clic en un botón), la petición recorre las capas internas**:
   
   - **UI (interfaz gráfica o frontend)**
   
   - **Lógica de negocio (procesa la solicitud)**
   
   - **Acceso a datos (consulta o guarda en la base de datos)**

3. Todo se ejecuta dentro del mismo proceso/aplicación y se despliega en un único servidor (o réplica de la misma aplicación si hay escalamiento vertical u horizontal).

---

### Ejemplos de situaciones donde se usa

1. **Aplicación web de inventario de una tienda pequeña**
   
   - Un sistema que maneja productos, clientes y ventas en un único software centralizado.
   
   - Fácil de instalar en un solo servidor.

2. **Sistema interno de una universidad para gestionar matrículas**
   
   - Una aplicación que contiene el módulo de estudiantes, profesores y cursos en un solo bloque.
   
   - No requiere separación de servicios porque el número de usuarios es limitado y estable.

---

### Ventajas

**Simplicidad en el desarrollo**: Fácil de programar, probar y desplegar. 
**Menor curva de aprendizaje**: Cualquier programador entiende rápidamente la estructura. 
**Un solo despliegue**: Basta con subir un archivo/servicio al servidor. 
**Eficiencia en entornos pequeños**: Corre bien en proyectos donde no se necesita gran escalabilidad.

---

### Desventajas

**Difícil de escalar**: Para manejar más carga, hay que duplicar toda la aplicación, aunque solo un módulo sea el que necesita más recursos. 
**Mantenimiento complicado**: A medida que el proyecto crece, el código se vuelve complejo y difícil de modificar. 
**Falta de flexibilidad tecnológica**: Todos los módulos deben usar el mismo lenguaje y framework. 
**Impacto de fallos**: Si un módulo falla, puede tumbar toda la aplicación. 
**Despliegues lentos**: Cualquier cambio, por pequeño que sea, requiere volver a desplegar toda la aplicación.

---

## Arquitectura por capas

Es un modelo de diseño de software donde la aplicación se organiza en capas separadas, y cada capa tiene una responsabilidad específica. Cada capa solo interactúa con la capa inmediatamente inferior o superior, lo que permite una mejor organización, mantenimiento y reutilización del código.

---

### ¿Para qué sirve?

- Sirve para organizar el software de forma estructurada, separando responsabilidades.

- Facilita el mantenimiento, pruebas y escalabilidad.

- Es muy usada en sistemas empresariales y aplicaciones grandes, porque reduce la complejidad del proyecto.

---

### ¿Cómo funciona?

Una aplicación en capas normalmente se divide en:

1. **Capa de Presentación (UI o Frontend)**
   
   - Lo que ve el usuario (pantallas, formularios, botones).
   
   - Ejemplo: una web en Angular, React o JSP.

2. **Capa de Negocio (Lógica de negocio)**
   
   - Procesa las reglas y operaciones de la aplicación.
   
   - Ejemplo: calcular el total de una factura, validar un pago.

3. **Capa de Datos (Persistencia o Acceso a datos)**
   
   - Se encarga de comunicarse con la base de datos.
   
   - Ejemplo: consultas SQL, repositorios en Spring Data JPA.

4. (Opcional) **Capa de Infraestructura**
   
   - Maneja la comunicación con APIs externas, seguridad, servicios de terceros.

El flujo básico es: 
**Usuario → UI → Lógica de negocio → Acceso a datos → Base de datos → Respuesta hacia arriba.**

---

### Ejemplos de situaciones donde se usa

1. **Sistema bancario en línea**
   
   - **Presentación**: La app móvil/web para los clientes.
   
   - **Negocio**: Reglas para validar transacciones, transferencias, cobros.
   
   - **Datos**: Consultas de cuentas y movimientos en la base de datos.

2. **Plataforma de reservas de un hotel**
   
   - **Presentación**: Formulario de reserva en la web.
   
   - **Negocio**: Lógica que verifica disponibilidad de habitaciones.
   
   - **Datos**: Base de datos con clientes, reservas y habitaciones.

---

### Ventajas

**Organización clara**: Separación de responsabilidades. 
**Mantenimiento más fácil**: Puedes modificar una capa sin afectar las demás. 
**Reutilización de código**: La lógica de negocio puede servir para diferentes interfaces (ej: web y móvil). 
**Escalabilidad lógica**: Puedes reforzar una capa sin necesidad de tocar todo el sistema. 
**Facilita pruebas unitarias**: Se testea cada capa por separado.

---

### Desventajas

**Menor rendimiento**: Cada petición pasa por varias capas, lo que puede ralentizar. 
**Rigidez en comunicación**: Las capas deben respetar la jerarquía, no pueden saltarse. 
**Sobrecarga en proyectos pequeños**: Para sistemas simples puede ser “demasiada estructura”. 
**Acoplamiento vertical**: Si una capa se vuelve muy dependiente de otra, puede dificultar los cambios.

---

## Arquitectura de software Cliente-Servidor

Es un modelo de arquitectura de software donde la aplicación se divide en dos partes principales:

- **Cliente**: la parte que solicita servicios (ej. una app, navegador, programa).

- **Servidor**: la parte que procesa esas solicitudes y devuelve respuestas (ej. servidor web, base de datos, API).

En este modelo, el cliente nunca accede directamente a los datos, sino que los pide al servidor.

---

### ¿Para qué sirve?

- Para compartir recursos centralizados (como bases de datos, archivos, aplicaciones).

- Para organizar sistemas distribuidos donde muchos clientes acceden al mismo servidor.

- Para aplicaciones que requieren interacción remota, como internet, redes empresariales, apps móviles, etc.

---

### ¿Cómo funciona?

1. El cliente hace una solicitud (ejemplo: pedir una página web, iniciar sesión).

2. El servidor recibe la petición, la procesa y consulta datos si es necesario.

3. El servidor devuelve la respuesta al cliente.

Ejemplo típico:

- Abres tu navegador (**cliente**) y escribes `www.google.com`.

- El navegador manda la petición a Google (**servidor**).

- El servidor procesa y devuelve la página.

- El cliente la muestra en tu pantalla.

---

### Ejemplos de situaciones donde se usa

1. **Aplicación web de correo electrónico** (ej: Gmail):
   
   - El cliente (navegador o app) solicita ver correos.
   
   - El servidor procesa y envía los mensajes almacenados en su base de datos.

2. **Sistema de cajeros automáticos (ATM)**:
   
   - El cajero (cliente) pide al servidor central información sobre saldo, retiros o depósitos.
   
   - El servidor valida las reglas y responde con la transacción aprobada o rechazada.

---

### Ventajas

**Centralización de recursos**: Los datos y procesos están en un servidor central, lo que facilita el control. 
**Mantenimiento sencillo**: Los cambios se aplican en el servidor y no en cada cliente. 
**Mayor seguridad**: El cliente no accede directamente a la base de datos. 
**Escalabilidad en número de clientes**: Se pueden conectar múltiples usuarios a un mismo servidor. 
**Facilita trabajo en red**: Ideal para internet y aplicaciones distribuidas.

---

### Desventajas

**Dependencia del servidor**: Si el servidor falla, todos los clientes quedan inactivos. 
**Sobrecarga del servidor**: Muchos clientes simultáneos pueden saturarlo. 
**Mayor complejidad en red**: Requiere buena conectividad y configuración de protocolos. 
**Costos de infraestructura**: Servidores potentes, balanceadores de carga, mantenimiento.

---

## Arquitectura orientada a servicios (SOA)

Es un estilo de arquitectura de software en el cual las funcionalidades de un sistema se organizan como servicios independientes que se comunican entre sí mediante **protocolos estándar** (por ejemplo, HTTP, SOAP, REST).

Cada servicio realiza una tarea específica (por ejemplo: “gestionar usuarios”, “procesar pagos”, “enviar notificaciones”) y puede ser reutilizado por diferentes aplicaciones.

---

### ¿Para qué sirve?

- Sirve para desacoplar sistemas grandes en servicios independientes y reutilizables.

- Facilita la integración de sistemas heterogéneos (ejemplo: Java, .NET, PHP pueden comunicarse entre sí vía servicios).

- Es muy útil en entornos empresariales donde distintos módulos necesitan interoperar.

---

### ¿Cómo funciona?

1. Una aplicación (o cliente) solicita un servicio (ejemplo: “consultar disponibilidad de habitaciones”).

2. El servicio expone una interfaz bien definida (ejemplo: un endpoint con SOAP o REST).

3. El servicio procesa la solicitud, accede a sus datos y devuelve la respuesta.

4. Otros servicios pueden reutilizar ese mismo servicio para sus propias operaciones.

La clave es que los servicios son independientes pero colaboran entre sí.

---

### Ejemplos de situaciones donde se usa

1. **Comercio electrónico (e-commerce)**
   
   - Servicio de clientes (gestiona registros y perfiles).
   
   - Servicio de pagos (procesa tarjetas y pasarelas).
   
   - Servicio de inventario (controla stock).
   
   - Todos trabajan juntos para completar una compra.

2. **Sistema de salud**
   
   - Servicio de pacientes (historial médico).
   
   - Servicio de citas médicas.
   
   - Servicio de facturación.
   
   - Servicios integrados, pero cada hospital puede usar los que necesite.

---

### Ventajas

**Reutilización de servicios**: Un mismo servicio puede ser usado por diferentes aplicaciones. 
**Interoperabilidad**: Permite conectar sistemas en distintos lenguajes o plataformas. 
**Flexibilidad**: Es fácil añadir, modificar o eliminar servicios sin afectar todo el sistema. 
**Escalabilidad**: Se pueden distribuir los servicios en distintos servidores según la demanda. 
**Mantenimiento más fácil**: Cada servicio es independiente y más simple de actualizar.

---

### Desventajas

**Complejidad de diseño**: Requiere planificación para definir bien los servicios y sus interfaces. 
**Sobrecarga de comunicación**: Al depender de mensajes entre servicios, puede ser más lento que un monolito. 
**Costos de infraestructura**: Mantener múltiples servicios y su orquestación puede ser caro. 
**Seguridad más compleja**: Se deben proteger varios puntos de entrada (servicios expuestos).

---

## Programación orientada a eventos

Es un paradigma de programación en el que la ejecución del programa se basa en eventos (acciones o sucesos que ocurren, ya sea por el usuario, el sistema o un dispositivo externo).

Un evento puede ser:

- Un clic en un botón.

- La llegada de un mensaje a un servidor.

- El cambio de estado en un sensor.

El programa no sigue un flujo lineal clásico, sino que espera a que ocurra un evento y ejecuta una función o rutina asociada (llamada *manejador de eventos* o *event handler*).

---

### ¿Para qué sirve?

- Sirve para crear aplicaciones interactivas y reactivas, donde el flujo depende de lo que haga el usuario o el sistema.

- Se utiliza en interfaces gráficas (GUI), aplicaciones web, videojuegos, sistemas IoT y arquitecturas distribuidas.

---

### ¿Cómo funciona?

1. El programa se suscribe a eventos específicos (ejemplo: “escuchar clics en un botón”).

2. Cuando el evento ocurre, el sistema lanza un dispatcher o notificador.

3. Se ejecuta el manejador de eventos correspondiente (ejemplo: una función que abre un formulario cuando haces clic).

Estructura: 
**Evento ocurre → Se dispara → Se ejecuta la acción asociada.**

---

### Ejemplos de situaciones donde se usa

1. **Aplicación de escritorio** (ej: un editor de texto):
   
   - El usuario hace clic en “Guardar”.
   
   - Se dispara el evento `onClick()`.
   
   - El manejador guarda el archivo en disco.

2. **Sistema IoT en una casa inteligente**:
   
   - Un sensor detecta movimiento en la sala.
   
   - Se dispara el evento `onMotionDetected`.
   
   - El manejador enciende automáticamente las luces.

---

### Ventajas

**Interactividad**: Ideal para aplicaciones que dependen de la acción del usuario. 
**Flexibilidad**: Se pueden añadir nuevos eventos sin reescribir todo el programa. 
**Asincronía**: Permite manejar múltiples sucesos al mismo tiempo (ejemplo: en servidores). 
**Escalabilidad lógica**: En sistemas distribuidos, facilita el procesamiento de eventos concurrentes.

---

### Desventajas

**Complejidad en el flujo**: El programa no sigue un orden lineal, lo que puede hacerlo más difícil de entender. 
**Difícil de depurar**: Encontrar errores puede ser complicado porque los eventos pueden ocurrir en cualquier momento. 
**Posible sobrecarga**: Si hay demasiados eventos simultáneos, el sistema puede saturarse. 
**Dependencia de manejadores**: Si un evento no tiene un handler adecuado, puede generar errores o comportamientos inesperados.
