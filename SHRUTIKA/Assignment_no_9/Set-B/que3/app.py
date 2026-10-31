from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname="studentdb1",
        user="postgres",
        password="shruti",
        host="localhost",
        port="5432"
    )

def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Product (
            Product_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Price FLOAT,
            Quantity INT
        )
    """)

    con.commit()
    cur.close()
    con.close()

@app.route("/", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["Name"]
        price = request.form["Price"]
        quantity = request.form["Quantity"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO Product (Name, Price, Quantity) VALUES (%s, %s, %s)",
            (name, price, quantity)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/product")

    return render_template("add.html")

@app.route("/product")
def display_products():
    con = db_connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM Product ORDER BY Product_ID")
    products = cur.fetchall()

    cur.close()
    con.close()

    return render_template("product.html", products=products)

@app.route("/update", methods=["GET","POST"])
def update_product():

    if request.method == "POST":
        product_id = request.form["Product_ID"]
        quantity = request.form["Quantity"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "UPDATE Product SET Quantity = %s WHERE Product_ID = %s",
            (quantity, product_id)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/product")

    return render_template('update.html')

@app.route("/delete", methods=["GET","POST"])
def delete_product():

    if request.method == "POST":

        product_id = request.form["Product_ID"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "DELETE FROM Product WHERE Product_ID = %s",
            (product_id,)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/product")

    return render_template('delete.html')


if __name__ == "__main__":
    create_table()
    app.run(debug=True)