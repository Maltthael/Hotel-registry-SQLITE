import sqlite3

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

cursor.execute(
    """
        UPDATE usuarios SET nome = ? WHERE \
        id = ?
        
    """,
)
