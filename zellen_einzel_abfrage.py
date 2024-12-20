import mysql.connector

def get_cell_from_mysql(db_config, query, params):
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
        cursor.execute(query, params)
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

spalte = 'Masse_des_Kernes'
bedingung = input("Gib die ID ein: ")

# SQL-Abfrage für die gewünschte Zelle
query = f"SELECT {spalte} FROM inhalt WHERE id = %s LIMIT 1"

# Abfrage ausführen und Ergebnis ausgeben
cell_value = get_cell_from_mysql(db_config, query, (bedingung,))
print(f'Der Wert der Zelle ist: {cell_value}')
