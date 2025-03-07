#Práctica Métodos 1
class Perro:
    def ladrar(self):
        print("Guau!")

zeus = Perro()
zeus.ladrar()

#Práctica Métodos 2
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

#Práctica Métodos 3
class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

reloj = Alarma()
reloj.postergar(10)