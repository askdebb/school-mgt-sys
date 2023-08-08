import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'csKT3ch@1'
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE schMgtSys_Test")

print("All Done! Solid!")