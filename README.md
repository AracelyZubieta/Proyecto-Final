📌 Nombre del Proyecto
MICRO-MACRO CENTRIFUGA
-Autores
Desarrollado por:
Aracely Zubieta
Ingrid Cruz
Joseph Iquize
🎯 Objetivo del Proyecto
Objetivo General

Desarrollar un prototipo de centrífuga que combine en un solo equipo las funciones de una microcentrífuga y una macro centrífuga. Utilizando tecnologías de impresión 3D y componentes electrónicos accesibles en Bolivia.
Objetivos especificos

-Diseñar y fabricar un prototipo funcional de centrífuga macro y micro utilizando materiales disponibles localmente. 

-Implementar un sistema de control de velocidad utilizando motores paso a paso, permitiendo un control preciso de la velocidad de rotación en ambas versiones de la centrífuga. 

-Construir y ensamblar las partes del prototipo mediante impresión 3D, optimizando los costos de fabricación y mejorando la precisión de los componentes como la carcasa, los soportes y el rotor. 

-Realizar pruebas de funcionamiento para evaluar la eficiencia de la separación de muestras en función de su volumen y velocidad de rotación. 
🧩 Justificación
En los hospitales y laboratorios, donde los recursos humanos y tecnológicos son limitados es necesario buscar alternativas para cumplir sus funciones,el proyecto busca ofrecer una solución práctica y económica al combinar en un solo equipo las funciones de microcentrífuga y macro centrífuga. De esta forma se reduce el costo de adquisición, el espacio requerido y el mantenimiento, facilitando su uso en laboratorios pequeños, hospitales de segundo nivel y entornos educativos, donde los recursos suelen ser limitados. 
🏥 Alcance
El alcance del proyecto comprende el diseño, desarrollo, construcción y validación funcional de un prototipo de centrífuga híbrida capaz de operar como micro y macrocéntrifuga, incluyendo el modelado mecánico de la carcasa, soportes y rotores mediante software CAD; la fabricación de los componentes estructurales mediante impresión 3D; la integración de un sistema de control basado en un sistema de comunicacion maestro esclavo para regular la velocidad de rotación; la selección e instalación de motores, electrónica y elementos de seguridad como sensores d etemperatura; y la realización de pruebas de funcionamiento para evaluar estabilidad, eficiencia de separación y comportamiento mecánico en distintas condiciones de carga. El proyecto se limita al desarrollo de un prototipo funcional con fines académicos y de validación conceptual

📚 Fundamentación Técnica
Seguridad: Los sensores de temperatura son para controlar el estado delos componentes dado que se trbaaja con componentes como la bateria Lipo 
Sistemas de comunicación:El sistema emplea una arquitectura de comunicación sencilla y eficiente basada en tres canales principales. El sensor BME280 utiliza la interfaz I²C, permitiendo la transmisión de datos ambientales (temperatura y presión) mediante un bus digital de dos líneas que reduce el cableado y facilita la integración con el microcontrolador. La medición de la velocidad real del rotor se realiza mediante un encoder incremental, cuya señal se recibe a través de entradas digitales por pulsos en los canales A y B, lo que permite obtener la frecuencia de giro y detectar variaciones dinámicas en las RPM. Finalmente, se utiliza comunicación serial para monitorear valores, registrar datos o realizar configuraciones durante la etapa de pruebas y validación del prototipo. Esta combinación de protocolos permite un sistema de control estable, de rápida respuesta y fácilmente ampliable.


Componentes 
-Motor Brushless A2212 (1800 KV o 2200 KV)
-ESC 30A (controlador brushless tipo drone)
-Sensor BME280
-Módulo encoder de velocidad HC-020K
-Batería LiPo 3S (11.1 V)
-Pantalla LCD
-Microcontrolador SP32

Especificaciones tecnicas :

Control de Velocidad:
Rango de RPM: 1,000 - 15,000 RPM ajustable.
Con una capacidad de 1 a 15kg
Control digital de tiempo, aceleración y desaceleración 
Adaptabilidad:
Rotor intercambiable: Compatible con tubos de 0.2 ml a 50 ml, gracias a adaptadores.
Energía recargable con baterías.
Seguridad:
Sistema de bloqueo de tapa durante el funcionamiento.
Protección contra desequilibrio y sobrecarga.
Sistema de ventilación para evitar sobrecalentamiento.


