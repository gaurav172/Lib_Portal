import sqlite3

conn=sqlite3.connect('test.db')

c=conn.cursor()
c.execute("CREATE TABLE USER(\
ID INTEGER PRIMARY KEY AUTOINCREMENT,\
FIRSTNAME TEXT,\
LASTNAME TEXT,\
USERNAME TEXT,\
PASSWORD TEXT,\
EMAIL TEXT,\
TYPE TEXT\
)")
conn.commit()
conn.close()