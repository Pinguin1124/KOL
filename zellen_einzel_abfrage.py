import mysql.connector

def get_cell_from_mysql(db_config, query):
    # Verbindung zur Datenbank herstellen
    connection = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
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
    'host': 'dein_host',
    'user': 'dein_benutzername',
    'password': 'dein_passwort',
    'database': 'deine_datenbank'
}

# SQL-Abfrage für die gewünschte Zelle
query = "SELECT deine_spalte FROM deine_tabelle WHERE deine_bedingung LIMIT 1"

# Abfrage ausführen und Ergebnis ausgeben
cell_value = get_cell_from_mysql(db_config, query)
print(f'Der Wert der Zelle ist: {cell_value}')
