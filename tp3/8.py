nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija como quiere leer su nombre: 1-Mayusculas 2-Minusculas 3-Primer Letra en mayuscula: "))

if opcion==1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
elif opcion==3:
    print(nombre.title())
else:
    print("Elija un numero de entre las opciones.")
    