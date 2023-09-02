# Leemos los datos
cargoFijo = float(input())
cantLitros = float(input())
valorConsumido = float(input())
valorRecoleccion = float(input())
valorTratamiento = float(input())

print("BOLETA ESVALPITO")
print(f"Cargo Fijo = ${cargoFijo}")

# Los calculos se realizan con metros cubicos de agua, pero en los datos nos lo dan en litros
# Convertimos la cantidad de litros a metros cubicos
cantMetrosCubicos = cantLitros / 1000

# Calculamos el valor total de cada servicio
precioConsumido = valorConsumido * cantMetrosCubicos
precioRecolectado = valorRecoleccion * cantMetrosCubicos
precioTratado = valorTratamiento * cantMetrosCubicos

# Sumamos todos los precios de los servicios para calcular la suma total del servicio
sumaTotal = precioConsumido + precioRecolectado + precioTratado + cargoFijo

print("Metros cúbicos de agua consumidos =",cantMetrosCubicos)
print(f"Monto parcial por agua consumida = ${precioConsumido}")
print(f"Monto parcial por agua recolectada = ${precioRecolectado}")
print(f"Monto parcial por agua tratada = ${precioTratado}")

# Caso cliente presenta sobreconsumo
if cantMetrosCubicos >= 40:
    
    if cantMetrosCubicos < 45:
        recargo = sumaTotal * 0.15
        totalFinal = sumaTotal + recargo
        print("Cliente presenta sobreconsumo, su recargo es de un 15%")
        
    elif cantMetrosCubicos < 50:
        recargo = sumaTotal * 0.20
        totalFinal = sumaTotal + recargo
        print("Cliente presenta sobreconsumo, su recargo es de un 20%")
        
    elif cantMetrosCubicos < 65:
        recargo = sumaTotal * 0.30
        totalFinal = sumaTotal + recargo
        print("Cliente presenta sobreconsumo, su recargo es de un 30%")
        
    else:
        recargo = sumaTotal * 0.55
        totalFinal = sumaTotal + recargo
        print("Cliente presenta sobreconsumo, su recargo es de un 55%")
    
    print(f"Monto Total Antes del recargo = ${sumaTotal}")
    print(f"Monto Total a Pagar = ${totalFinal}")

# Caso cliente no tiene sobreconsumo    
else:
    print("Cliente no presenta sobreconsumo")
    print(f"Monto Total a Pagar = ${sumaTotal}")
    
   
    
    
   