import time

counter = 0
preset = 3

digital_input = 0
previous_input = 0
digital_output = 0

try:
    while True:
        digital_input = int(input("Introduce 0 o 1: "))

        # Detectar flanco de subida (0 → 1)
        if digital_input == 1 and previous_input == 0:
            counter += 1
            print(f"Flanco detectado → Contador = {counter}")

        # Lógica de salida
        if counter >= preset:
            digital_output = 1
        else:
            digital_output = 0

        print(f"Salida: {digital_output}")

        # Guardar estado anterior
        previous_input = digital_input

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Simulación detenida")
