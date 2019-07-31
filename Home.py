import sqlite3
from flask import render_template

def ShowHome(user):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		if user.type != "admin":
			c.execute("SELECT * FROM REQUESTS WHERE USERID=?",(user.id,))
		else:
			c.execute("SELECT * FROM REQUESTS")
		data=c.fetchall()
	with sqlite3.connect('test.db') as conn:
			c=conn.cursor()
			c.execute("SELECT * FROM BOOKS ORDER BY RATING DESC")
			topr=c.fetchall()
	return render_template("Dashboard.html",usr=user,data=data,length=len(data),topr=topr)