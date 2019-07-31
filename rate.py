import sqlite3
from flask import redirect,url_for

def Rate_book(x,y):
	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		c.execute("SELECT RATING FROM BOOKS WHERE ID=?",(x,))
		old_rating=c.fetchall()
		c=conn.cursor()
		c.execute("SELECT NUM FROM BOOKS WHERE ID=?",(x,))
		num=c.fetchall()

	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		if float(y)>5:
			y=5
		p=((float(old_rating[0][0])*float(num[0][0])+float(y))/float(num[0][0]+1))
		p=round(p,1)
		c.execute("UPDATE BOOKS SET RATING=?,NUM=? WHERE ID=?",(p,num[0][0]+1,x),)
		return redirect(url_for('b1'))