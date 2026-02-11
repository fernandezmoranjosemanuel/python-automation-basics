# Python Automation Basics

Repositorio de ejercicios en Python orientados a automatización industrial.

## Descripción
Este proyecto recoge pequeños scripts prácticos que simulan sensores industriales y el registro de datos, como primer contacto con Python aplicado a automatización y sistemas SCADA.

## Contenido
- `sensor_simulation.py`  
  Simulación básica de un sensor de temperatura en tiempo real.

- `sensor_logger.py`  
  Simulación de un sensor de temperatura con registro de datos en un archivo CSV generado automáticamente.

- `plot_temperature.py`  
  Lectura del CSV y visualización gráfica de los datos de temperatura.

- `multi_sensor_logger.py`  
  Simulación de múltiples sensores (temperatura y presión) con registro de datos de proceso.

- `multi_sensor_plot.py`  
  Lectura del CSV de múltiples sensores y visualización gráfica con **doble eje**: temperatura y presión.

- `digital_io_simulation.py`  
  Simulación de una entrada y una salida digital con lógica ON/OFF tipo PLC.

- `ton_timer.py`  
  Simulación de un **temporizador TON (retardo a la conexión)** típico de PLC.  
  La salida se activa automáticamente tras mantener la entrada activa durante 5 segundos.

## Cómo ejecutar
Ejecutar cualquiera de los scripts desde terminal:

```bash
python nombre_del_script.py
