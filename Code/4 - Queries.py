import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "",
    passwd = "",
    database = "olympics"
)

cursor = db.cursor()




# Total amount of medals won by Italy
print('Total amount of medals won by Italy:')
cursor.execute('SELECT (Golds + Silvers + Bronzes) FROM NOCs WHERE Name = "Italy"')
print(cursor.fetchall())
print('')








# All events of the Athletics discipline
print('All events of the Athletics discipline:')
cursor.execute('SELECT distinct Event FROM Teams WHERE Discipline = "Athletics"')
events = cursor.fetchall()
for event in events: print(event)
print('')

# Number of events of the Athletics discipline
print('Number of events of the Athletics discipline:')
cursor.execute('SELECT COUNT(*) FROM (SELECT Distinct Event FROM Teams WHERE Discipline = "Athletics") AS Disciplines')
print(cursor.fetchall())
print('')








# All teams competing in Beach Volleyball, ordered by NOC
print('All teams competing in Beach Volleyball, ordered by NOC:')
cursor.execute('SELECT Name, NOC FROM Teams WHERE Discipline = "Beach Volleyball" ORDER BY NOC')
teams = cursor.fetchall()
for team in teams: print(team)
print('')

# Number of Beach Volleyball teams for each NOC
print('Number of Beach Volleyball teams for each NOC:')
cursor.execute('SELECT NOC, COUNT(Name) as c FROM Teams WHERE Discipline = "Beach Volleyball" GROUP BY NOC ORDER BY c DESC')
NOCs = cursor.fetchall()
for NOC in NOCs: print(NOC)
print('')








# Disciplines with "Men" events and their respective male competitors
print('Disciplines with "Men" events and their respective male competitors:')
cursor.execute('SELECT Disciplines.Name, Disciplines.Males FROM (SELECT distinct Discipline FROM Teams WHERE Event LIKE "%Men%") as d INNER JOIN Disciplines ON d.Discipline = Disciplines.Name ORDER BY Disciplines.Males DESC')
disciplines = cursor.fetchall()
for discipline in disciplines: print(discipline)
print('')

# Disciplines with less than 100 male competitors among those with a "Men" event
print('Disciplines with less than 100 male competitors among those with a "Men" event:')
cursor.execute('SELECT t.Name, t.Males FROM (SELECT Disciplines.Name, Disciplines.Males FROM (SELECT distinct Discipline FROM Teams WHERE Event LIKE "%Men%") as d INNER JOIN Disciplines ON d.Discipline = Disciplines.Name) as t WHERE t.Males < 100 ORDER BY t.Males')
disciplines = cursor.fetchall()
for discipline in disciplines: print(discipline)
print('')

# Discipline with fewest male competitors among those with a "Men" event
print('Discipline with fewest male competitors among those with a "Men" event:')
cursor.execute('SELECT t.Name, t.Males FROM (SELECT Disciplines.Name, Disciplines.Males FROM (SELECT distinct Discipline FROM Teams WHERE Event LIKE "%Men%") as d INNER JOIN Disciplines ON d.Discipline = Disciplines.Name) as t WHERE t.Males = (SELECT MIN(j.Males) FROM(SELECT Disciplines.Name, Disciplines.Males FROM (SELECT distinct Discipline FROM Teams WHERE Event LIKE "%Men%") as d INNER JOIN Disciplines ON d.Discipline = Disciplines.Name) as j)')
print(cursor.fetchall())
print('')








# Number of coaches per NOC
print('Number of coaches per NOC:')
cursor.execute('SELECT NOC, COUNT(Coach) FROM Teams GROUP BY NOC ORDER BY COUNT(Coach) DESC')
NOCs = cursor.fetchall()
for NOC in NOCs: print(NOC)
print('')

# NOCs with more than 5 coaches
print('NOCs with more than 5 coaches:')
cursor.execute('SELECT NOC FROM Teams GROUP BY NOC HAVING COUNT(Coach)>5 ORDER BY COUNT(Coach) DESC')
NOCs = cursor.fetchall()
for NOC in NOCs: print(NOC)
print('')

# NOCs, number of golds won, number of coaches
print('NOCs, number of golds won, number of coaches:')
cursor.execute('SELECT NOCs.Name, NOCs.Golds, gt0.c FROM (SELECT NOC, COUNT(Coach) as c FROM Teams GROUP BY NOC HAVING c>0) as gt0 JOIN NOCs ON gt0.NOC = NOCs.Name GROUP BY NOCs.Name ORDER BY NOCs.Golds DESC')
NOCs = cursor.fetchall()
for NOC in NOCs: print(NOC)
print('')

# NOCs, total number of medals won, number of coaches
print('NOCs, total number of medals won, number of coaches:')
cursor.execute('SELECT NOCs.Name, (NOCs.Golds + NOCs.Silvers + NOCs.Bronzes) as Total, gt0.c FROM (SELECT NOC, COUNT(Coach) as c FROM Teams GROUP BY NOC HAVING c>0) as gt0 JOIN NOCs ON gt0.NOC = NOCs.Name GROUP BY NOCs.Name ORDER BY Total DESC')
NOCs = cursor.fetchall()
for NOC in NOCs: print(NOC)
print('')