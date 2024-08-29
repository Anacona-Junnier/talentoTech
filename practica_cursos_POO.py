class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}"

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre_curso = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre_curso}")

    def eliminar_estudiante(self, nombre_estudiante):
        #Validar caracteres mayusculas o minusculas
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                self.estudiantes.remove(estudiante)
                print(f"Estudiante {nombre_estudiante} eliminado")
                return 
        print("NO se encontro el estudiante")

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)
        #Imprimir si no hay estudiantes

def inicio():
    curso = Curso("Noveno", "Julio")
    while(True):
        opcion = input("-"*10+"MENU"+"-"*10+"\n1.Agregar Estudiante \n2.Eliminar Estudiante \n3.Listar Estudiantes \n4.Salir \n")
        if(opcion == "1"):
            nombre = input("Digita el Nombre del Estudiante: ")
            edad = input("Digita la Edad del Estudiante: ")
            grado = input("Digita el Grado del Estudiante: ")
            estudiante = Estudiante(nombre, edad, grado)
            curso.agregar_estudiante(estudiante)
        elif (opcion == "2"):
            nombre_estudiante = input("Digita el Nombre del Estudiante a Eliminar: ")
            curso.eliminar_estudiante(nombre_estudiante)
        elif (opcion == "3"):
            curso.mostrar_estudiantes()
        elif(opcion=="4"):
            print("Gracias por usar nuestro Servicio")
            break
        else:
            print("Digita una opción CORRECTA")

inicio()