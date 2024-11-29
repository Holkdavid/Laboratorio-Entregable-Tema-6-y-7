lista = []
while True:
    elemento = input("Agrega un elemento (o escribe 'salir' para terminar): ")
    if elemento.lower() == "salir":
        break
    lista.append(elemento)
print("Lista final:", lista)
