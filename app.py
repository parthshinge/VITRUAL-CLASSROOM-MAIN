from flask import Flask, render_template, request, redirect, url_for, flash, session
import boto3
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "__YOUR_SECRET_KEY__"
app.permanent_session_lifetime = timedelta(minutes=15)

# AWS S3 Config
S3_BUCKET = 'parthdypbucket'
S3_REGION = 'ap-south-1'
s3 = boto3.client('s3', region_name=S3_REGION)

# SQLite Database
DATABASE = 'database.db'


# Create Database Connectio
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create Users Table Automatically
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


create_table()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()

            flash('Registration successful!', 'success')

            return redirect(url_for('login'))

        except sqlite3.IntegrityError:
            flash('Username already exists!', 'danger')

        finally:
            conn.close()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user['password'], password):

            session['username'] = username

            flash('Login successful!', 'success')

            return redirect(url_for('content'))

        else:
            flash('Invalid credentials!', 'danger')

    return render_template('login.html')


@app.route('/content')
def content():

    if 'username' not in session:
        flash('Please log in first!', 'warning')
        return redirect(url_for('login'))

    courses = []

    try:

        response = s3.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix='s3/'
        )

        print("FULL RESPONSE = ", response)

        files = response.get('Contents', [])

        print("FILES = ", files)

        for file in files:

            key = file['Key']

            print("KEY = ", key)

            if key.endswith('/'):
                continue

            filename = key.split('/')[-1]

            print("FILENAME = ", filename)

            title = filename.replace('.pdf', '')

            pdf_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{key}"

            print("TITLE = ", title)
            print("PDF URL = ", pdf_url)

            courses.append({

                "title": title,

                "pdf": pdf_url

            })

        print("COURSES = ", courses)

    except Exception as e:

        print("ERROR = ", e)

        flash(f"Error fetching courses: {str(e)}", 'danger')

    return render_template(
        'content.html',
        courses=courses
    )


@app.route('/logout')
def logout():

    session.clear()

    flash('You have been logged out!', 'info')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)