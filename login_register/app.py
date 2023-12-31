from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors as c
import os, re
from dotenv import load_dotenv
from waitress import serve

load_dotenv() 

app = Flask(__name__)

secret_key = os.urandom(24).hex()
app.secret_key = secret_key

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USERNAME')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

@app.route('/register', methods = ['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor(c.DictCursor)
        cursor.execute("SELECT * FROM accounts where username = % s and password = % s" , (username , password))
        account = cursor.fetchone()

        if account:
            msg = 'Account Already Exists !'
        elif not username or not password or not email:
            msg = 'Please fill out the fields...'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must start with a character !'
        elif not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&+=!]).{10}$', password):
            msg = 'Password must be 10 characters long having a capital letter, a special character & a number !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email))
            mysql.connection.commit()
            msg = 'You have Successfully Registered !'
    elif request.method == 'POST':
            msg = 'Please fill out the form !'

    return render_template('register.html', msg = msg)

@app.route('/')
@app.route('/login', methods = ['GET','POST'])
def login():        
    msg =''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(c.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return render_template('login.html')

if __name__ == '__main__':
    serve(app , host="0.0.0.0", port=8000)