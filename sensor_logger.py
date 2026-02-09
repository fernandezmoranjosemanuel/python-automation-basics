import random
import time
import csv
import os
print("CSV se creará en esta carpeta:", os.getcwd())

from datetime import datetime

with open("temperature_log.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature"])

    print("Registrando temperatura... (Ctrl+C para parar)")

    while True:
        temperature = round(random.uniform(200, 800), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, temperature])
        print(timestamp, "-", temperature, "°C")
        time.sleep(2)
