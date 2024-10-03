import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "janacona",
    database = "testdb"
)

myCursor = mydb.cursor()
myCursor.execute("CREATE TABLE users (idUser INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, email VARCHAR(60) NOT NULL, age INT NOT NULL)")