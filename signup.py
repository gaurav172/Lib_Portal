import sqlite3
from Home import *

def check(per):
	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		c.execute("SELECT * FROM USER WHERE USERNAME=?",(per.username,))
		rst=c.fetchall()
		if len(rst) > 0 :
			return "<h1>USERNAME ALREADY EXISTS !! TRY ANOTHER</h1>"
		c.execute("SELECT EMAIL FROM USER WHERE USERNAME=?",(per.username,))
		rst=c.fetchall()
		if len(rst) >0:
			return "<h1>Email Already Taken</h1>"
		if per.p1 != per.p2:
			return "<h1>Passwords Do Not Match</h1>"
	return 0

def signup(per):		
	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		c.execute('''INSERT INTO USER(FIRSTNAME,LASTNAME,USERNAME,PASSWORD,EMAIL,TYPE)VALUES(?,?,?,?,?,?)''',(per.first,per.last,per.username,per.p1,per.email,per.type))
		conn.commit()
	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		c.execute("SELECT ID FROM USER WHERE USERNAME =?",(per.username,))
		per.id=c.fetchone()[0]
		return per

def Check_pwd(uname,email):
	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		c.execute("SELECT EMAIL FROM USER WHERE USERNAME=?",(uname,))
		data=c.fetchone()
		if email != data[0]:
			return "No such Account Exists"
		return 1 