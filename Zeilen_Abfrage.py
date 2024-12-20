import mysql.connector

# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
  host="localhost",
  user="Python",
  password="KOLSQL",
  database="kol" 
)

mycursor = mydb.cursor()

# Wert für LIMIT während der Laufzeit eingeben
limit_value = int(input("Bitte gib deine ID ein: "))

# SQL-Abfrage mit LIMIT-Variable ausführen
query = "SELECT * FROM inhalt LIMIT %s"
mycursor.execute(query, (limit_value,))

# Ergebnis abrufen
myresult = mycursor.fetchall()

for row in myresult:
    print(row)

print("Der letzte Wert entspricht der Bindungsenergie!")

input("Zum Beenden Enter drücken!")
