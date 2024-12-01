import mysql.connector
from mysql.connector import Error

def test_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Python",
            password="KOLSQL"
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Erfolgreich verbunden. MySQL Version: {db_info}")
            return True
    except Error as e:
        print(f"Fehler: {e}")
        return False
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

test_connection()