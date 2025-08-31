import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

import statistics
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)
print(f"La media es {media}")
print(f"La mediana es {mediana}")
print(f"La moda es {moda}")

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("No hay sesgo")
