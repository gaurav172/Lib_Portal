import sqlite3

def getallpending(id):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("SELECT * FROM REQUESTS WHERE (STATUS='APPROVED' OR STATUS='OVERDUE') AND USERID=?",(id,))
		data=c.fetchall()
		return data

def r_book(id):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		# c.execute("SELECT TME FROM REQUESTS WHERE ID=?",(id,))
		# data=c.fetchone()
		# p=(time.time()-data[0])*(0.001)
		c.execute("UPDATE REQUESTS SET STATUS='RETURNED'  WHERE ID=?",(id,))
		return

def getdata():
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("SELECT USERID FROM REQUESTS WHERE (STATUS='APPROVED' OR STATUS='OVERDUE')")
		data=c.fetchall()
		c.execute("SELECT NAME FROM REQUESTS WHERE (STATUS='APPROVED' OR STATUS='OVERDUE')")
		book=c.fetchall()
	val=[]
	i=0;
	for item in data:
		x=[]
		x.append(item[0])
		with sqlite3.connect('test.db') as conn:
			c=conn.cursor()
			c.execute("SELECT USERNAME FROM USER WHERE ID=?",(item[0],))
			x.append(c.fetchone()[0])
			x.append(book[i][0])
			val.append(x)
	return val

def update(uname,p1):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("UPDATE USER SET PASSWORD=? WHERE USERNAME=?",(p1,uname,))
		conn.commit()

def checkdues(idx):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("SELECT * FROM REQUESTS WHERE USERID=? AND (STATUS='OVERDUE')",(idx,))
		data=c.fetchall()
		return data

def submission(idx):
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("SELECT * FROM REQUESTS WHERE ID=?",(idx,))
		data=c.fetchone()
		return data