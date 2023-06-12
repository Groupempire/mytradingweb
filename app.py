from flask import Flask, render_template, request, session, redirect, url_for
from flask_httpauth import HTTPBasicAuth
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'
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


# ----------------------------
# Authentication and Routes
# ----------------------------

@app.route('/', methods=['GET', 'POST'])
def home():
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        gmails = request.form['gmails']

        cursor = db.cursor()
        cursor.execute("INSERT INTO solution (name, number, gmails) VALUES (%s, %s, %s)", (name, number, gmails))
        db.commit()
        cursor.close()

    return render_template('index.html')

@app.route('/indexs')
def aboutus():
    return render_template('index.html')



@app.route('/contactus')
def contactus():
    return render_template('contact.html')

@app.route('/aboutus')
def about():
    return render_template('about.html')

@app.route('/world')
def world():
    return render_template('world.html')

@app.route('/pricepc')
def pricepc():
    return render_template('pricepc.html')

@app.route('/viewmsg')
def viewmsg():
    return render_template('viewmsg.html')

@app.route('/cryptoo')
def cryptoo():
    return render_template('cryptoo.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('admin'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if verify_password(username, password):
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error=True)

    return render_template('login.html', error=False)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        gmails = request.form['gmails']

        cursor = db.cursor()
        cursor.execute("INSERT INTO solution (name, number, gmails) VALUES (%s, %s, %s)", (name, number, gmails))
        db.commit()
        cursor.close()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM solution")
    data = cursor.fetchall()
    cursor.close()
    return render_template('admin.html', data=data)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('home'))

# ----------------------------
# Authentication Functions
# ----------------------------

@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]:
        session['logged_in'] = True
        session['username'] = username
        return True
    return False

@auth.error_handler
def unauthorized():
    return "Unauthorized Access"

if __name__ == '__main__':
    app.run(debug=True)
