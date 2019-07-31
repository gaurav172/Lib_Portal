import sqlite3

conn=sqlite3.connect('test.db')

c=conn.cursor()
c.execute("CREATE TABLE BOOKS(\
ID INTEGER PRIMARY KEY AUTOINCREMENT,\
NAME TEXT,\
AUTHOR TEXT,\
GENRE TEXT,\
RATING DECIMAL,\
NUM DECIMAL\
)")
conn.commit()
with sqlite3.connect('test.db') as conn: 
	c=conn.cursor()
	c.execute('''INSERT INTO BOOKS(NAME,AUTHOR,GENRE,RATING,NUM)VALUES(?,?,?,?,?)''',("Alchemist","Paulo Coelho","Life and Adventure",0,0))
	conn.commit()
conn.close()