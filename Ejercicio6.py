asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []
for asignatura in asignaturas:
    nota = float(input("¿Cual ha sido la nota que has sacado en " + asignatura + "? "))
    if nota < 5.0:
        repetir.append(asignatura)
    else:
        asignaturas.remove(asignatura)
print("Te toca repetir:")
for asignatura in repetir:
    print(asignatura)
input("Pulsa enter para salir")