# Proyecto Integrador de Mecatrónica: Sistema Automatizado con ESP32

## Descripción General

El proyecto consiste en el diseño, construcción e implementación de un sistema mecatrónico funcional basado en el microcontrolador ESP32 como unidad de control y comunicación principal. El sistema podrá estar orientado a domótica, automatización de procesos industriales, monitoreo ambiental, agricultura inteligente, energía, o control de dispositivos electromecánicos, entre otros campos afines.

El objetivo es que el equipo desarrolle una solución integrada que combine electrónica, control, programación y comunicación IoT, demostrando la aplicación práctica de los conceptos aprendidos durante el curso.

---

### Requisitos Técnicos Mínimos

1. **Controlador principal:**

Uso obligatorio del ESP32 como microcontrolador central.

2. **Sensórica:**

Implementar mínimo 5 sensores de distinta naturaleza (temperatura, humedad, gas, luminosidad, movimiento, nivel, presión, etc.).

Los sensores deben aportar datos útiles y coherentes con la finalidad del proyecto.

3. **Actuadores:**

Utilizar mínimo 5 actuadores (motores, servos, relés, electroválvulas, luces, alarmas, ventiladores, etc.).

Deben responder a condiciones o comandos definidos por la lógica de control.

4. **Motor obligatorio:**

Incluir al menos un motor (DC, servo o paso a paso), controlado mediante driver o puente H según corresponda.

5. **Visualización de datos:**

Incorporar un display o pantalla (LCD, OLED, TFT, etc.) para mostrar información relevante del sistema.

Se valorará el diseño de interfaz clara y funcional.

6. **Comunicación de datos:**

Implementar al menos un protocolo de comunicación:

I²C, SPI o UART (para conexión con módulos, sensores o periféricos).

Además, debe integrar comunicación inalámbrica por Bluetooth o WiFi, según la función deseada.

7. **Conectividad e IoT:**

El sistema deberá enviar o almacenar datos en la nube (por ejemplo, en Google Sheets, ThingSpeak, Firebase, Blynk u otra plataforma).

Alternativamente, puede incluir un panel web o aplicación móvil que muestre los datos en tiempo real.

8. **Maqueta o prototipo físico:**

Se debe construir una maqueta funcional o simulador físico que represente el entorno donde opera el sistema.

Debe ser estética, clara y estructuralmente coherente con la aplicación propuesta.

9. **Documentación técnica:**

El equipo debe entregar un informe final con:

- Descripción general y objetivos del proyecto.

- Diagramas eléctricos y de conexión.

- Diagrama de flujo o pseudocódigo del algoritmo de control.

- Capturas o gráficos del almacenamiento de datos en la nube.

- Evidencia fotográfica y/o en video del funcionamiento.

- Conclusiones y análisis de desempeño.

---

### Criterios de Evaluación (100%)

| **N.º** | **Criterio**                                    | **Descripción**                                                                                                                                      | **Ponderación** |
| ------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **1**   | **Creatividad e innovación**                    | Originalidad del concepto, nivel de integración de tecnologías, valor agregado y pertinencia del problema abordado.                                  | **15%**         |
| **2**   | **Funcionamiento técnico**                      | Correcto desempeño del sistema, estabilidad del código, interacción fluida entre sensores y actuadores, respuesta del motor y comunicación efectiva. | **25%**         |
| **3**   | **Integración electrónica y de comunicaciones** | Uso apropiado de protocolos I²C, SPI o UART; comunicación Bluetooth/WiFi estable; organización del cableado y conexiones.                            | **15%**         |
| **4**   | **Interfaz y visualización de datos**           | Claridad del display, calidad del panel o aplicación, estructura del almacenamiento en la nube y facilidad de interpretación de los datos.           | **10%**         |
| **5**   | **Maqueta y presentación física**               | Nivel de detalle, diseño funcional, orden, limpieza y coherencia estética con el propósito del proyecto.                                             | **10%**         |
| **6**   | **Documentación técnica**                       | Claridad del informe, diagramas correctos, evidencia de pruebas y resultados, calidad técnica del reporte.                                           | **15%**         |
| **7**   | **Presentación final y demostración**           | Exposición oral, claridad en la explicación del funcionamiento, dominio del tema y respuesta a preguntas técnicas.                                   | **10%**         |
