numeros = list(range(1, 11))
numeros.reverse()
for numero in numeros:
    if numero != numeros[-1]:
        print(numero, end=", ")
    else:
        print(numero)
input("Pulsa enter para salir")
