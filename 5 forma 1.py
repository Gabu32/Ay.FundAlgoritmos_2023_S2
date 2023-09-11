# Leemos altura
altura = int(input())

# Verificamos que sea un valor valido
while altura <= 0 or altura >= 21:
    altura = int(input())

# Iniciamos contador para la cantidad de asteriscos a imprimir
cont = 1

# En cada piso imprimos cantidad de asteriscos segun contador y aumentamos en 1 la cantidad
for piso in range(altura):
    print("*"*cont)
    cont += 1
