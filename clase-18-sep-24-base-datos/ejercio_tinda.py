#Las BD son transaccionales
import mysql.connector

#Genera la conexión
conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'janacona'
)

#Generar cursor para poder hacer sentencias sql
cursor = conexion.cursor()

#Generar transacción
cursor.execute("CREATE DATABASE IF NOT EXISTS tienda")
#Confirmar y Cerrar transacción para que sean permatenentes los cambios
conexion.commit()

#Generar nuevamente la conexión especificando la BD anteriormente creada
conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'janacona',
    database = 'tienda'
)

#Crear tablas
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE productos (
    idProducto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio DECIMAL(10,2) NOT NULL
)
""")
cursor.execute("""
CREATE TABLE ventas (
    idVenta INT AUTO_INCREMENT PRIMARY KEY,
    idProducto INT NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (idProducto) REFERENCES productos (idProducto)
)
""")

#Ingresar datos 
cursor.execute("""
INSERT INTO productos (nombre, precio) VALUES ('Leche',3000),('Pan',4000),('Huevos',20000)
""")
conexion.commit()   

cursor.execute("""
INSERT INTO ventas (idProducto, cantidad, fecha)
VALUES (1, 3, '2024-04-18')
""")
conexion.commit()

#Cerrar el objeto cursor
cursor.close()
#Cerrar la conexion
conexion.close()