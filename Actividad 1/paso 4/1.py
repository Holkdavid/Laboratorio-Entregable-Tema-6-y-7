def calculadora():
    while True:
        operacion = input("¿Qué operación deseas realizar? (+, -, *, / o 'salir'): ")
        if operacion.lower() == "salir":
            break
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        if operacion == "+":
            print(f"Resultado: {num1 + num2}")
        elif operacion == "-":
            print(f"Resultado: {num1 - num2}")
        elif operacion == "*":
            print(f"Resultado: {num1 * num2}")
        elif operacion == "/":
            print(f"Resultado: {num1 / num2}")
        else:
            print("Operación no válida.")
calculadora()
