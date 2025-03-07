import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "janacona",
        database = "libreria"
    )

def agregar_libro(titulo, autor, precio):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO libros (titulo, autor, precio) VALUES (%s,%s,%s)"
    valores = (titulo, autor, precio)
    cursor.execute(query, valores)
    conexion.commit()
    print("Libro agregado exitosamente")
    cursor.close()
    conexion.close()

def obtener_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    for libro in libros:
        print(libro)
    cursor.close()
    conexion.close()

def actualizar_libro(libro_id, nuevo_precio):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE libros SET precio = %s WHERE id = %s"
    valores = (nuevo_precio, libro_id)
    cursor.execute(query, valores) 
    conexion.commit()
    print("Libro actualizado correctamente") 
    cursor.close()
    conexion.close()

def eliminar_libro(libro_id):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM libros WHERE id = %s"
    cursor.execute(query, (libro_id,))
    conexion.commit()
    print("Libro eliminado correctamente.")
    cursor.close()
    conexion.close()

def menu():
    while True: 
        print("\n MENU LIBRERIA")
        print("1. Agregar libro")
        print("2. Ver libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            precio = float(input("Precio: "))
            agregar_libro(titulo, autor, precio)
        elif opcion == "2":
            obtener_libros()
        elif opcion == "3":
            libro_id = int(input("ID del libro a actualizar: "))
            nuevo_precio = float(input("Nuevo precio: "))
            actualizar_libro(libro_id, nuevo_precio)
        elif opcion == "4":
            libro_id = int(input("ID del libro a eliminar: "))
            eliminar_libro(libro_id)
        elif opcion == "5":
            break
        else:
            print("Opcion no valida. Intentelo de nuevo.")

menu()