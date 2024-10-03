import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "janacona",
        database = "empresa"
    )

def agregar_empreado(nombre, puesto, salario):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s,%s,%s)"
    valores = (nombre, puesto, salario)
    cursor.execute(query, valores)
    conexion.commit()
    print("Empleado agregado exitosamente")
    cursor.close()
    conexion.close()

def obtener_empleados():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)
    cursor.close()
    conexion.close()

#Actualizar DOS CAMPOS de un empleado
def actualizar_empleado(idEmpleado, nuevoPuesto, nuevoSalario):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE empleados SET puesto = %s, salario = %s WHERE id = %s"
    valores = (nuevoPuesto, nuevoSalario, idEmpleado)
    cursor.execute(query, valores)
    conexion.commit()
    print("Empleado actualizado exitosamente")
    cursor.close()
    conexion.close()

def eliminar_empleado(idEmpleado):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM empleados WHERE id = %s"
    cursor.execute(query, (idEmpleado,)) #Así se agrega una dupla para que funcione EXECUTE()
    conexion.commit()
    print("Empleado eliminado exitosamente.")
    cursor.close()
    conexion.close()

def menu():
    while True:
        print("-"*20+"\n Gestión de Empleados")
        print("1. Agregar empleado")
        print("2. Ver empleados")
        print("3. Actualizar puesto y salario")
        print("4. Eliminar empleado")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            puesto = input("Puesto: ")
            salario = float(input("Salario: "))
            agregar_empreado(nombre, puesto, salario)
        elif opcion == "2":
            obtener_empleados()
        elif opcion == "3":
            idEmpleado = int(input("ID del empleado a actualizar: "))
            nuevoPuesto = input("Nuevo puesto: ")
            nuevoSalario = float(input("Salario: "))
            actualizar_empleado(idEmpleado, nuevoPuesto, nuevoSalario)
        elif opcion == "4":
            idEmpleado = int(input("ID del empleado a eliminar: "))
            eliminar_empleado(idEmpleado)
        elif opcion == "5":
            break
        else:
            print("Opción incorrecta, intentelo nuevamente.")

menu()
