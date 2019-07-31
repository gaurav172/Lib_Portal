import sqlite3

def request_book(bookid,userid):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("SELECT NAME FROM BOOKS WHERE ID=?",(bookid,))
		book=c.fetchall()
		c.close()

	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute('''INSERT INTO REQUESTS(BOOKID,USERID,NAME,STATUS) VALUES(?,?,?,?)''',(int(bookid),int(userid),book[0][0],"APPROVAL REQUIRED",))
		conn.commit()

	conn.close()
