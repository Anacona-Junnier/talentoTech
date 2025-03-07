mi_lista = ['b','a','c','d']
otra_lista = ['Hola', 2 , 3.7]

#indice de letra
resultado = mi_lista.index('c')
print(resultado)

#imprimir un rango de la lista
resultado = mi_lista[0:2]
print(resultado)

#concatenación
print(mi_lista+otra_lista)

#mutable
mi_lista[0] = 'alfa'
print(mi_lista)

#Agregar un elementos a una lista Append
mi_lista.append('z')
print(mi_lista)

#Eliminar el último elemento
mi_lista.pop()
print(mi_lista)

#Eliminar un elemento en específico, se puede utilizar el método remove()
mi_lista.pop(0)
print(mi_lista) 

#Ordenar elementos de una lista
lista_desordenada = [5,1,8,2,4,3,6]
lista_desordenada.sort()
mi_lista.sort()
print(lista_desordenada)
print(mi_lista)