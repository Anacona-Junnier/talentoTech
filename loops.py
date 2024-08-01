#Loop FOR
lista = ['a','b','c']

for letra in lista:
    print(letra)

for letra in lista:
    indice_lista = lista.index(letra)
    print(f"La letra {letra} esta en el indice {indice_lista}")

lista_nombres = ['pablo', 'junnier', 'juliana', 'luis']

for nombre in lista_nombres:
    if nombre.startswith('j'):
        print(nombre)
    else:
        print('El nombre no inicia con la letra \'j\'')

dic = {'edad': 18, 'nombre':'junnier', 'apellido':'anacona'}

##Imprimir las CLAVES
# for item, nombre in dic:
#     print(item)

#Imprimir los VALORES
for item in dic.values():
    print(item)

#Imprimir las CLAVE junto al VALOR (items)
for item in dic.items():
    print(item)




