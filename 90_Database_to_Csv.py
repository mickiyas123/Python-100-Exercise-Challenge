# Please download the database file database.db. and use python to access the database table rows that have an area of 2,000,000 or greater.Then export those those to a CSV fle

import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >=2000000")
rows = cur.fetchall()
conn.close()
# print(rows)

df = pd.DataFrame.from_records(rows)
df.columns = ['Rank','Country','Area','Population']
df.to_csv("countries_big_area.csv",index=False)