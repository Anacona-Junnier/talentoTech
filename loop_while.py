# monedas = 5

# while monedas > 0:
#     print(f'tengo {monedas} monedas')
#     monedas -= 1

respuesta = ""
while respuesta =="":
    respuesta = input('Digita tu nombre: ')


for nombre in respuesta:
    num = 2
    if(nombre == 'n'):
        continue
    else:
        print(nombre)

    while(num>0):
        print('Junnier')
        num -= 1