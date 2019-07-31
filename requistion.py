import sqlite3

def getbook(name,author,genre,userid):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute(''' INSERT INTO BOOKRE(NAME,AUTHOR,GENRE,USERID) VALUES(?,?,?,?) ''',(name,author,genre,userid) )
		conn.commit()