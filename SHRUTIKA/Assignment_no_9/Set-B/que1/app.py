from flask import Flask , request, render_template, redirect
import psycopg2

app = Flask(__name__)

def db_conncet():
    return psycopg2.connect(
        dbname = 'library',
        user = 'postgres',
        password = 'shruti',
        host = 'localhost',
        port = '5432'
    )
def create_table():
    con = db_conncet()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Book (
            Book_ID SERIAL PRIMARY KEY,
            Titl VARCHAR(100),
            Author VARCHAR(100)'
            Price FLOAT
        );
    """)

    con.commit()
    cur.close()
    con.close()
@app.route('/', methods= ['GET','POST'])
def add_book():
    if request.method == 'POST':
        title= request.form.get('Title')
        author = request.form.get('Author')
        price = request.form.get('Price')

        con = db_connect()
        cur = con.Cursor

        cur.execute(
            "INSERT INTO Book(Title, Author, Price) VALUES(%s,%s)",(title, Author, Price)
        )
        con.commit()
        cur.close()
        con.close()
        return redirect("/")
    return render_template('add.html')
@app.route('/update', methods = ['GET','POST'])
def update_book():
    con = db_conncet()
    cur = con.cursor()
    if request.method == "POST":
        book_ID = request.form.get("Book_ID")
        price = request.form.get("Price")

        cur.execute(
            "UPDATE Book SET Course = %s WHERE Book_ID = %s",
            (Price, Book_ID)
        )
        con.commit()
    cur.execute("SELECT * FROM Book ORDER BY Book_ID")
    books = cur.fetchall()
    cur.close()
    con.close()
    return render_template('update.html', books=books)
if __name__ == '__main__':
    create_table()
    app.run(debug = True)