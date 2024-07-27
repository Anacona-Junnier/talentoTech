# #Practica 2
# div = 17834/34
# multi = 87*56
# print(div > multi)

# Ejercicio 3
texto = input("Digita un texto: ")
textoMinus = texto.lower()

letras = input("Digite 3 letras: ")
letrasMinus = letras.lower()

listaLetras = list(letrasMinus) 

cantidad_letra1 = textoMinus.count(listaLetras[0])
cantidad_letra2 = textoMinus.count(listaLetras[1])
cantidad_letra3 = textoMinus.count(listaLetras[2])

print(f"Hemos encontrado la letra {listaLetras[0]} repetida {cantidad_letra1} veces")
print(f"Hemos encontrado la letra {listaLetras[1]} repetida {cantidad_letra2} veces")
print(f"Hemos encontrado la letra {listaLetras[2]} repetida {cantidad_letra3} veces")

#Ejercicio 3 desarrollado en clases
# texto = input("Digite un texto: ")
# texto = texto.lower()

# letra = []
# letra.append(input("Digite la primera letra: ").lower())
# letra.append(input("Digite la segunda letra: ").lower())
# letra.append(input("Digite la tercera letra: ").lower())

# #comparaciones
# cantidad_letra1 = texto.count(letra[0])
# cantidad_letra2 = texto.count(letra[1])
# cantidad_letra3 = texto.count(letra[2])

# print(f"En el texto se encontró la letra {letra[0]} repetida {cantidad_letra1} veces")
# print(f"En el texto se encontró la letra {letra[1]} repetida {cantidad_letra2} veces")
# print(f"En el texto se encontró la letra {letra[2]} repetida {cantidad_letra3} veces")


