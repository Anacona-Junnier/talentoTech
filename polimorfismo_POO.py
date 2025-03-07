#POLI = muchas, FORMISMO = formas, POLIMORFISMO = MUCHAS FORMAS
class vaca:
    def hablar(self):
        print('MUUUU')

class oveja:
    def hablar(self):
        print('MEEEE')

vaca1 = vaca()
oveja1 = oveja()

print("CON OBJETOS")
vaca1.hablar()
oveja1.hablar()

print("CON LOOP (BUCLE)")
animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()

print("CON FUNCIONES")
def animal_hablar(animal):
    animal.hablar()

animal_hablar(vaca1)
animal_hablar(oveja1)