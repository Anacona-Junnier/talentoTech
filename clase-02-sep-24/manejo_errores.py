#Teoría
# try:
#     print("Este es el codigo que INTENTARA ejecutarse sin errores")
# except (): #En los entreparentesis va el TIPO DE ERROR a controlar
#     print("Manejo de errores")
# else: 
#     print("Se ejecuta esta parte del codigo cuando no hay errores, despues del try")
# finally:
#     print("Siempre se va a ejecutar a pesar de que existan errores o no")

#try---except
def sumar():
    try:
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
    except ValueError:
        print("Error: por favor ingrese solo números")
    else: 
        print(n1+n2)
        print("Gracias por sumar")
    finally:
        print("Esto fue todo...")

sumar()