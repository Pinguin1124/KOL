import mysql.connector

# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
  host="localhost",
  user="Python",
  password="KOLSQL",
  database="kol" 
)

mycursor = mydb.cursor()

# Wert für die ID während der Laufzeit eingeben
row_number = int(input("Was ist die ID deines Elmentes? "))

# SQL-Abfrage mit LIMIT und OFFSET-Klausel, um eine bestimmte Zeile auszuwählen
query = "SELECT * FROM inhalt LIMIT 1 OFFSET %s"
mycursor.execute(query, (row_number - 1,))  # OFFSET beginnt bei 0

# Ergebnis abrufen
myresult = mycursor.fetchone()

if myresult:
    print(myresult)
else:
    print("Keine Zeile mit der angegebenen Nummer gefunden.")

print("Immer der letzte Wert ist die Bindungsenergie!")

input("Zum Beenden Enter drücken!")
