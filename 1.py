# Leemos la cantidad de notas a leer
cantidadNotas = int(input())

# Iteramos hasta la cantidad de notas
for iteracion in range(cantidadNotas):
    # Leemos la nota
    nota = float(input())
    
    # Si es la primera iteracion (primera nota leida) la guardamos como la menor
    if iteracion == 0:
        menorNota = nota
    
    # En cualquier otra iteracion revisamos si la nota leida actualmente es menor que la guardada
    elif nota < menorNota:
        menorNota = nota

# Imprimimos la nota menor
print("Menor nota final :", menorNota)