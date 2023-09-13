cantPersonas = int(input())

totalRecaudado = 0

enviosStgo = 0
enviosNorte = 0
enviosSur = 0

montoCompraDebito = 0
montoCompraCredito = 0
cantidadDebito = 0
cantidadCredito = 0

for i in range(cantPersonas):
    rut = input()
    montoCompra = int(input())
    metodoPago = int(input())
    zonaEnvio = int(input())
    
    print("Rut Cliente :", rut)
    print("Monto Compra :", montoCompra)
    
    if metodoPago == 1: 
        tipoPago = "TARJETA DÉBITO"
        cantidadDebito += 1
    
    else: 
        tipoPago = "TARJETA CRÉDITO"
        cantidadCredito += 1
    
    if zonaEnvio == 1: 
        zona = "SANTIAGO"
        enviosStgo += 1
    
    elif zonaEnvio == 2: 
        zona = "NORTE"
        enviosNorte += 1
    
    else: 
        zona = "SUR"
        enviosSur += 1
    
    print("Forma de Pago :", tipoPago)
    print("Zona Destino :", zona)
    
    #Aplica descuento
    if montoCompra > 50000:
        # Monto menor o igual a 100000
        if montoCompra <= 100000:
            # Caso debito
            if metodoPago == 1: 
                descuento = 0.1
            
            # Caso credito
            else:
                descuento = 0.05
        
        elif montoCompra <= 500000:
            if metodoPago == 1:
                descuento = 0.2
            
            else:
                descuento = 0.1
        
        else:
            if metodoPago == 1:
                descuento = 0.4
            
            else:
                descuento = 0.25
    
        montoConDescuento = montoCompra - (montoCompra * descuento)
        montoConDescuento = round(montoConDescuento, 0)
        
        print(f"Porcentaje de descuento a aplicar = {round(descuento * 100)}%")
        print("Monto total de la compra con descuento =", montoConDescuento)
    
    #NO se aplica descuento
    else:
        print("No Tiene Descuento.")
        print("Monto total de la compra =", montoCompra)
        montoConDescuento = montoCompra
    
    totalRecaudado += montoConDescuento
    
    if metodoPago == 1: montoCompraDebito += montoConDescuento
    else: montoCompraCredito += montoConDescuento
    
    if zonaEnvio == 1 and montoConDescuento <= 100000:
        costoEnvio = 3000
    
    elif zonaEnvio == 2 and montoConDescuento <= 200000:
        costoEnvio = 6000
    
    elif zonaEnvio == 3 and montoConDescuento <= 300000:
        costoEnvio = 8000
    
    else:
        costoEnvio = 0
    
    print("Costo Envío =", costoEnvio)
    print(f"Monto final a pagar por compra y envío = ${montoConDescuento + costoEnvio}")
    print("")

totalRecaudado = round(totalRecaudado, 0)

porcentajeStgo = round(enviosStgo / cantPersonas * 100, 1)
porcentajeNorte = round(enviosNorte / cantPersonas * 100, 1)
porcentajeSur = round(enviosSur / cantPersonas * 100, 1)

print("\nREPORTE FINAL\n")
print(f"Monto total recaudado por concepto de ventas = ${totalRecaudado}")
print(f"Porcentaje de ventas enviadas a Santiago = {porcentajeStgo}%")
print(f"Porcentaje de ventas enviadas a Zona Norte = {porcentajeNorte}%")
print(f"Porcentaje de ventas enviadas a Zona Sur = {porcentajeSur}%")
print("Total de clientes que pagaron con tarjeta de débito =",cantidadDebito)
print("Total de clientes que pagaron con tarjeta de crédito =",cantidadCredito)

if cantidadDebito == 0:
    print("No se procesaron compras con tarjeta de débito")
else:
    promedioDebito = montoCompraDebito // cantidadDebito
    print(f"Promedio de ventas con tarjeta de débito = {promedioDebito}")
    

if cantidadCredito == 0:
    print("No se procesaron compras con tarjeta de crédito")
else:
    promedioCredito = montoCompraCredito // cantidadCredito
    print(f"Promedio de ventas con tarjeta de crédito = {promedioCredito}")
