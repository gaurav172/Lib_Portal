import sqlite3
import time

def checkdues(idp):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		x=int(time.time())
		c.execute("SELECT ID FROM REQUESTS WHERE USERID=? AND TME<= AND STATUS='APPROVED'",(idp,x-1000,))
