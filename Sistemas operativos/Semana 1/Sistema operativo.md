# ¿Qué es un sistema operativo?

Son un conjunto de programas que se encargan de la administración de todos los recursos del computador tanto de hardware como de sorftware.

---

## Clasificación de los Sistemas Operativos (S.O.)

#### Por su estructura interna:

- **Jerárquico o por capas**:  
  El sistema se organiza en niveles, donde cada capa ofrece servicios a la capa superior y se apoya en la inferior. Mejora la modularidad y el mantenimiento.

- **Monolítico**:  
  Todo el sistema operativo corre en un solo espacio de memoria (núcleo), incluyendo controladores, servicios y gestión de hardware. Es rápido pero difícil de mantener.

- **Cliente-servidor**:  
  Divide funciones entre clientes (que solicitan servicios) y servidores (que los proporcionan). Facilita la escalabilidad y distribución de procesos.

- **Máquina virtual**:  
  Simula múltiples sistemas operativos sobre una misma máquina física, permitiendo ejecutar varios entornos independientes.

---

#### Por los modos de explotación:

- **Procesamiento por lotes**:  
  Ejecuta trabajos sin interacción del usuario. Se agrupan tareas en lotes y se procesan secuencialmente.

- **Multiprogramación**:  
  Permite ejecutar múltiples programas simultáneamente, aprovechando mejor el procesador.

- **Tiempo compartido**:  
  Asigna el tiempo del procesador a múltiples usuarios de manera equitativa y rápida, creando la ilusión de simultaneidad.

- **Tiempo real**:  
  Responde a eventos en un tiempo predecible. Se usa en sistemas críticos como control industrial o médico.

- **Híbrido (compartido y tiempo real)**:  
  Combina características de tiempo compartido y tiempo real, permitiendo tareas críticas y multitarea general.

---

#### Por el manejo de recursos o por la forma de ofrecer servicios:

- **Centralizado**:  
  Todos los recursos están en una única máquina, y los usuarios acceden a ella para procesar datos.

- **Sistema de red (Network Operating System)**:  
  Coordina y gestiona recursos entre varias computadoras conectadas en red, pero cada una mantiene su sistema operativo.

- **Distribuido**:  
  El sistema operativo se ejecuta de manera coordinada en múltiples máquinas como si fuera una sola, ocultando la distribución al usuario.

---

#### Por la administración de tareas:

- **Monotarea**:  
  Basado en la monoprogramación. Solo permite ejecutar una tarea o programa a la vez.

- **Multitarea**:  
  Basado en la multiprogramación. Permite ejecutar múltiples tareas o procesos simultáneamente, compartiendo el procesador.

---

### Por la administración de usuarios:

- **Monousuario**:  
  Solo permite que un usuario utilice el sistema a la vez.

- **Multiusuario**:  
  Permite que varios usuarios trabajen con el sistema al mismo tiempo, ya sea de forma local o remota.

---

### Por el número de procesadores:

- **Monoproceso**:  
  El sistema operativo está diseñado para trabajar con un solo procesador.

- **Multiproceso**:  
  El sistema operativo puede manejar varios procesadores simultáneamente, permitiendo una mayor eficiencia y rendimiento en el procesamiento de tareas.
