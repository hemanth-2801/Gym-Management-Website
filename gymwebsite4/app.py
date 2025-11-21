# from flask import Flask, render_template, request
from flask import *
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as sql

app = Flask(__name__)
app.secret_key = "abc"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:kannu100surya@localhost/gym"

db = SQLAlchemy(app)
class Joinus(db.Model):       #joinus is a table name, db.model is keyword
    name = db.Column(db.String(30))
    age = db.Column(db.Integer, unique=False, nullable=True)
    phone_number = db.Column(db.String(100), unique=False, nullable=True)
    email = db.Column(db.String(30), unique=False, nullable=False)
    gender = db.Column(db.String(30), unique=False, nullable=False)
    membership = db.Column(db.String(30), unique=False, nullable=False)

class Sign(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30), unique=False)

@app.route('/templates/join.html', methods =['GET','POST'])
def MemberInfo():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        phone_number = request.form.get('phone')
        email = request.form.get('email')
        gender = request.form.get('gender')
        membership = request.form.get('membership')
        entry = Joinus(name=name, age=age, phone_number=phone_number, email=email, gender=gender, membership=membership)
        db.session.add(entry)
        db.create_all()
        db.session.commit()
    return render_template("join.html")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/login.html', methods =['GET','POST'])
def login():
    error = None;
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('psw')
        con = sql.connect(host="localhost",user="root",password="kannu100surya",database="gym")
        mypassword_queue = []
        sql_query = "SELECT *FROM sign WHERE username ='%s' AND password ='%s'" % (username, password)
        mycursor = con.cursor()
        try:
            mycursor.execute(sql_query)
            myresults = mycursor.fetchall()
            for row in myresults:
                for x in row:
                      mypassword_queue.append(x)
        except Exception as e:
            print(e)
            print('error occured')
        if (username and password) in mypassword_queue:

            flash("you are successfuly logged in")
            return redirect(url_for('index'))
        else:
            error = "invalid password"
    return render_template('login.html', error=error)
    con.close()
@app.route('/templates/signup.html',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('psw')
        rpassword = request.form.get('psw-repeat')
        e = Sign(username=username, password=rpassword)       #sign = table name
        db.session.add(e)
        db.create_all()
        db.session.commit()
    return render_template('signup.html')
if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, render_template, request, redirect, flash
from flask import *
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as sql
from flask import *
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as sql


app = Flask(__name__)
app.secret_key = "abc"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:kannu100surya@localhost/gym"

db = SQLAlchemy(app)


class Joinus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer, unique=False, nullable=True)
    phone_number = db.Column(db.String(100), unique=False, nullable=True)
    email = db.Column(db.String(30), unique=False, nullable=True)
    gender = db.Column(db.String(30), unique=False, nullable=False)
    membership = db.Column(db.String(30), unique=False, nullable=False)


class Sign(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30), unique=False)


@app.route('/templates/join.html', methods=['GET', 'POST'])
def MemberInfo():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        phone_number = request.form.get('phone')
        email = request.form.get('email')
        gender = request.form.get('gender')
        membership = request.form.get('membership')
        entry = Joinus(name=name, age=age, phone_number=phone_number, email=email, gender=gender, membership=membership)
        db.session.add(entry)
        db.session.commit()
        flash("Member added successfully!")
    return render_template("join.html")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/templates/login.html', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('psw')
        con = sql.connect(host="localhost", user="root", password="RajRock_1643", database="gym")
        mypassword_queue = []
        sql_query = "SELECT * FROM sign WHERE username ='%s' AND password ='%s'" % (username, password)
        mycursor = con.cursor()
        try:
            mycursor.execute(sql_query)
            myresults = mycursor.fetchall()
            for row in myresults:
                for x in row:
                    mypassword_queue.append(x)
        except Exception as e:
            print(e)
            error = "An error occurred while trying to log in"
        con.close()
        if (username and password) in mypassword_queue:
            flash("You have successfully logged in!")
            return redirect(url_for('index'))
        else:
            error = "invalid password"
    return render_template('login.html', error=error)


@app.route('/templates/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('psw')
        rpassword = request.form.get('psw-repeat')
        e = Sign(username=username, password=rpassword)  # sign = table name
        db.session.add(e)
        db.create_all()
        db.session.commit()
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
