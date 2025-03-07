# #Practica 1
# mi_lista = list(range(2500, 2586))
# print(mi_lista)

# #Practica 2
# mi_lista = list(range(3,301,3))
# print(mi_lista)

#Practica 3
rango = list(range(1,16))
suma_cuadrados = 0

for item in rango:
    resultado = item**2
    print(f"{item}^{2} resultado: {resultado}")
    suma_cuadrados += resultado

print(f"Total: {suma_cuadrados}")

