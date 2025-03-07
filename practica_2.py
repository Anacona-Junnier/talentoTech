#Práctica Formatear Cadenas 1
print("-------------------------------------------------------------------------------------")
nombre_asociado = input("Digita tu nombre de asociado: ")
numero_asociado = int(input("Digita tu numero de asociado: "))
print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado, numero_asociado))
print("-------------------------------------------------------------------------------------")

#Práctica Formatear Cadenas 2
puntos_nuevos = int(input("Digita los nuevos puntos: "))
puntos_totales = puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
print("-------------------------------------------------------------------------------------")


#Práctica Formatear Cadenas 3
puntos_anteriores = puntos_totales
puntos_nuevos = int(input("Digita los nuevos puntos: "))
puntos_totales = puntos_anteriores+puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
print(f"Los puntos anteriores son ({puntos_anteriores}), los puntos nuevos son ({puntos_nuevos}) y tus puntos totales son ({puntos_totales}))")
print("-------------------------------------------------------------------------------------")


