from flask import Flask, render_template, request, redirect, session
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "myproject123"

# Database Connection
def connect():
    return psycopg2.connect(
        database="fsd_project",
        user="postgres",
        password="shruti",
        host="localhost",
        port="5432"
    )

# Create Table
def create_table():
    con = connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

    con.commit()
    cur.close()
    con.close()


# Home Page
@app.route("/")
def home():
    return redirect("/login")


# Registration Page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        if not name or not email or not password:
            return "All fields are required"

        if len(password) < 6:
            return "Password must be at least 6 characters"

        con = connect()
        cur = con.cursor()

        try:
            cur.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, generate_password_hash(password))
            )
            con.commit()
            return redirect("/login")

        except psycopg2.IntegrityError:
            con.rollback()
            return "Email already registered"

        finally:
            cur.close()
            con.close()

    return render_template("register.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"].strip()
        password = request.form["password"]

        con = connect()
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,)
        )

        user = cur.fetchone()

        cur.close()
        con.close()

        if user and check_password_hash(user[3], password):
            session["name"] = user[1]
            return redirect("/dashboard")

        return "Invalid Email or Password"

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():

    if "name" in session:
        return render_template(
            "dashboard.html",
            name=session["name"]
        )

    return redirect("/login")


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    create_table()
    app.run(debug=True)