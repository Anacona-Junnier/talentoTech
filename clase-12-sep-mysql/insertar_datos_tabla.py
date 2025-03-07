import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "janacona",
    database = "testdb"
)

myCursor = mydb.cursor()

sentenciaSql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
datos = [("Junnier", "janco@gmail.com",26), ("Alexis", "alexis@gmail.com",20), ("Mauricio", "mauricio@gmail.com",23), ("Camila", "cami@gmail.com", 24)]

myCursor.executemany(sentenciaSql, datos)
mydb.commit()
#Para Insertar, Actualizar y Eliminar se necesita COMMIT() para hacer permatente los cambios