import sqlite3
from flask import render_template

def search(key,value,per):
	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		if key == "NAME":
			# value=" "+value+" "
			sql="""SELECT * FROM BOOKS WHERE NAME LIKE "%{p}%";"""
			sql=sql.format(p=value)
			c.execute(sql)
			# c.execute("SELECT * FROM BOOKS WHERE NAME = ?")
		if key == "AUTHOR":
			sql="""SELECT * FROM BOOKS WHERE AUTHOR LIKE "%{p}%";"""
			sql=sql.format(p=value)
			c.execute(sql)
		if key == "GENRE":
			sql="""SELECT * FROM BOOKS WHERE GENRE LIKE "%{p}%";"""
			sql=sql.format(p=value)
			c.execute(sql)
		data=c.fetchall()
		if len(data) == 0:
			return "<h1>No books were found</h1>"
		else:
			return render_template("books.html",data=data,usr=per)