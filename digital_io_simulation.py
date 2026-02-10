import time
import random

digital_input = False
digital_output = False

try:
    while True:
        digital_input = random.choice([True, False])

        if digital_input:
            digital_output = True
            print("Entrada ON → Salida ON")
        else:
            digital_output = False
            print("Entrada OFF → Salida OFF")

        time.sleep(1)

except KeyboardInterrupt:
    print("Simulación detenida")
