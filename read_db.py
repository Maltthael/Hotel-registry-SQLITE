import sqlite3

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

cursor.execute(
    """
        SELECT * FROM usuarios
    """   
    
) 

conn.commit()

usuarios = cursor.fetchall()

for usuarios in usuarios:
    print(usuarios)
    
conn.close()
