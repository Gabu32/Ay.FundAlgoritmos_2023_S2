# Leemos los datos
patente = input()
categoriaVehiculo = int(input())
categoriaTarifa = input()
distanciaKm = float(input())

# Imprimimos los datos
print(f"Vehículo Placa Patente : {patente}")
print(f"Categoría del Vehículo : {categoriaVehiculo}")
print(f"Categoría Tarifa : {categoriaTarifa}")
print(f"Distancia recorrida por el vehículo = {distanciaKm} kms.")

# Dividimos los casos segun la categoria del vehiculo
if categoriaVehiculo == 1:
    # En este caso sabemos precio de la tarifa baja
    TARIFA_BAJA = 90

    # Calculamos los precios segun la categoria de la tarifa
    if categoriaTarifa == "BAJA":
        # Tarifa baja por km
        peaje = TARIFA_BAJA * distanciaKm

    elif categoriaTarifa == "MEDIA":
        # Doble de la tarifa baja por km
        peaje = 2*TARIFA_BAJA * distanciaKm

    else:
        # Triple de la tarifa baja por km
        peaje = 3*TARIFA_BAJA * distanciaKm

elif categoriaVehiculo == 2:
    # En este caso sabemos precio de la tarifa media
    TARIFA_MEDIA = 360

    if categoriaTarifa == "BAJA":
        # Mitad de la tarifa media por km
        peaje = TARIFA_MEDIA/2 * distanciaKm

    elif categoriaTarifa == "MEDIA":
        # Tarifa media por km
        peaje = TARIFA_MEDIA * distanciaKm

    else:
        # Triple de la tarifa baja por km
        peaje = 3*(TARIFA_MEDIA/2) * distanciaKm

elif categoriaVehiculo == 3:
    # En este caso sabemos precio de la tarifa alta
    TARIFA_ALTA = 780

    if categoriaTarifa == "BAJA":
        # Un tercio de la tarifa alta por km
        peaje = TARIFA_ALTA/3 * distanciaKm

    elif categoriaTarifa == "MEDIA":
        # Doble de la tarifa baja por km
        peaje = 2*(TARIFA_ALTA/3) * distanciaKm

    else:
        # Tarifa alta por km
        peaje = TARIFA_ALTA * distanciaKm

else:
    # En este caso sabemos precio de la tarifa baja
    TARIFA_BAJA = 100

    if categoriaTarifa == "BAJA":
        # Tarifa baja por km
        peaje = TARIFA_BAJA * distanciaKm

    elif categoriaTarifa == "MEDIA":
        # Triple de la tarifa baja por km
        peaje = 3*TARIFA_BAJA * distanciaKm

    else:
        # Quintuple de la tarifa baja por km
        peaje = 5*TARIFA_BAJA * distanciaKm

# Truncamos valor del peaje
peaje = int(peaje)
print(f"Valor del peaje calculado es ${peaje}")

# Caso no se aplica descuento
if(peaje < 2000):
    print("No se aplica descuento")

# Caso en los que si se aplica descuento
else:
    if(peaje < 5000):
        print("Se aplica descuento del 7%")
        descuento = peaje*0.07

    elif(peaje <= 10000):
        print("Se aplica descuento del 12%")
        descuento = peaje*0.12

    else:
        print("Se aplica descuento del 15%")
        descuento = peaje*0.15

    print(f"Valor Final del peaje a pagar es ${int(peaje-descuento)}")
