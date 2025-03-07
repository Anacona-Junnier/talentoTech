class Pelicula:
    def __init__(self, titulo):
        self.titulo = titulo
        self.vista = False

    def marcarVistaPelicula(self):
        self.vista = True

    def __str__(self):
        if self.vista:
            estado = "SI VISTA"
        else: 
            estado = "NO VISTA"
        return f"Pelicula: {self.titulo} - {estado}"

class ListaPeliculas:
    def __init__(self):
        self.listaPeliculas = []

    def agregarPelicula(self, titulo):
        pelicula = Pelicula(titulo)
        self.listaPeliculas.append(pelicula)
        print(f"Pelicula {titulo} agregada correctamente")

    def mostrarListaPeliculas(self):
        if self.listaPeliculas:
            print("LISTA DE PELICULAS")
            for i,pelicula in enumerate(self.listaPeliculas):
                print(f"{i}. {pelicula}")
            return True
        else:
            print("No hay peliculas en la lista")
            return False

    def marcarPeliculaVista(self, opcion):
        if 0 <= opcion <= len(self.listaPeliculas):
            self.listaPeliculas[opcion].marcarVistaPelicula()
            print(f"Pelicula {self.listaPeliculas[opcion].titulo} marcada como SI VISTA")
        else:
            print("Opción no valida")            

def mostrarMenu():
    print("\n GESTOR DE LISTA DE PELICULAS")
    print("1. Agregar pelicula \n2. Marcar pelicula como vista \n3. Mostrar todas las peliculas \n4. Salir")

def main():
    listaPeliculas = ListaPeliculas()
    
    while True:
        mostrarMenu()
        opcion = int(input("Digite una Opción: "))
        if opcion == 1:
            titulo = input("Ingrese el Titulo de la pelicula: ")
            listaPeliculas.agregarPelicula(titulo)
        elif opcion == 2:
            if listaPeliculas.mostrarListaPeliculas():
                indice = int(input("Digite el número de la Pelicula a marcar como SI VISTA: "))
                listaPeliculas.marcarPeliculaVista(indice)
            else: 
                print("Por favor, ingrese una pelicula")
        elif opcion == 3:
            if listaPeliculas.mostrarListaPeliculas() == False:
                print("Por favor, ingrese una pelicula")
        elif opcion == 4:
            print("Saliendo del Sistema...")
            break
        else:
            print("Opción incorrecta, ingrese un valor valida")
    
    print("Gracias por usar nuestro Sistema")

main()
