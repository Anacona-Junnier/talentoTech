class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.prestados = 0

    def disponible(self):
        return self.ejemplares - self.prestados

    def prestar(self):
        if self.disponible() > 0:
            self.prestados += 1
            print(f"Has tomado prestado el libro '{self.titulo}' de {self.autor}")
            return True
        else:
            print(f"Lo siento, no hay ejemplares disponibles de '{self.titulo}' en este momento.")
            return False

    def devolver(self):
        if self.prestados > 0:
            self.prestados -= 1
            print(f"Has devuelto el libro '{self.titulo}' de {self.autor}")
        else:
            print(f"No tienes ejemplares de '{self.titulo}' para devolver.")

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} - Disponibles: {self.disponible()}"


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        else:
            return False

    def devolver(self, libro):
        libro.devolver()
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def libros_prestados_str(self):
        if self.libros_prestados:
            return ", ".join([libro.titulo for libro in self.libros_prestados])
        else:
            return "Ninguno"

    def __str__(self):
        return f"Usuario: {self.nombre} - Libros prestados: {self.libros_prestados_str()}"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def registrar_usuario(self, nombre):
        self.usuarios.append(Usuario(nombre))

    def buscar_libro(self, titulo):
        resultados = [libro for libro in self.catalogo if titulo.lower() in libro.titulo.lower()]
        if resultados:
            print(f"Resultados de búsqueda para '{titulo}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontró ningún libro con el título '{titulo}' en {self.nombre}.")

    def mostrar_catalogo(self):
        print(f"Catálogo de libros en {self.nombre}:")
        for libro in self.catalogo:
            print(libro)
        print()

    def mostrar_usuarios(self):
        print(f"Usuarios registrados en {self.nombre}:")
        for usuario in self.usuarios:
            print(usuario)
        print()

    def gestionar_biblioteca(self):
        while True:
            print("\n### Bienvenido a la Biblioteca ###")
            print("1. Agregar libro al catálogo")
            print("2. Registrar nuevo usuario")
            print("3. Buscar libro por título")
            print("4. Mostrar catálogo de libros")
            print("5. Mostrar usuarios registrados")
            print("6. Prestar libro")
            print("7. Devolver libro")
            print("8. Salir")

            opcion = input("Ingrese el número de opción: ")

            if opcion == "1":
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                ejemplares = int(input("Ingrese la cantidad de ejemplares disponibles: "))
                self.agregar_libro(Libro(titulo, autor, ejemplares))
                print(f"El libro '{titulo}' de {autor} ha sido agregado al catálogo.")
            elif opcion == "2":
                nombre_usuario = input("Ingrese el nombre del nuevo usuario: ")
                self.registrar_usuario(nombre_usuario)
                print(f"Usuario '{nombre_usuario}' registrado exitosamente.")
            elif opcion == "3":
                titulo = input("Ingrese el título del libro que desea buscar: ")
                self.buscar_libro(titulo)
            elif opcion == "4":
                self.mostrar_catalogo()
            elif opcion == "5":
                self.mostrar_usuarios()
            elif opcion == "6":
                titulo = input("Ingrese el título del libro que desea prestar: ")
                libro = next((libro for libro in self.catalogo if libro.titulo.lower() == titulo.lower()), None)
                if libro:
                    nombre_usuario = input("Ingrese el nombre del usuario que desea tomar prestado el libro: ")
                    usuario = next((usuario for usuario in self.usuarios if usuario.nombre.lower() == nombre_usuario.lower()), None)
                    if usuario:
                        usuario.tomar_prestado(libro)
                    else:
                        print(f"No se encontró el usuario '{nombre_usuario}'.")
                else:
                    print(f"No se encontró el libro '{titulo}' en {self.nombre}.")
            elif opcion == "7":
                titulo = input("Ingrese el título del libro que desea devolver: ")
                libro = next((libro for libro in self.catalogo if libro.titulo.lower() == titulo.lower()), None)
                if libro:
                    nombre_usuario = input("Ingrese el nombre del usuario que desea devolver el libro: ")
                    usuario = next((usuario for usuario in self.usuarios if usuario.nombre.lower() == nombre_usuario.lower()), None)
                    if usuario:
                        usuario.devolver(libro)
                    else:
                        print(f"No se encontró el usuario '{nombre_usuario}'.")
                else:
                    print(f"No se encontró el libro '{titulo}' en {self.nombre}.")
            elif opcion == "8":
                print("Gracias por utilizar la Biblioteca. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")

# Ejemplo de uso:
if __name__ == "__main__":
    biblioteca = Biblioteca("Biblioteca Central")
    biblioteca.agregar_libro(Libro("El hobbit", "J.R.R. Tolkien", 5))
    biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 3))
    biblioteca.registrar_usuario("Juan")
    biblioteca.registrar_usuario("María")
    biblioteca.gestionar_biblioteca()