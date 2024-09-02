#Práctica Herencia 1
class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

alumno = Alumno('Junnier', 22)
print(alumno.nombre)

#Práctica Herencia 2
class Mascota():
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas, color_ojos):
        super().__init__(edad, nombre, cantidad_patas)
        self.color_ojos = color_ojos

perro = Perro(2,"Zeus", 4, 'Azul')
print(perro.color_ojos)

#Práctica Herencia 3
class Vehiculo():
    def acelerar(self):
        pass
    
    def frenar(self):
        print("Has frenado!!!")

class Automovil(Vehiculo):
    pass

chevrolet = Automovil()
chevrolet.frenar()
