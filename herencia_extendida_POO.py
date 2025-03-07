class Mascota():
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas, color_ojos): #Se piden los atributos que vamos a heredar del Padre con el metodo Super()
        super().__init__(edad, nombre, cantidad_patas) #Aquí se especifica los atributos que vamos a utilizar del padre
        self.color_ojos = color_ojos

perro = Perro(2,"Zeus", 4, 'Azul')
print(perro.color_ojos)