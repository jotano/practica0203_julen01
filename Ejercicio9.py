palabra = input("Introduce una palabra: ").lower()
cantidad_de_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for letra in palabra:
    if letra in 'aeiou':
        cantidad_de_vocales[letra] += 1
for vocal in 'aeiou':
    print("La vocal", vocal, "aparece", cantidad_de_vocales[vocal], "veces.")
input("Pulsa enter para salir")