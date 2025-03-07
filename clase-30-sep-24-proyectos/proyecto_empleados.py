import mysql.connector

class DataBase:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "janacona",
            database = "EmpresaDB"
        )
        
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

class Empleado:
    
    def __init__(self, db):
        self.db = db

    def agregar_empleado(self, nombre, puesto_id, departamento_id, salario):
        query = "INSERT INTO empleados (nombre, puesto_id, departamento_id, salario) VALUES (%s, %s, %s, %s)"
        self.db.execute_query(query, (nombre, puesto_id, departamento_id, salario))
        print(f"Empleado {nombre} agregado correctamente.")

    def listar_empleados(self):
        query = "SELECT E.id, E.nombre, P.nombre, D.nombre, E.salario FROM empleados E JOIN puestos P ON E.puesto_id = P.id JOIN departamentos D ON E.departamento_id = D.id"
        empleados = self.db.fetch_query(query)
        print("\n Lista de contactos")
        if not empleados:
            print("No hay contactos registrados")
        else:
            for empleado in empleados:
                print(f"ID: {empleado[0]},  EMPLEADO: {empleado[1]}, PUESTO: {empleado[2]}, DEPARTAMENTO: {empleado[3]} SALARIO: {empleado[4]}")

    def actualizar_empleado(self, id_empleado, nuevo_salario):
        query = "UPDATE empleados SET salario = %s WHERE id = %s"
        self.db.execute_query(query, (id_empleado, nuevo_salario))
        print(f"Salario del empleado con ID {id_empleado}, actualizado a {nuevo_salario}")

    def eliminar_empleado(self, id_empleado):
        query = "DELETE FROM empleados WHEERE id = %s"
        self.db.execute_query(query, (id_empleado,))
        print(f"Empleado con ID {id_empleado} eliminado.")