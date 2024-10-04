import mysql.connector

class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "janacona",
            database = "ParqueDB"
        )
        
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params)
        if not params:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

class Reserva:
    def __init__(self, db):
        self.db = db

    def agregar_reserva(self, nombre, fecha, numeroPersonas, tipoTour):
        query = "INSERT INTO reservas (nombre, fecha, personas, tipo_tour) VALUES (%s, %s, %s, %s)"
        self.db.execute_query(query, (nombre, fecha, numeroPersonas, tipoTour))
        print("Reserva exitosa.")

    def listar_reservas(self):
        query = "SELECT * FROM reservas"
        reservas = self.db.fetch_query(query)
        print("\n LISTA RESERVAS")
        if not reservas:
            print("NO HAY REGISTROS")
        else:
            for reserva in reservas:
                print(f"ID: {reserva[0]} Nombre: {reserva[1]} Fecha: {reserva[2]} Personas: {reserva[3]} Tipo Tour: {reserva[4]}")

    def actualizar_reserva(self, id, numeroPersonas, tipoTour):
        reserva = self.verificar_reserva(id)
        if not reserva:
            print("Reserva NO encontrada.")
        else:
            query = "UPDATE reservas SET personas = %s, tipo_tour = %s WHERE id = %s"
            self.db.execute_query(query, (numeroPersonas, tipoTour, id))
            print(f"Actualización exitosa, {reserva[1]}.")

    def eliminar_reserva(self, id):
        reserva = self.verificar_reserva(id)
        if not reserva:
            print("Reserva NO encontrada.")
        else:
            print(f"Nombre: {reserva[1]} Fecha: {reserva[2]}")
            query = "DELETE FROM reservas WHERE id = %s"
            self.db.execute_query(query, (id,))
            print("Reserva Eliminada.")
            
    def verificar_reserva(self, id):
        query = "SELECT * FROM reservas WHERE id = %s"
        reserva = self.db.fetch_query(query, (id,))
        return reserva


def main():
    db = DataBase()
    reserva = Reserva(db)
    
    while True:
    
        print("\n --MENÚ DE GESTIÓN DE RESERVAS --")
        print("1. Registrar nueva reserva.")
        print("2. Listar todas las reservas.")
        print("3. Actualizar una reserva.")
        print("4. Eliminar una reserva.")
        print("5. Salir.")
        
        opcion = int(input("Digite la opción: "))
        
        # if opcion == 1:
        #     nombre = input("Nombre: ")
        #     fecha = input("Fecha: ")
        #     numeroPersonas = int(input("Número de personas: "))
        #     tipoTour = input("Tipo Tour: ")
        #     reserva.agregar_reserva(nombre, fecha, numeroPersonas, tipoTour)
        # elif opcion == 2:
        #     reserva.listar_reservas()
        # elif opcion == 3:
        #     id = int(input("ID: "))
        #     numeroPersonas = int(input("Número de Personas: "))
        #     tipoTour = input("Tipo de Tour: ")
        #     reserva.actualizar_reserva(id, numeroPersonas, tipoTour)
        # elif opcion == 4:
        #     id = int(input("ID: "))
        #     reserva.eliminar_reserva(id)
        # elif opcion == 5:
        #     print("Saliendo...")
        #     break
        # else:
        #     print("Opción incorrecta. Intente de nuevo.")
        
        match opcion:
            case 1:
                nombre = input("Nombre: ")
                fecha = input("Fecha: ")
                numeroPersonas = int(input("Número de personas: "))
                tipoTour = input("Tipo Tour: ")
                reserva.agregar_reserva(nombre, fecha, numeroPersonas, tipoTour)
            case 2:
                reserva.listar_reservas()
            case 3:
                id = int(input("ID: "))
                numeroPersonas = int(input("Número de Personas: "))
                tipoTour = input("Tipo de Tour: ")
                reserva.actualizar_reserva(id, numeroPersonas, tipoTour)
            case 4:
                id = int(input("ID: "))
                reserva.eliminar_reserva(id)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opción incorrecta. Intente de nuevo.")
        
    # reserva.db.close_connection()
    db.close_connection()

main()
