# Leemos n
n = int(input())

# Realimos un ciclo infinito puesto que no sabemos cuantas veces necesitaremos iterar
while True:
    # Imprimimos el numero
    print(n, end=" , ")
    
    # En el caso de ser par lo dividimos en 2
    if n % 2 == 0: 
        n = n//2
    
    # En cualquier otro caso (ser impar) lo multiplicamos por 3 y le sumamos 1
    else:
        n = n * 3 + 1
        
    # Si se llega al resultado deseado (1) imprimimos '1.' y terminamos el ciclo
    if n == 1:
        print("1.")
        break
        