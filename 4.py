# Importamos funcion 'sqrt' (raiz cuadrada) de la libreria math
from math import sqrt

# Leemos datos como tipo 'float' (numero real) 
ladoA = float(input())
ladoB = float(input())

# Utilizamos teorema de pitagoras para calcular la hipotenusa
hipotenusa = sqrt(pow(ladoA, 2) + pow(ladoB, 2))

# Imprimimos el resultado redondeando a la decima
print(round(hipotenusa,1))

"""
Alternativas para calcular hipotenusa:

1: hipotenusa = pow(pow(ladoA,2) + pow(ladoB, 2), 0.5)
2: hipotenusa = (ladoA**2 + ladoB**2) ** 0.5

"""