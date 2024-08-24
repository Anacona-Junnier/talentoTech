class Juguete:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        
    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio} - {self.cantidad} en Stock"
    
    def actualizarCantidad(self, cantidad):
        self.cantidad = cantidad
        
class AlmacenJuguete:
    def __init__(self):
        self.inventario = []
        
    def agregarJuguete(self, juguete):
        self.inventario.append(juguete)
    
    def eliminarJuguete(self, nombre):
        bandera = False
        for juguete in self.inventario:
            if juguete.nombre == nombre:
                self.inventario.remove(juguete)
                #return juguete
                return "Juguete Eliminado"
        #return None   
        return "NO se encontro el juguete"
        
    def listarJuguetes(self):
        if not self.inventario:
            print("no hay juguetes en el inventario")
        else:
            for juguete in self.inventario:
                print(juguete)
    
    def encontrarJuguete(self, nombre):
        for juguete in self.inventario:
            if juguete.nombre == nombre:
                return juguete
        return None
    
    def actualizarCantidadJuguete(self, nombre, cantidad):
        juguete = self.encontrarJuguete(nombre)
        if juguete:
            juguete.actualizarCantidad(cantidad)
        else:
            print(f"juguete {nombre} no encontrado ")
            

def mostrarMenu():
    print("MENU DEL ALMACEN DE JUGUETES")
    print("1. Agregar Juguete")
    print("2. Eliminar Juguete")
    print("3. Listar Juguetes")
    print("4. Encontrar Juguete")
    print("5. Actualizar Cantidad de Juguetes")
    print("6. Salir")
    
def main():
    almacen = AlmacenJuguete()
    
    while True:
        mostrarMenu()
        opcion = int(input("ingrese la opcion: "))
        
        if opcion == 1:
            nombre = input("Ingrese el nombre del juguete: ")
            categoria = input("Ingrese la categoria del juguete: ")
            precio = float(input("Ingrese el precio del juguete: "))
            cantidad = int(input("Ingrese la cantidad del juguete: "))
            juguete = Juguete(nombre, categoria, precio, cantidad)
            almacen.agregarJuguete(juguete)
            print(f"Juguete: {nombre} agregado")
            
        elif opcion == 2:
            nombre = input("Ingrese el nombre del juguete: ")
            resultado = almacen.eliminarJuguete(nombre)
            print(resultado)
            # if resultado:
            #     print("eliminado")
            # else:
            #     print("no encontrado")
        
        elif opcion == 3:
            almacen.listarJuguetes()
        
        elif opcion == 4:
            nombre = input("Ingrese el nombre del juguete: ")
            juguete = almacen.encontrarJuguete(nombre)
            if juguete:
                print(juguete)
            else:
                print(f"juguete {nombre} no encontrado")
                
        elif opcion == 5:
            nombre = input("Ingrese el nombre del juguete: ")
            cantidad = int(input("Ingrese la cantidad del juguete: "))
            almacen.actualizarCantidadJuguete(nombre, cantidad)
            print(f"cantidad del juguete {nombre} actualizada")
            
        elif opcion == 6:
            print("saliendo....")
            break
        else:
            print("opcion invalida....")

if __name__ == "__main__":
    main()
            
            
            