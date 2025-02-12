from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration (update with your credentials)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your-password'
app.config['MYSQL_DB'] = 'sqli_ctf'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")  # Loads index.html

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = mysql.connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    cursor.close()

    if user:
        return "Login successful! But did you try SQL Injection? 😉"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)

