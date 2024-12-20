import mysql.connector

# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
  host="localhost",  # Ersetze durch deinen Hostnamen
  user="Python",  # Ersetze durch deinen Benutzernamen
  password="KOLSQL",  # Ersetze durch dein Passwort
  database="kol"  # Ersetze durch den Namen deiner Datenbank
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
