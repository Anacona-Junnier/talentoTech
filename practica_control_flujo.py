# #Practica 1
# num1 = int(input("Ingresa un número: "))
# num2 = int(input("Ingresa otro número: "))

# if (num1>num2):
#     print(f"{num1} es MAYOR que {num2}")
# elif (num1<num2):
#     print(f"{num1} es MENOR que {num2}")
# else:
#     print(f"{num1} y {num2} son IGULAES")
    
# #Practica 2
# edad = int(input("Digita tu edad: "))
# tiene_licencia = input("Tienes licencia? Digita \'si\' ó \'no\': ")
# tiene_licencia = {'si': True, 'no':False}

# if edad>=18 and tiene_licencia==True:
#     print("Puedes conducir")
# elif edad<18:
#     print("No pudes conducir aún. Debes tener 18 años y contrar con una licencia")
# else:
#     print("No pudes conducir. Necesitas contar con una licencia")
    
#Practica 3
conocimientoPython = input('¿Sabes programar en Python? Digita \"si\" ó \"no\" ')
conocimientoIngles = input('¿Tienes conocimientos en Inglés? \"si\" ó \"no\" ')
print(conocimientoPython)
print(conocimientoIngles)

if conocimientoPython=='si' and conocimientoIngles=='si':
    print('Cumples con los requisitos para postularte')
elif conocimientoPython=='si':
    print('Para postularte, necesitas tener conocimientos en inglés')
elif conocimientoIngles=='si':
    print('Para postularte, necesitas saber programar en Python')
else:
    print('Para postularte, necesitas saber programar en Python y tener conocimientos en inglés')