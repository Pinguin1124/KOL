import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='Python',
        password='KOLSQL',
        database='KOL'
    )
    print("Verbindung erfolgreich!")
except mysql.connector.Error as err:
    print(f"Fehler: {err}")