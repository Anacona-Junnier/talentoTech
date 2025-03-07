import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "janacona",
    database = "testdb"
)

myCursor = mydb.cursor()

myCursor.execute("SELECT * FROM users")

# #consultar un solo registro
# resultado = myCursor.fetchone()
# print(resultado)

resultado = myCursor.fetchall()
for row in resultado:
    print(f"llave primaria: {row[0]} nombre: {row[1]} correo: {row[2]} edad: {row[3]}")
