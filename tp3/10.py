hemisferio = int(input("En que hemisferio se encuentra(1- Sur/2- Norte)? "))
dia = int(input("Que dia es? "))
mes =int(input("Que mes es? "))

if hemisferio==1:
    if (mes==3 and dia >=21) or (mes in[4,5]) or (mes == 6 and dia <=20):
        print("Otoño")
    elif (mes == 6 and dia >=21) or (mes in[7,8]) or (mes == 9 and dia <=20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes ==12 and dia <=20):
        print("Primavera")
    else:
        print("Verano")
elif hemisferio==2:
    if (mes==3 and dia >=21) or (mes in[4,5]) or (mes == 6 and dia <=20):
        print("Primavera")
    elif (mes == 6 and dia >=21) or (mes in[7,8]) or (mes == 9 and dia <=20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes ==12 and dia <=20):
        print("Otoño")
    else:
        print("Invierno")
else:
    print("Ingrese 1 o 2")