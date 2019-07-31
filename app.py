from flask import Flask , render_template , request,redirect,url_for
import sqlite3
from addbook import *
from requestsbook import *
from Home import *
from appr import *
from searching import *
from signup import *
from rate import *
from getstatus import *
import random
from send import *
from flask_mail import Mail, Message
from requistion import *

app=Flask(__name__)

# print(2)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'libport17@gmail.com'
app.config['MAIL_PASSWORD'] = 'lib_port'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# print(time.time())

Rating_Flag=[[0 for i in range(1000)] for j in range(1000)]
conn=sqlite3.connect('test.db')

c=conn.cursor()
uname=""
class stud():
	pass

per=stud()
per.id=0

login=False
user="check"
@app.route('/')
def index():
	if login == True:
		return redirect(url_for('disp'))
	return render_template("index.html")

@app.route('/login.html')
def show():
	if login == True:
		return redirect(url_for('disp'))
	else:
		return render_template("login.html")
y=0

@app.route('/update',methods=['GET','POST'])
def upd():
	if login == True:
		x=request.form['id']
		y=request.form['rate']
		if Rating_Flag[per.id][int(x)]==0:
			Rating_Flag[per.id][int(x)]=1
			return Rate_book(x,y)
		return redirect(url_for('b1'))

	else:
		return redirect(url_for('index'))

@app.route('/books.html')
def b1():
	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		c.execute("SELECT * FROM BOOKS")
		data=c.fetchall()
	if login == True:
		return render_template("books.html",data=data,usr=per)
	else:
		return redirect(url_for('index'))

@app.route('/profile.html')
def prof():
	if login==False:
		return redirect(url_for('index'))

	with sqlite3.connect('test.db') as conn: 
		c=conn.cursor()
		c.execute("SELECT * FROM REQUESTS WHERE USERID=?",(per.id,))
		data=c.fetchall()
	return render_template("profile.html",usr=per,length=len(data))	

@app.route('/add',methods=['GET','POST'])
def b2():
	name=request.form['name']
	author=request.form['author']
	genre=request.form['genre']
	Add(name,author,genre)
	return redirect(url_for('b1'))

@app.route('/signup.html')
def sho():
	return render_template("signup.html")

@app.route('/addbooks.html')
def ab():
	if login==False:
		return redirect(url_for('index'))
	return render_template("addbooks.html",usr=per)

@app.route('/Dashboard')
def disp():
	if login == False:
		return redirect(url_for('index'))
	else:
		return ShowHome(per)

@app.route('/books',methods=['GET','POST'])
def bk():
	if login == True:
		if request.method == 'POST':
			key=request.form['category']
			value=request.form['search']
			return search(key,value,per)
	else:
		return redirect(url_for('index'))		

@app.route('/logout',methods=['GET','POST'])
def act():
	if request.method == 'POST':
		global login
		login=False
		return redirect(url_for('index'))

@app.route('/send', methods=['GET','POST'])
def send():
	if request.method == 'POST':
		per.first=request.form['first']
		per.last=request.form['Last']
		per.username=request.form['Username']
		per.p1=request.form['p1']
		per.p2=request.form['p2']
		per.type=request.form['type']
		per.email=request.form['Email']
		p=check(per)
		if p == 0:
			global y
			y=random.randint(1,1000000)
			with app.app_context():	
				msg = Message('Confirmation Email', sender = 'libport17@gmail.com', recipients = [per.email])
				msg.body ="Your otp for confirmation is "+str(y)
				mail.send(msg)
			return render_template("confirm.html")
		else:
			return p;

@app.route('/sd', methods=['GET','POST'])
def sd():
	if request.method == 'POST':
		global user
		user=request.form['name']
		p1=request.form['p1']
		with sqlite3.connect('test.db') as conn:
			c=conn.cursor()
			rst=None
			c.execute("SELECT * FROM USER WHERE USERNAME=?",(user,))
			rst=c.fetchall()			
			for row in rst:
				if row[4]==p1:
					global login
					login=True
					per.id=row[0]
					per.first=row[1]
					per.last=row[2]
					per.username=row[3]
					per.email=row[5]
					per.type=row[6]
					return redirect(url_for('disp'))
	
				else:
					return "<h1>INVALID USERNAME OR PASSWORD</h1>"
			return "<h1>INVALID USERNAME OR PASSWORD</h1>"

@app.route('/confirm',methods=['GET','POST'])
def con():
	x=request.form['otp']
	if int(x)==y:
		global login
		login=True
		global per
		per=signup(per)
		return redirect(url_for('disp'))
	return "Incorrect Confirmation Key"	


@app.route('/issuereq.html')
def  ireq():
	if login==False:
		return redirect(url_for('index'))
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("SELECT * FROM REQUESTS")
		data=c.fetchall()
		return render_template("issuereq.html",data=data,usr=per,length=len(data))

@app.route('/req',methods=['GET','POST'])
def req():
	if request.method == 'POST':
		x=request.form['id']
		request_book(x,per.id)
		return ShowHome(per)

@app.route('/def.html')
def defa():
	if login==False:
		return redirect(url_for('index'))
	data=getdata()
	return render_template("def.html",data=data,usr=per,length=len(data))

@app.route('/approve',methods=['GET','POST'])
def approve():
	if login==False:
		return redirect(url_for('index'))
	reqid=request.form['requestid']
	ApproveRequest(reqid)
	return redirect(url_for('disp'))


