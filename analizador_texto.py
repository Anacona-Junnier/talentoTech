texto = "Hola mundo soy Junnier"

#crear lista a partir de un texto
print("\n Convertir texto a lista")
palabra = texto.split()
print(f"{palabra} tienes {len(palabra)}")

print("\n LETRA DE INICIO Y DE FIN")
letraInicio = texto[0]
letraFin = texto[-1]
print(f"La letra de inicial es {letraInicio} y la letra final es {letraFin}")

print("\n TEXTO INVERTIDO")
palabra.reverse()
#AGREGAR ESPACIOS entre palabras
textoInvertido = ' '.join(palabra)
print(f"si ordenamos tu texto al reves va a decir: {textoInvertido}")

print("\n BUSCANDO LA PALABRA \'mundo\' EN EL TEXTO")
buscarPalabra = 'mundo' in texto

dic = {True:"si", False:"no"}
print(f"La palabra \'mundo\' {dic[buscarPalabra]} se encuentra en el texto")