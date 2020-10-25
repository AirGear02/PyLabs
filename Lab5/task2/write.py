import sqlite3

conn = sqlite3.connect('stadiums.db')
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE stadiums
#                   (name text, city text, country text, 
#                   capacity int, built_year int)
#                """)

name = input('name: ')
city = input('city: ')
country  = input('country: ')
capacity = input('capacity: ')
built_date = input('built_date: ')

cursor.execute('INSERT INTO stadiums VALUES (?, ?, ?, ?, ?)', 
    (name, city, country, capacity, built_date))

conn.commit()

