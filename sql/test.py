import sqlite3 

connection = sqlite3.connect('sql/chinook.db')
cursor = connection.cursor()

query = """
SELECT Title FROM albums
JOIN artists ON artists.ArtistId = albums.ArtistId
WHERE artists.Name LIKE ?"""
name = input("Name to look up: ")
params = ('%'+name+'%',)
print(query, params)

cursor.execute(query, params)
for row in cursor:
    print(row)

connection.commit()
connection.close()