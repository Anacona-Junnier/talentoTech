import mysql.connector

class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "janacona",
            database = "ContactosDB"
        )
        
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

class Contacto:
    def __init__(self):
        self.db = DataBase()

    def agregar_contacto(self, nombre, telefono, correo):
        query = "INSERT INTO contactos (nombre, telefono, correo) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (nombre, telefono, correo))
        print(f"Contacto {nombre} agregado correctamente.")

    def listar_contactos(self):
        query = "SELECT * FROM contactos"
        contactos = self.db.fetch_query(query)
        print("\n Lista de contactos")
        if not contactos:
            print("No hay contactos registrados")
        else:
            for contacto in contactos:
                print(f"ID: {contacto[0]},  NOMBRE: {contacto[1]}, TELEFONO: {contacto[2]}, CORREO: {contacto[3]}")

        print()

    def eliminar_contacto(self, id_contacto):
        query = "DELETE FROM contactos WHERE id = %s"
        self.db.execute_query(query, (id_contacto,))
        print(f"Contacto con ID {id_contacto} eliminado")

def menu():
    gestion_contacto = Contacto()

    while True:
        print("*"*10+" Menu de Gestión de Contactos "+"*"*10)
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Eliminar contacto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el telefono: ")
            correo = input("Ingrese el correo: ")
            gestion_contacto.agregar_contacto(nombre, telefono, correo)
        elif opcion == "2":
            gestion_contacto.listar_contactos()
        elif opcion == "3":
            id_contacto = int(input("Ingrese el ID del contacto a eliminar: "))
            gestion_contacto.eliminar_contacto(id_contacto)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida. Intentelo nuevamente.")

menu()