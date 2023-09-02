# Leemos la cantidad y precio de cada producto como tipo 'int' (numero entero)
cantBebida = int(input())
precioBebida = int(input())

cantPizzas = int(input())
precioPizzas = int(input())

cantPalomitas = int(input())
precioPalomitas = int(input())

# Leemos la cantidad de personas como tipo 'int' (numero entero)
cantPersonas = int(input())

# Calculamos el gasto total
# Para esto multiplicamos el valor de cada producto por la cantidad comprada y sumamos
totalGasto = cantBebida*precioBebida + cantPizzas*precioPizzas + cantPalomitas*precioPalomitas

# Para calcular la cuota dividimos el gasto total y dividimos por la cantidad de personas
# Redondeamos el resultado
cuota = round(totalGasto/cantPersonas)

# Calculamos el total de productos sumando la cantidad de cada producto
totalItems = cantBebida + cantPizzas + cantPalomitas

# Imprimimos los mensajes correspondientes
print("Total gasto compra =", totalGasto)
print("Valor cuota por invitado =", cuota)
print("Total items comprados =", totalItems)