import time
import random

digital_input = 1
digital_output = 0
timer_start = None
TOF_DELAY = 5

try:
    while True:
        # Simula cambio de sensor cada 7 segundos
        if int(time.time()) % 7 == 0:
            digital_input = random.choice([0, 1])

        current_time = time.time()

        if digital_input == 1:
            digital_output = 1
            timer_start = None
            print("Entrada ON → Salida ON")

        else:
            if timer_start is None:
                timer_start = current_time
                print("Entrada OFF → TOF arrancando...")

            elif current_time - timer_start >= TOF_DELAY:
                digital_output = 0
                print("⏹ TOF cumplido → Salida OFF")

            else:
                print(f"Salida mantenida → {int(current_time - timer_start)}s")

        time.sleep(1)

except KeyboardInterrupt:
    print("Simulación detenida")
