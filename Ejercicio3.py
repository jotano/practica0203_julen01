asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = float(input("Introduce la nota que has sacado en " + asignatura + ": "))
    notas.append(nota)
print("Notas introducidas por el usuario:")
for j in range(len(asignaturas)):
    mensaje = "En " + asignaturas[j] + " has sacado " + str(notas[j])
    print(mensaje)
input("Pulsa enter para salir")
