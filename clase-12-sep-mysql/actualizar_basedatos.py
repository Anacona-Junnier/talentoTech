import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "janacona",
    database = "testdb"
)

myCursor = mydb.cursor()

sentenciaSql = "UPDATE users SET name = 'Maria', email = 'maria@gmail.com', age = 28 WHERE idUser = 1"
myCursor.execute(sentenciaSql)

mydb.commit() #Por ser una BD transaccional necesita cerrar la sentencia cuando se trate de insertar, actualizar y eliminar