@app.route('/issue_hist.html')
def issue():
	if login==False:
		return redirect(url_for('index'))
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		if per.type != "admin":
			c.execute("SELECT * FROM REQUESTS WHERE USERID=?",(per.id,))
		else:
			c.execute("SELECT * FROM REQUESTS")
		data=c.fetchall()
	return render_template("issue_hist.html",usr=per,data=data,length=len(data))

@app.route('/return_book.html')
def ret():
	if login==False:
		return redirect(url_for('index'))
	data=getallpending(per.id)
	return render_template("return_book.html",data=data,length=len(data),usr=per)

@app.route('/return',methods=['GET','POST'])
def retu():
	if request.method=='POST':
		x=request.form['reqid']
		r_book(x)
		data=submission(x)
		tp=(time.time()-data[7])*(0.001)
		tp=round(tp,1)
		Fine=0
		if(tp>=0):
			Fine=tp
		with app.app_context():
			msg = Message('Submission Info', sender = 'libport17@gmail.com', recipients = [per.email])
			msg.body ="Book Id : " +str(data[1])+"\n"+"Book Name: "+str(data[3])+"\n" +"Issued By : "+per.first+" "+per.last+"\n"+"Total Fine: "+str(Fine)+"\n"
			mail.send(msg)
		return "<h1>Book Successfully Returned</h1><br><br><h1>An email regarding submission is sent to your email id " +per.email
		return redirect(url_for('disp'))

@app.route('/forget.html')
def fg():
	return render_template("forget.html")

@app.route('/fget',methods=['GET','POST'])
def fget():
	global uname
	uname=request.form['username']
	email=request.form['email']
	x=Check_pwd(uname,email)
	if x!= 1 :
		return x

	global y
	y=random.randint(1,1000000)
	with app.app_context():
		msg = Message('Confirmation Email', sender = 'libport17@gmail.com', recipients = [email])
		msg.body ="Your otp for Password change is "+str(y)
		mail.send(msg)
	return render_template("change.html")


@app.route('/change',methods=['GET','POST'])
def a4():
	x=request.form['otp']
	if int(x)!=y:
		return "Wrong Key"
	else:
		return render_template("upd_pwd.html")

@app.route('/index.html')
def a6():
	return redirect(url_for('index'))

@app.route('/updpwd',methods=['GET','POST'])
def a5():
	p1=request.form['p1']
	p2=request.form['p2']
	if p1!=p2:
		return "Passwords do not match"
	else:
		update(uname,p1)
		return 'Your Password Has been Changed <a href="index.html"><h1>Login</h1></a>'

@app.route('/breq',methods=['GET','POST'])
def a8():
	name=request.form['name']
	author=request.form['author']
	genre=request.form['genre']
	getbook(name,author,genre,per.id)
	return redirect(url_for('disp'))

@app.route('/bookre.html')
def a10():
	if login==False:
		return redirect(url_for('index'))
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("SELECT * FROM BOOKRE")
		data=c.fetchall()
		return render_template("bookre.html",data=data,usr=per,length=len(data))



@app.route('/book_req.html')
def a7():
	if login==False:
		return redirect(url_for('index'))
	return render_template("book_req.html")

@app.route('/brek',methods=['GET','POST'] )
def a13():
	p=request.form['idx']
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("SELECT * FROM BOOKRE WHERE ID=?",(p,))
		data=c.fetchone()
		Add(data[1],data[2],data[3])
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		c.execute("DELETE FROM BOOKRE WHERE ID=?",(p,))
	return redirect(url_for('a10'))

@app.route('/dues.html')
def a14():
	if login==False:
		return redirect(url_for('index'))
	data=checkdues(per.id)
	val=[]
	for item in data:
		tp=item[7]-time.time()
		tp=-tp*(0.001)
		tp=round(tp,1)
		val.append(tp)
	return render_template("overdue.html",data=data,usr=per,val=val,x=0,len=len(data))


# @app.route('/dues')
# def a24():
# 	if login==False:
# 		return redirect(url_for('index'))
# 	return render_template("dues.html")
# 	return "<a href='duebook'><h1>Overdue Books</h1></a><a href='reciept' ><h1>Reciepts</h1></a>"

import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

def print_date_time():
	with sqlite3.connect('test.db') as conn:
		c=conn.cursor()
		p=int(time.time())
		c.execute("SELECT USERID,NAME FROM REQUESTS WHERE TME<=? AND STATUS='APPROVED'",(p-10,))
		data=c.fetchall()
		c=conn.cursor()
		c.execute("UPDATE REQUESTS SET STATUS='OVERDUE' WHERE TME<=? AND STATUS='APPROVED'",(p-10,))
		conn.commit()
		c=conn.cursor()
		# print(len(data))
		# print(time.time())
	for item in data:
		c=conn.cursor()
		c.execute("SELECT EMAIL FROM USER WHERE ID=?",(str(item[0]),))
		# print(item[0])
		with app.app_context():
			avc=c.fetchone()
			msg = Message('Reminder Email', sender = 'libport17@gmail.com', recipients = [avc[0]])
			msg.body ="Return Date of " + item[1]+" is due today"
			mail.send(msg)
		# print("username")
		# print(avc[0])
		# print(item[1])

			



scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=print_date_time,
    trigger=IntervalTrigger(seconds=5),
    id='printing_job',
    name='Print date and time every five seconds',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
	app.run(debug=True)
