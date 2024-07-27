#Ejercicio 1
mi_tupla = (1, 2, 3, 2, 3, 1, 2, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
num_repeticion = mi_tupla.count(2)
print(num_repeticion)

#Ejercicio 2
mi_tupla = (1, 2, 3, 3, 2, 1, 2)
mi_lista = list(mi_tupla)
print(type(mi_lista))

#Ejericicio 3
mi_tupla = (1, 2, (3,6), 4)
a,b,c,d = mi_tupla
print(a,b,c,d)
x,z = c
print(x,z)
