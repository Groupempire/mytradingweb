from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'marklift'
# app.config['MYSQL_HOST'] = 'sql202.byetcluster.com'
# app.config['MYSQL_USER'] = 'epiz_34114194'
# app.config['MYSQL_PASSWORD'] = '0m1ysysgQQ'
# app.config['MYSQL_DB'] = 'epiz_34114194_marklift'
# mysql = MySQL(app)



@app.route('/aboutus')
def aboutus():
    return render_template('cryptoo.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']

        db = mysql.connector.connect(
            host='sql202.byetcluster.com',
            user='epiz_34114194',
            password='0m1ysysgQQ',
            database='epiz_34114194_marklift'
        )

        cursor = db.cursor()
        cursor.execute("INSERT INTO solution (name, number) VALUES (%s, %s)", (name, number))
        db.commit()
        cursor.close()
        db.close()


# @app.route('/', methods=['GET', 'POST'])
# def home():
#    if request.method == 'POST':
#       name = request.form['name']
#       number = request.form['number']

#     #   cur = mysql.connection.cursor()
#     #   cur.execute("INSERT INTO solution (name,number) VALUES (%s, %s)", (name, number))
#     #   mysql.connection.commit()
#     #   cur.close()
#       cursor = db.cursor()
#       cursor.execute("INSERT INTO solution (name, number) VALUES (%s, %s)", (name, number))
#       db.commit()
#       cursor.close()   
   
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True,port=3306)






















# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def home():
#    return render_template('index.html')


# @app.route('/aboutus')
# def aboutus():
#     return render_template('cryptoo.html')






# if __name__ == '__main__':
#    app.run(debug=True,port=8000)
