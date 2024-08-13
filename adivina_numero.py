from random import randint

intentos = 0
estimado = 0
numeroSecreto = randint(1,100)
nombre = input('Dime tu nombre: ')

print(f'Bueno {nombre}, he pensado en un número entre 1 y 100 \nTienes 8 intentos para adivinar')

while intentos <= 8:
    estimado = int(input('¿Cúal es el número?: '))
    intentos += 1
    
    if estimado < numeroSecreto:
        print('Mi número es más alto')
    elif estimado > numeroSecreto:
        print('Mi número más bajo')
    else:
        print(f'Felicitaciones {nombre}. Has ganado en {intentos}')
        break

if estimado != numeroSecreto:
    print(f'Lo siento :c se han acabado los intentos. El número secreto era: {numeroSecreto}')