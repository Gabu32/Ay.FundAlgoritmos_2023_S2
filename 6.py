# Importamos la funcion 'exp' (exponente) de la libreria math
from math import exp

# Leemos los años como tipo 'int' (numero entero)
years = int(input())

# Leemos los siguientes datos como tipo 'float' (numero real)
poderPelea = float(input())
fuerza = float(input())
voluntad = float(input())
debilidad = float(input())

# Utilizando la formula despejamos y calculamos valor 'espiritu'
espiritu = exp(voluntad/debilidad)

# Utilizando la formula despejamos y calculamos 'agilidad'
agilidad = 4 * (pow(poderPelea/pow(years,2),2) - fuerza/2 - espiritu)

# Imprimimos el mensaje y redondeamos la 'agilidad' a la centesima
print("La agilidad que Goku debe alcanzar para enfrentar a los saiyajines es", round(agilidad,2))