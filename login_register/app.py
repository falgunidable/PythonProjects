from flask import Flask, render_template
from flask_mysqldb import MySQL
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

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    serve(app , host="0.0.0.0", port=8000)