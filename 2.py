# Leemos la cantidad de personas
cantidadPersonas = int(input())

# Iniciamos un contador con la cantidad de personas que sean mayores de edad
cantidadMayoresEdad = 0

# Iteramos hasta la cantidad de personas
for iteracion in range(cantidadPersonas):
    # Leemos la edad
    edad = int(input())
    
    # Si edad es mayor o igual 18 (mayoria de edad) aumentamos contador
    if edad >= 18:
        cantidadMayoresEdad += 1    #cantidadMayoresEdad = cantidadMayoresEdad + 1

# Si contador es igual a 0, no habia ningun mayor de edad 
if cantidadMayoresEdad == 0:
    print("No hubo mayores de edad")

# Si contador es igual a la cantidad total todas las personas eran mayores de edad
elif cantidadMayoresEdad == cantidadPersonas:
    print("Todos eran mayores de edad")

# En cualquier otro caso se imprime la cantidad de mayores de edad
else:
    print("Cantidad de mayores de edad:",cantidadMayoresEdad)