# Leemos dato como tipo 'int' (numero entero)
cantBotellas = int(input())

""" 
    Cada jaba puede transportar 12 botellas, por lo tanto para saber la cantidad
    de jabas que se pueden llenar completamente utilizamos el operador '//' (division entera)
    el cual nos devuelve el resultado de la division truncado.
    Para saber la cantidad de botellas sobrantes utilizamos el operador '%' (modulo)
"""
# el cual nos devuelve el resto de una division
cantJabas = cantBotellas//12
sobrantes = cantBotellas%12

# Imprimimos los resultados
print("Cantidad de jabas =",cantJabas)
print(f"quedan {sobrantes} sin trasladar")