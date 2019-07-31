import sqlite3
def Add(name,author,genre):
	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		c.execute('''INSERT INTO BOOKS(NAME,AUTHOR,GENRE,RATING,NUM)VALUES(?,?,?,?,?)''',(name,author,genre,0,0))
		conn.commit()
	conn.close()