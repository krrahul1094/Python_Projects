from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # change if different
        password="12345",
        database="flaskdb"
    )

# READ
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template("index.html", users=users)
#Rahul
@app.route('/rahul')
def Raj():
    return 'Hello World'
#Kumar
@app.route('/rahul/kumar')
def full():
    return 'Rahul is not a cheater'
# CREATE
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()
    conn.close()
    return redirect('/')

# DELETE
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# if __name__ == '__main__':
app.run(debug=True)
