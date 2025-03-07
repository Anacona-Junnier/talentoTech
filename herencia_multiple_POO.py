class Padre:
    def hablar(self):
        print("Hola, soy el Padre")

class Madre:
    def hablar(self):
        print("Hola, soy la Madre")

class Hijo(Madre, Padre): #Dependiendo el orden de la harencia se ejecutara primero
    pass

class Nieto(Hijo):
    pass

nieto = Nieto()
nieto.hablar()

print(Nieto.__mro__) #Método Especial para ver el árbol de herencia