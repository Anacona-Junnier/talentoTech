#Ejercicio para calcular la comisión del 13% por ventas totales

#Obtener información del vendedor
nombre = input("Digita tu nombre: ")
venta_total = float(input("¿Cuánto vendite? "))

#Calcular el 13% de las ventas para la comisión
comision = venta_total*0.13
print(comision)

#Redondeo
comision = round(comision, 2)
print(comision)

#Impresión de la información
print(f"Él vendedor {nombre} con un total de ventas {venta_total} pesos tiene una comisión con un 13% de {comision} pesos con un Total de: {round(comision+venta_total,2)}")
