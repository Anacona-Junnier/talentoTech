import mysql.connector

def conectar():
    return mysql.connector.connect(
        host =  "localhost",
        user = "root",
        password = "janacona",
        database = "store"
    )

def registrar_producto(nombre, categoria, cantidad):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO products (nombre, categoria, cantidad) VALUES (%s, %s, %s)"
    values = (nombre, categoria, cantidad)
    cursor.execute(query, values)
    conexion.commit()
    print("Producto ingresado exitosamente")
    cursor.close()
    conexion.close()

def mostrar_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    cursor.close()
    conexion.close()

def actualizar_cantidad_categoria(idProducto, nuevaCantidad, nuevaCategoria):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE products SET cantidad = %s, categoria = %s WHERE id = %s"
    values = (nuevaCantidad, nuevaCategoria, idProducto)
    cursor.execute(query, values)
    conexion.commit()
    print("Producto actualizado exitosamente")
    cursor.close()
    conexion.close()

def eliminar_producto(idProducto):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM products WHERE id = %s"
    cursor.execute(query, (idProducto,))
    conexion.commit()
    print("Producto eliminado exitosamente")
    cursor.close()
    conexion.close()

def menu():
    while True:
        print("*"*20+"\nGestor Tienda")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Actualizar cantidad y categoría")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            cantidad = int(input("Cantidad: "))
            registrar_producto(nombre, categoria, cantidad)
        elif opcion == 2:
            mostrar_productos()
        elif opcion == 3:
            idProducto = int(input("ID del producto a actualizar: "))
            nuevaCategoria = input("Categoría: ")
            nuevaCantidad = int(input("Cantidad: "))
            actualizar_cantidad_categoria(idProducto, nuevaCantidad, nuevaCategoria)
        elif opcion == 4:
            idProducto = int(input("ID del producto a eliminar: "))
            eliminar_producto(idProducto)
        elif opcion == 5:
            break
        else:
            print("Opción incorrecta. Intentelo nuevamente.")
            

menu()