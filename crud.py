from flask import Flask, render_template, request, redirect
import mysql.connector
from flask import jsonify

crud = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # change if different
        password="12345",
        database="rahuldb"
    )

#Read
@crud.route('/', methods=['GET'])
def get_emp():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emp")
    emp = cursor.fetchall()
    conn.close()

    return jsonify(emp)

#Read
@crud.route('/r', methods=['GET'])
def get_emp_indv():
    name = request.args.get('name') 
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emp where name = %s", (name,))
    emp = cursor.fetchall()
    conn.close()

    return jsonify(emp)

# CREATE
@crud.route('/add', methods=['POST'])
def add():
    name = request.args.get('name')
    age = request.args.get('age')
    id = request.args.get('id')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO emp (id, name, age) VALUES (%s, %s, %s)",
        (id, name, age,)
    )
    cursor.execute("SELECT * FROM emp")
    emp1 = cursor.fetchall()
    conn.commit()
    conn.close()
    return jsonify(emp1)

#Delete
@crud.route('/del', methods=['DELETE'])
def delete():
    id = request.args.get('name')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "Delete from emp where name = %s", (id,)
    )
    cursor.execute("SELECT * FROM emp")
    emp1 = cursor.fetchall()
    conn.commit()
    conn.close()
    return jsonify(emp1)

#Update
@crud.route('/update', methods=['PUT'])
def update():
    id = request.args.get('id')
    name = request.args.get('name')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "update emp set name = %s where id = %s", (name, id,)
    )
    cursor.execute("SELECT * FROM emp")
    emp1 = cursor.fetchall()
    conn.commit()
    conn.close()
    return jsonify(emp1)














# if __name__ == '__main__':
crud.run(debug=True)