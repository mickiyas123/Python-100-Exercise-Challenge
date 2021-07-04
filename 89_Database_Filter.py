# Please download the database file database.db. The file contains a table with 50 country names along with their area in square km and population.
# please use python to print out the countries that have an area of greater than 2,00,000

import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT  country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

for i in rows:
    print(i[0])
