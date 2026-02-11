import time

counter = 0
preset = 3

digital_input = 0
previous_input = 0
digital_output = 0
reset_digital_input = 0

try:
    while True:
        digital_input = int(input("Introduce 0 o 1: "))
        reset_digital_input = int(input("Introduce 1 para resetear: "))
        
        if reset_digital_input == 1 :
            digital_output = 0
            counter  = 0
            print("contador a 0 y salida a 0")

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
        
       

        time.sleep(2)

except KeyboardInterrupt:
    print("Simulación detenida")
