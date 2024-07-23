diccionario = {'c1':'valor', 'c2':'valor2'}
print(type(diccionario))

resultado = diccionario['c1']
print(resultado)

dic = {'c1': 55, 'c2':[14,20,30], 'c3':{'s1':100, 's2': 200}}
#Imprimir la DICCIONARIO-LISTA
print(dic['c2'][1])
#Imprimir DICCIONARIO-DICCIONARIO
print(dic['c3']['s2'])

#Agragar elemento al Diccionario
dic['c4'] = 'Junnier'
print(dic)

#Editar elemento en un Diccionario
dic['c4'] = 'JUNNIER'
print(dic)