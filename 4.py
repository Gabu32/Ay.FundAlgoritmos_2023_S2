# Leemos los limites
A = int(input())
B = int(input())

# Iniciamos contador de la suma
suma = 0

# Iteramos desde limite inferior (A) hasta limite superior (B)
for num in range(A, B+1):
    # Si num es divisible por 2 y 3 se agrega a la suma
    if num % 2 == 0 and num % 3 == 0:
        suma += num                         # suma = suma + num

# Si la suma es 0 ningun numero cumplia la propiedad
if suma == 0:
    print("NO EXISTEN NUMEROS DIVISIBLES POR 2 Y POR 3 EN EL INTERVALO")

# En cualquier otro caso se imprime el resultado
else:
    print("SUMA =", suma)