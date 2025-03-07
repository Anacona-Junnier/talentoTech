import mysql.connector

class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "janacona",
            database = "TiendaDB"
        )
        
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

class Producto:
    def __init__(self):
        self.db = DataBase()

    def agregar_producto(self, nombre, precio, cantidad):
        query = "INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (nombre, precio, cantidad))
        print(f"Producto {nombre} agregado correctamente")

    def listar_productos(self):
        query = "SELECT * FROM productos"
        productos = self.db.fetch_query(query)
        print("\n Lista de productos")
        if not productos:
            print("No hay productos registrados")
        else:
            for producto in productos:
                print(f"ID: {producto[0]},  NOMBRE: {producto[1]}, TELEFONO: {producto[2]}, CORREO: {producto[3]}")
        