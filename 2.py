# Realizamos ciclo para validar numero
while True:
    # Leemos el numero
    n = int(input())
    # En el caso de cumplir con la condicion necesaria se termina el ciclo
    if n >= 1: break

# Iniciamos las variables para la sumatoria
suma = 0

numerador = 1
denominador = 2

# Iteramos hasta n
for i in range(n):
    # Agregamos resultado a la suma
    suma += numerador/denominador

    # En cada ciclo al numerador y denominador se les suma 2
    numerador += 3
    denominador += 3

# Imprimimos resultado
print("El resultado de la sumatoria es", suma)