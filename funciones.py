# #Practica 1 Crear Funciones
# def saludar():
#     print('¡Hola Mundo!')

# saludar()

# #Practica 2 
# def bienvenida(nombre_persona):
#     print(f'Bienvenido {nombre_persona}')

# nombre = input('Digita tu nombre: ')
# bienvenida(nombre)

# def cuadrado(un_numero):
#     print(un_numero**2)

# numero = int(input('Digita el número que deseas elevar al cuadrado: '))
# cuadrado(numero)



# #RETURN
# def multiplicar(numero1, numero2):
#     return numero1 * numero2

# resultado = multiplicar(5,10)
# print(resultado)





#Práctica Return 1
def potencia(base, exponente):
    return base**exponente

base = int(input('Digita tu base: '))
exponente = int(input('Digita un Exponente: '))
potencia = potencia(base, exponente)
print(f'Resultado: {potencia}')
