from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors as c
from waitress import serve

app = Flask(__name__ , static_folder='static')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'signinsignup'

mysql = MySQL(app)

@app.route('/')
@app.route('/login')
def login():        # function to return something for the routes
    # return 'Hello World !'
    return render_template('login.html')

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
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
            msg = 'Please fill out the form !'

    return render_template('register.html', msg = msg)

if __name__ == '__main__':
    serve(app , host="0.0.0.0", port=8000)