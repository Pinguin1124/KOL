import mysql.connector

def get_cell_from_mysql(db_config, query):
    # Verbindung zur Datenbank herstellen
    connection = mysql.connector.connect(
        host=db_config['localhost'],
        user=db_config['Python'],
        password=db_config['KOLSQL'],
        database=db_config['inhalt']
    )

    cursor = connection.cursor()

    try:
        # SQL-Abfrage ausführen
        cursor.execute(query)
        result = cursor.fetchone()

        # Rückgabe der ersten Zelle des Ergebnisses
        return result[0] if result else None
    finally:
        cursor.close()
        connection.close()

# Konfigurationsdaten für die Verbindung
db_config = {
    'host': 'localhost',
    'user': 'Python',
    'password': 'KOSQL',
    'database': 'kol'
}

spalte = input()
bedingung = input()

# SQL-Abfrage für die gewünschte Zelle
query = "SELECT {spalte} FROM inhalt WHERE {bedingung} LIMIT 1"

# Abfrage ausführen und Ergebnis ausgeben
cell_value = get_cell_from_mysql(db_config, query)
print(f'Der Wert der Zelle ist: {cell_value}')
