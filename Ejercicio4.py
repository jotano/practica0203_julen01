ganadores = []
for j in range(6):
    numero = int(input("Cuales han sido los números ganadores de la lotería? "))
    ganadores.append(numero)
ganadores.sort()
print("Éstos son los números ganadores ordenados de menor a mayor:")
for numero in ganadores:
    print(numero)
input("Pulsa enter para salir")
