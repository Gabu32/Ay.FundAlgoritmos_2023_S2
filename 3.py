# Leemos N
N = int(input())

# Iteramos desde 1 hasta N 
for num in range(1, N+1):
    # Revisamos condicion de que el numero no sea multiplo de 3 ni 7
    if num % 3 != 0 and num % 7 != 0:
        # Si cumple condicion se imprime
        print(num,end=' ')
    