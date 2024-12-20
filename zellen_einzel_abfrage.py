import mysql.connector

# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
  host="localhost",
  user="Python",
  password="KOLSQL",
  database="kol"
)

mycursor = mydb.cursor()

# Bedingung während der Laufzeit eingeben
yourcondition = input("Bitte gib deine ID ein: ")

# Beispiel für eine spezifische Zellenabfrage mit der Bedingung
query = f"SELECT Masse_des_gesamten_Kernes FROM inhalt WHERE {yourcondition}"

mycursor.execute(query)

# Ergebnis abrufen
myresult = mycursor.fetchone()

# Ausgabe der abgerufenen Zelle
print(myresult[0]) if myresult else print("Keine Daten gefunden")

input("Zum Beenden Enter drücken!")
