import time
import random

digital_input = 0
digital_output = 0
timer_start = None
TON_DELAY = 5  # segundos
digital_input =int(input("pon 0 o 1:"))

try:
    while True:
        # Simula entrada automática
        
        current_time = time.time()

        if digital_input == 1:
            if timer_start is None:
                timer_start = current_time
                digital_output = 0
                print(f"Entrada ON → Temporizador arrancando...")

            elif current_time - timer_start >= TON_DELAY:
                digital_output = 1
                print(f"TON cumplido ({TON_DELAY}s) → Salida ON")

            else:
                digital_output = 0
                print(f"Entrada ON → Esperando retardo ({int(current_time - timer_start)}s)")

        else:
            timer_start = None
            digital_output = 0
            print("Entrada OFF → Salida OFF")

        time.sleep(1)

except KeyboardInterrupt:
    print("Simulación detenida")
