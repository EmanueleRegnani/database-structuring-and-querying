import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "",
    passwd = ""
)

cursor = db.cursor()

# Creation the database
cursor.execute("CREATE DATABASE olympics")

# Check that it has been created
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
for database in databases: print(database)
