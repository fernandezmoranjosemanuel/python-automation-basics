import csv
import matplotlib.pyplot as plt

timestamps = []
temperatures = []
pressures = []  # corregido el nombre

with open("process_data.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # saltar cabecera

    for row in reader:
        timestamps.append(row[0])
        temperatures.append(float(row[1]))
        pressures.append(float(row[2]))  # ahora sí estamos cogiendo la columna correcta
        
# Crear figura y eje principal
fig, ax1 = plt.subplots()

# Línea de temperatura (eje izquierdo)
ax1.plot(temperatures, color='red', label='Temperatura (°C)')
ax1.set_xlabel("Muestras")
ax1.set_ylabel("Temperatura (°C)", color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Crear segundo eje Y para la presión
ax2 = ax1.twinx()
ax2.plot(pressures, color='blue', label='Presión (bar)')
ax2.set_ylabel("Presión (bar)", color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Título y leyenda
plt.title("Temperatura y Presión registradas")
fig.tight_layout()
plt.show()
