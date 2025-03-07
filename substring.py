#Fragmentación de Strings
texto = "ABCDEFGHIJKLM"

#De la posición 2 hasta la 4
fragmento = texto[2:5]
print(fragmento)

#De la posición 2 hasta el último
fragmento = texto[2:]
print(fragmento)

#Desde la posición 0 hasta la 4
fragmento = texto[:5]
print(fragmento)

#Saltos de 2 en 2
fragmento = texto[::2]
print(fragmento)

#Invertir texto
fragmento = texto[::-1]
print(fragmento)


