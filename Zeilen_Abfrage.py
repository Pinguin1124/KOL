import mysql.connector

# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
  host="localhost",  # Ersetze durch deinen Hostnamen
  user="yourusername",  # Ersetze durch deinen Benutzernamen
  password="yourpassword",  # Ersetze durch dein Passwort
  database="yourdatabase"  # Ersetze durch den Namen deiner Datenbank
)

mycursor = mydb.cursor()

# SQL-Abfrage ausführen
mycursor.execute("SELECT * FROM yourtable LIMIT 1")

# Ergebnis abrufen
myresult = mycursor.fetchone()

print(myresult)
