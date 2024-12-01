import mysql.connector
# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(  host="localhost",  user="Python",  password="KOLSQL",  database="KOL")
# Cursor-Objekt erstellen
mycursor = mydb.cursor()
# SQL-Abfrage ausführen
mycursor.execute("SELECT * FROM inhalt")
# Ergebnisse abrufen
results = mycursor.fetchall()
# Ergebnisse ausgeben
for row in results:  print(row)
# Verbindung schließen
mydb.close()

input()