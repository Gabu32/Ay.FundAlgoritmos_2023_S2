# Leemos altura y ancho
altura = int(input())
ancho = int(input())

# Realizamos 2 ciclos representando la altura y ancho
for i in range(altura):
    for j in range(ancho):
        # En cada iteracion del ancho imprimimos un asterisco
        print("*",end='')
        
    # En cada iteracion de altura imprimimos un espacio
    print("")