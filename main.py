from flask import Flask , render_template , request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length

app=Flask(__name__)

class LoginForm(FlaskForm):
	username=StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
	password=PasswordField('password',validators=[InputRequired(),Length(min=8,max=80)])

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login.html')
def show():
	return render_template("login.html")

@app.route('/signup.html')
def sho():
	return render_template("signup.html")

@app.route('/send', methods=['GET','POST'])
def send():
	if request.method == 'POST':
		first=request.form['first']
		last=request.form['Last']
		user=request.form['Username']
		p1=request.form['p1']
		email=request.form['Email']

		return render_template("disp.html",first=first,last=last,user=user,p1=p1,email=email)
	else:
		return render_template("indx.html")

@app.route('/sd', methods=['GET','POST'])
def sd():
	if request.method == 'POST':
		user=request.form['user']
		p1=request.form['p1']

		return render_template("log.html",user=user,p1=p1)
	else:
		return render_template("indx.html")

if __name__ == "__main__":
	app.run(debug=True)