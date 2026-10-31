from flask import Flask , request, render_template
import psycopg2
app = Flask(__name__)
def get_connect():
    conn = psycopg2.connect(
       dbname = 'company',
       user = 'postgres',
       password = 'shruti',
       host = 'localhost',
       port = '5432'
    )
    return conn
def create_table():
    con = get_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            Employee_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Department VARCHAR(100)
        );
    """)
    con.commit()
    cur.close()
    con.close()

@app.route('/employee', methods=['GET','POST'])
def employee():

    con = get_connect()
    cur = con.cursor()

    if request.method == 'POST':

        Name = request.form.get("Name")
        Department = request.form.get("Department")

        cur.execute(
            "INSERT INTO Employee (Name,Department) VALUES(%s,%s)",
            ( Name, Department)
        )

        con.commit()

    cur.execute("SELECT * FROM Employee ORDER BY Employee_ID")
    Employee = cur.fetchall()

    cur.close()
    con.close()
    return render_template("index.html", Employee=Employee)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)