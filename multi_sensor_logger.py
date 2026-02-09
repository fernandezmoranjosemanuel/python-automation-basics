import csv
import time
import random
from datetime import datetime

with open("process_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature", "pressure"])

    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            temperature = round(random.uniform(20, 80), 2)
            pressure = round(random.uniform(1.0, 5.0), 2)

            writer.writerow([timestamp, temperature, pressure])
            print(f"T={temperature} °C | P={pressure} bar")

            time.sleep(1)

    except KeyboardInterrupt:
        print("Registro detenido")
