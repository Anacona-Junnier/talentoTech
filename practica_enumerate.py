#Practica 1
lista_nombres = ['Marcos', 'Laura', 'Mónica', 'Javier', 'Celina', 'Marta']

for indice, item in enumerate(lista_nombres):
    print(f'{item} se encuentra en el índice {indice}')

#Practica 2
lista_indice = list('Python')

for indice, item in enumerate(lista_indice):
    print(indice, item)

#Practica 3
for indice, item in enumerate(lista_nombres):
    if(item[0]=='M'):
        print(f'{indice} , {item}')
