import sqlite3

conn = sqlite3.connect('stadiums.db')
cursor = conn.cursor()

country = input('country')

cursor.execute("""SELECT * FROM stadiums
                  WHERE country LIKE ?
                  ORDER BY built_year
              """, (country, ))

print("The oldest stadium:", cursor.fetchone())

cursor.execute("""SELECT sum(capacity) as sum FROM stadiums
                  WHERE country LIKE ?
                  ORDER BY built_year
              """, (country, ))

print("Summary country capacity: ", cursor.fetchone()[0])