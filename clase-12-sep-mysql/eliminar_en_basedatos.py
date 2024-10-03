import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "janacona",
    database = "testdb"
)

myCursor = mydb.cursor()

sentenciaSql = "DELETE FROM users WHERE idUser = 5"
myCursor.execute(sentenciaSql)
mydb.commit()