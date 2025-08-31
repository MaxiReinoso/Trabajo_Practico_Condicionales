oracion = input("Escriba una oracion: ")

if oracion[-1] in "aeiouAEIOU":
    print(f"{oracion}!")
else:
    print(oracion)