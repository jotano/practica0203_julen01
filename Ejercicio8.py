palabra = input("Escribe una palabra:")
palabra_invertida = ""
for letra in palabra:
    palabra_invertida = letra + palabra_invertida
if palabra == palabra_invertida:
    print("Ésta palabra es un palíndromo")
else:
    print("Ésta palabra no es un palíndromo")
input("Pulsa enter para salir")

