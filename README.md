# Guía de fundamentos de Python

Este repositorio contiene un conjunto estructurado de ejercicios prácticos diseñados para aprender y consolidar los conceptos básicos de la programación en Python. Los módulos cubren desde la sintaxis inicial y las estructuras de datos hasta el procesamiento de texto, operaciones del sistema operativo y manipulación de archivos estructurados.

## Qué problema resuelve este repositorio

Al aprender a programar en Python, los estudiantes a menudo se enfrentan a la desconexión entre la teoría y la práctica del mundo real. Este repositorio resuelve ese problema ofreciendo laboratorios prácticos y secuenciales que abordan:
- La transición gradual desde conceptos básicos (variables, tipos de datos, condicionales y bucles) hasta tareas más complejas (procesamiento de secuencias biológicas, criptografía básica y administración de sistemas).
- El manejo de datos estructurados como archivos CSV y JSON con librerías nativas del lenguaje.
- La ejecución de comandos del sistema operativo de manera programática, preparando al desarrollador para tareas de automatización y DevOps.

## Tecnologías utilizadas

El proyecto se basa en las siguientes herramientas y tecnologías:
- Python 3 como lenguaje de programación principal.
- Librerías estándar de Python, incluyendo:
  - `re` para manipulación de expresiones regulares y limpieza de texto.
  - `json` para el procesamiento y manejo de datos en formato JSON.
  - `os` y `subprocess` para interactuar con el sistema operativo y ejecutar procesos.
- AWS Cloud9 como entorno de desarrollo integrado en la nube.

## Uso de AWS Cloud9 en este proyecto

Este proyecto está configurado para ser desarrollado y ejecutado utilizando AWS Cloud9. AWS Cloud9 es un entorno de desarrollo integrado (IDE) basado en la nube que permite escribir, ejecutar y depurar código a través de un navegador web.

El repositorio incluye la carpeta `.c9`, la cual contiene las configuraciones específicas del entorno para facilitar la ejecución de los scripts sin necesidad de configurar dependencias locales complejas. 

Para ejecutar los scripts dentro de AWS Cloud9, se puede utilizar el terminal integrado de la instancia de Linux asociada o usar el botón de ejecución rápida en la interfaz gráfica del IDE. Esto garantiza que todos los desarrolladores compartan un entorno uniforme, eliminando los problemas de compatibilidad del sistema operativo.

## Casos de uso específicos y cuándo utilizar este repositorio

Este repositorio es de utilidad en las siguientes situaciones:
- Aprendizaje guiado de Python para principiantes que buscan ejemplos de código comentados y aplicados.
- Prácticas de procesamiento de cadenas de texto y bioinformática básica, como la extracción de subcadenas y el cálculo de propiedades moleculares de secuencias como la insulina.
- Implementación de algoritmos clásicos de criptografía de nivel introductorio, como el cifrado y descifrado César.
- Automatización básica de tareas del sistema operativo mediante scripts de administración de sistemas.

## Estructura de archivos y descripción de ejercicios

A continuación se detalla el propósito de cada archivo en el repositorio:
- `01-hello-world.py`: Introducción a la sintaxis básica e impresión de mensajes en consola.
- `02-numeric-data.py`: Uso de tipos de datos numéricos (enteros, flotantes y complejos).
- `03-string-data-type.py`: Manipulación de cadenas de caracteres y concatenación.
- `04-collections.py`: Introducción a listas, tuplas y diccionarios.
- `05-categorize-values.py`: Clasificación de diferentes tipos de datos dentro de colecciones mixtas.
- `06-composite-data.py`: Creación y manejo de estructuras compuestas a partir de archivos como `car_fleet.csv`.
- `07-workWithConditionals.py`: Control de flujo mediante condicionales básicas.
- `07.1-validador-de-datos.py`: Ejemplo práctico de lógica de condicionales con validación de edad y presupuesto.
- `08-while-loop.py`: Uso de bucles controlados por condiciones.
- `08.1-for-loop.py`: Uso de bucles de conteo definido.
- `10-analyze-insulin.py`: Procesamiento y limpieza de secuencias de ADN/proteínas mediante expresiones regulares.
- `11-string-insulin.py`: Análisis de cadenas aplicadas al cálculo molecular.
- `12-net-charge.py`: Cálculo de la carga neta de la insulina a través de diferentes niveles de pH mediante bucles y diccionarios.
- `13-caesar-cipher.py`: Implementación del cifrado y descifrado César mediante funciones personalizadas.
- `14.1-calc_weight_json.py`: Script principal que calcula el peso molecular de la insulina importando un módulo personalizado.
- `jsonFileHandler.py`: Módulo auxiliar para la lectura segura de archivos JSON con control de errores.
- `sys-admin.py`: Interacción con el sistema operativo para ejecutar comandos y listar procesos activos.
- `debugCipher1.py` a `debugCipher4.py`: Ejercicios diseñados para aprender a depurar errores en implementaciones del cifrado César.
- `car_fleet.csv`: Archivo de datos CSV utilizado en el ejercicio de datos compuestos.
- `files/insulin.json`: Archivo con datos estructurados de moléculas y pesos moleculares.

## Cómo ejecutar los scripts del repositorio

1. Abra su entorno de AWS Cloud9.
2. Clone este repositorio o navegue al directorio donde se encuentra el proyecto.
3. Para ejecutar cualquier archivo de Python, utilice el comando en la terminal integrada:
   ```bash
   python3 nombre_del_archivo.py
   ```
   Por ejemplo, para el caso de cálculo molecular:
   ```bash
   python3 14.1-calc_weight_json.py
   ```