import mysql.connector as mysql
import csv    # the "csv" module was used to deal with values containing a comma, which would make a simple ".split(',')" method not work (for instance, the string "Hong Kong, China" should have been considered as 1 value)

db = mysql.connect(
    host = "localhost",
    user = "",
    passwd = "",
    database = "olympics"
)

cursor = db.cursor()




# EntriesGender.csv --> Disciplines table

with open('../Data/csv/EntriesGender.csv', 'r', encoding='ISO-8859-1') as f:
    file = csv.reader(f)
    next(file)
        
    for line in file:
        cursor.execute("INSERT INTO Disciplines VALUES (%s, %s, %s)", (line[0], line[1], line[2]))
        db.commit()
   



# Medals.csv --> NOCs table

with open('../Data/csv/Medals.csv', 'r', encoding='ISO-8859-1') as f:
    file = csv.reader(f)
    next(file)
    
    NOC = []    # this list of all NOCs will be used in the next insertion (lines 46-68) to deal with NOCs missing from "Medals" file but present in the "Teams" file
        
    for line in file:
        NOC.append(line[1])
        
        cursor.execute("INSERT INTO NOCs VALUES (%s, %s, %s, %s)", (line[1], line[2], line[3], line[4]))
        db.commit()
        



# Athletes.csv --> Athletes table

with open('../Data/csv/Athletes.csv', 'r', encoding='ISO-8859-1') as f:
    file = csv.reader(f)
    next(file)
    
    Full_name = []    # this list will be used in lines 62-68 to deal with repeating names of athletes
        
    for line in file:
        
        if line[1] not in NOC:    # this 'if' statement makes use of the NOC list created earlier, as explained in the comment at line 35
            NOC.append(line[1])    # here I am using the list created earlier (line 35)
            
            cursor.execute("INSERT INTO NOCs VALUES (%s, %s, %s, %s)", ( line[1], str(0), str(0), str(0) ))
            db.commit()
        
        if line[0] in Full_name:    # this 'if' statement makes use of the Full_name list created earlier, as explained in the comment at line 52
            continue
        
        cursor.execute("INSERT INTO Athletes VALUES (%s, %s, %s)", (line[0], line[1], line[2]))
        db.commit()
        
        Full_name.append(line[0])




# Teams.csv --> Teams table, columns 1-4

with open('../Data/csv/Teams.csv', 'r', encoding='ISO-8859-1') as f:
    file = csv.reader(f)
    next(file)
            
    for line in file:
        cursor.execute("INSERT INTO Teams (Name, NOC, Discipline, Event) VALUES (%s, %s, %s, %s)", (line[0], line[2], line[1], line[3]))
        db.commit()




# Coaches.csv --> Teams table, column 5

with open('../Data/csv/Coaches.csv', 'r', encoding='ISO-8859-1') as f:
    file = csv.reader(f)
    next(file)
        
    for line in file:
        
        # this "if" statement deals with coaches with "NULL" event, for which we use as the event the same as the discipline ("line[2]" instead of "line[3]")
        if line[3] == '':
            cursor.execute("UPDATE Teams SET Coach = (%s) WHERE NOC = (%s) AND Discipline = (%s) AND Event = (%s)", (line[0], line[1], line[2], line[2]))
            db.commit()
            
        else:
            cursor.execute("UPDATE Teams SET Coach = (%s) WHERE NOC = (%s) AND Discipline = (%s) AND Event = (%s)", (line[0], line[1], line[2], line[3]))
            db.commit()