#Práctica Atributos 1
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)
print(f"Color de la casa: {casa_blanca.color}, número de pisos: {casa_blanca.cantidad_pisos}")

#Práctica Atributos 2
class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")
print(f"Caras del cubo: {cubo_rojo.caras}, Color del cubo: {cubo_rojo.color}")

#Práctica Atributos 3
class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", True, 17)
print(f"Especie: {harry_potter.especie}, Magico: {harry_potter.magico}, Edad: {harry_potter.edad}")