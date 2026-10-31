from flask import Flask, request
app = Flask(__name__)

@app.route('/Employee', methods=['GET', 'POST'])
def Employee():
    if request.method == "POST":
        emp_id = request.form.get("emp_id")
        name = request.form.get("name")
        age = request.form.get("age")
        department = request.form.get("department")

        return f"""
            <h2>Employee Details</h2>
            <p>
                EMP_ID: {emp_id}<br>
                Name: {name}<br>
                Age: {age}<br>
                Department: {department}
            </p>
        """

    return '''
        <h2>Employee Form</h2>
        <form method="POST">
            EMP_ID: <input type="number" name="emp_id" required><br><br>
            Name: <input type="text" name="name" required><br><br>
            Age: <input type="number" name="age" required><br><br>
            Department: <input type="text" name="department" required><br><br>
            <input type="submit" value="Add">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)