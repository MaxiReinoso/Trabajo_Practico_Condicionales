edad = int(input("Ingrese su edad por favor: "))
if edad <12:
    print("Usted es un niño")
else:
    if edad >= 12 and edad<18 :
        print("Usted es un adolescente")
    else:
        if edad >= 18 and edad < 30:
            print("Usted es un adulto jóven")
        else:
            print("Usted es un adulto")
            