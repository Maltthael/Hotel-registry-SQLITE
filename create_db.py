import sqlite3

conn = sqlite3.connect('hotel.db')

cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email VARCHAR
        )
    """
    
)

conn.commit()
conn.close()