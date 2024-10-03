import mysql.connector

#crear primera conexión
conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'janacona'
)

#Crear el cursor
cursor = conexion.cursor()
#Crear transacción
cursor.execute("CREATE DATABASE IF NOT EXISTS universidad")
#Hacer los cambios de la transacción permantentes en la BD y cerrar el hilo
conexion.commit()
#Cerrar cursor de la primara conexión
cursor.close()
#Cerrar conexión
conexion.close()

#Volver a crear la conexión pero con la Base de Datos especificada
conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'janacona',
    database = 'universidad'
)
cursor = conexion.cursor()

#Crear tablas
cursor.execute("""
CREATE TABLE estudiantes (
    idEstudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    edad INT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE cursos (
    idCurso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    creditos INT NOT NULL
)
""")

#Insertar datos
cursor.execute("""
INSERT INTO estudiantes (nombre, edad)
VALUES ('Julian',24),('Camila',20),('Melissa',26)
""")
cursor.execute("""
INSERT INTO cursos (nombre, creditos)
VALUES ('Calculo', 4), ('Programación', 4), ('Álegra Lineal',3)
""")
conexion.commit()
cursor.close()
conexion.close()
