# Leemos los datos
episodio = int(input())
nivel = int(input())

puntajeMin = int(input())
puntajeObtenido = int(input())

cantVidas = int(input())

# Caso jugador supera el nivel
if puntajeObtenido >= puntajeMin:
    print("Genial nivel superado !")

    # Calculamos la razon para saber la cantidad de estrellas
    razon = puntajeObtenido / puntajeMin

    # Segun valor de razon imprimimos mensaje correspondiente
    if razon < 2:
        print("Obtuviste 1 estrella.")
    
    elif razon < 3:
        print("Obtuviste 2 estrellas.")
        
    else:
        print("Obtuviste 3 estrellas.")
    
    # Caso es el ultimo nivel del episodio
    if nivel == 15:
       print("Completaste el episodio", episodio)
    
    # Cualquier otro caso
    else:
        print(f"Pasaste al nivel {nivel+1} del episodio {episodio}")
        

#Caso jugador falla el nivel
else:
    print("Nivel no superado NO lograste el objetivo")
    
    # Restamos cantidad de vidas del jugador
    cantVidas -= 1          # cantVidas = cantVidas - 1
    
    # Imprimimos mensaje segun cantidad de vidas restantes
    if cantVidas == 0:
        print("No te quedan más vidas.")
        
    elif cantVidas == 1:
        print("Te queda 1 vida.")
    
    else:
        print(f"Te quedan {cantVidas} vidas.")
    
    