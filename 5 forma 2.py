# Verificamos altura
while True:
    altura = int(input())
    if altura > 0 and altura < 21: break

# En cada piso imprimos cantidad de asteriscos segun contador y aumentamos en 1 la cantidad
for contador in range(1, altura+1):
    print("*"*contador)
