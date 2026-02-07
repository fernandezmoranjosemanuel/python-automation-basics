import random
import time

print("Simulación de sensor de temperatura industrial")

while True:
    temperatura = random.uniform(20.0, 80.0)
    print(f"Temperatura actual: {temperatura:.2f} °C")
    time.sleep(1)
