# Leemos altura y ancho
altura = int(input())
ancho = int(input())

# Iteramos hasta la altura
for i in range(altura):
    # En cada 'piso' imprimimos la cantidad de asteriscos del ancho
    print("*"*ancho)