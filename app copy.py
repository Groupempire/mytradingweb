from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth
import mysql.connector

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
    "admin": "password"
}

db = mysql.connector.connect(
    host='sql12.freesqldatabase.com',
    user='sql12624615',
    password='1HzdZwzDI7',
    database='sql12624615'
)

print(mysql.connector.__version__)
print("xxx")
print(mysql.connector.__version__)

@app.route('/aboutus')
def aboutus():
    return render_template('cryptoo.html')

@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]:
        return username

@auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None

@auth.error_handler
def unauthorized():
    return "Unauthorized Access"

@app.route('/admin', methods=['GET', 'POST'])
@auth.login_required
def admin():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO solution (name, number) VALUES (%s, %s)", (name, number))
        db.commit()
        cursor.close()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM solution")
    data = cursor.fetchall()
    cursor.close()
    return render_template('admin.html', data=data)

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def home():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO solution (name, number) VALUES (%s, %s)", (name, number))
        db.commit()
        cursor.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
