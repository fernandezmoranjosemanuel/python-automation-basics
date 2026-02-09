import csv
import matplotlib.pyplot as plt

timestamps = []
temperatures = []

with open("temperature_log.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # saltar cabecera

    for row in reader:
        timestamps.append(row[0])
        temperatures.append(float(row[1]))

plt.plot(temperatures)
plt.title("Temperatura registrada")
plt.xlabel("Muestras")
plt.ylabel("Temperatura (°C)")
plt.show()
