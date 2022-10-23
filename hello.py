from flask import Flask, render_template, redirect, url_for
import requests
import sqlite3
import pandas as pd
app = Flask(__name__)


#database connection estabilishment
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


#landing page
@app.route("/")
def index():
    return render_template('index.html')

#list of countries page
@app.route("/students")
def students():
    #get db connection
    conn = get_db_connection()
    #get all countries in DB
    students = conn.execute('SELECT * FROM students').fetchall()
    #render template for list of countries, returning list of countries as param
    #return render_template('students.html', students=students)
    return render_template('students.html', students = students)
    conn.close()
    

@app.route("/student/<id>")
def student(id):
    conn = get_db_connection()
    #selecting all ports based on country given by param of function
    student = conn.execute('SELECT * FROM students WHERE id = ?', [id]).fetchall()
    return render_template("students.html", student=student)
    conn.close()

@app.route("/student/edit/<id>")
def student_edit(id):
    conn = get_db_connection()
    #selecting all ports based on country given by param of function
    student = conn.execute('SELECT * FROM students WHERE id = ?', [id]).fetchall()
    return render_template("student_edit.html", student=student)
    conn.close()

@app.route("/student/delete/<id>")
def student_delete(id):
    conn = get_db_connection()
    #selecting all ports based on country given by param of function
    student = conn.execute('DELETE FROM students WHERE id = ?', [id])
    conn.commit()
    print("Deleted student with id"+id)
    return render_template("index.html")
    conn.close()
