import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "",
    passwd = "",
    database = "olympics"
)

cursor = db.cursor()




# Creation of table NOCs
cursor.execute("CREATE TABLE NOCs (Name VARCHAR(150) NOT NULL PRIMARY KEY, Golds INT(4), Silvers INT(4), Bronzes INT(4))")
db.commit()
# Check that NOCs was created correctly
cursor.execute("DESC NOCs")
print(cursor.fetchall(), end='\n\n\n')




# Creation of table Disciplines
cursor.execute("CREATE TABLE Disciplines (Name VARCHAR(150) NOT NULL PRIMARY KEY, Females INT(5), Males INT(5))")
db.commit()
# Check that Disciplines was created correctly
cursor.execute("DESC Disciplines")
print(cursor.fetchall(), end='\n\n\n')




# Creation of table Teams
cursor.execute("CREATE TABLE Teams (Name VARCHAR(150) NOT NULL, NOC VARCHAR(150), Discipline VARCHAR(150) NOT NULL, Event VARCHAR(150) NOT NULL, Coach VARCHAR(200), FOREIGN KEY (NOC) REFERENCES NOCs(Name) ON DELETE CASCADE, FOREIGN KEY (Discipline) REFERENCES Disciplines(Name) ON DELETE CASCADE, PRIMARY KEY (Name, Discipline, Event))")
db.commit()
# Check that Teams was created correctly
cursor.execute("DESC Teams")
print(cursor.fetchall(), end='\n\n\n')



# Creation of table Athletes
cursor.execute("CREATE TABLE Athletes (Full_Name VARCHAR(200) NOT NULL PRIMARY KEY, NOC VARCHAR(150) NOT NULL, Discipline VARCHAR(150) NOT NULL, FOREIGN KEY (NOC) REFERENCES NOCs(Name) ON DELETE CASCADE, FOREIGN KEY (Discipline) REFERENCES Disciplines(Name) ON DELETE CASCADE)")
db.commit()
# Check that Athletes was created correctly
cursor.execute("DESC Athletes")
print(cursor.fetchall(), end='\n\n\n')




# Check that all tables have been created
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
for table in tables: print(table)
print('')