import random
numero_secreto = random.randint(1, 100)
while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento < numero_secreto:
        print("Más alto.")
    elif intento > numero_secreto:
        print("Más bajo.")
    else:
        print("¡Felicidades! Adivinaste.")
        break
