import sqlite3

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

cursor.execute(
    
    """
        INSERT INTO usuarios(nome, email)
        VALUES (?, ?)
    """,
    ("Gina", "Gina@gmail.com"),
     
)

conn.commit()
conn.close()