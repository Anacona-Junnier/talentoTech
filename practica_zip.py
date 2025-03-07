# #TEORIA
# letras = ['A', 'B', 'C']
# numeros = [4,5,6,7,8,9,10,11,12,13]

# obj = list(zip(letras,numeros))
# print(obj)
# for letra, numero in obj:
#     print(f'{numero} y {letra}')

#Practica 1
capitales = ['Berlín', 'Tokio', 'París', 'Helsinki',  'Ottawa', 'Canberra']
paises = ['Alemania', 'Japón', 'Francia', 'Finlandia', 'Canada', 'Australia']

combinada = list(zip(capitales, paises))
#print(combinada)

for capital, pais in combinada:
    print(f'La capital de {capital} es {pais}')

#Practica 2
marcas = ['Mattelsa', 'Adidas', 'Koaj']
productos = ['Camisas', 'Tenis', 'Pantalones']

mi_zip = list(zip(marcas, productos))

for marca, producto in mi_zip:
    print(f'La tienda {marca} tiene {producto}')

#Practica 3
lista_numeros = ['uno / um / one', 'dos / dois / two', 'tres / três / three', 'cuatro / quatro / four', 'cinco / cinco / five']
orden = [1,2,3,4,5]

for numero, idioma in zip(orden, lista_numeros):
    print(f'{numero}. {idioma}') 
