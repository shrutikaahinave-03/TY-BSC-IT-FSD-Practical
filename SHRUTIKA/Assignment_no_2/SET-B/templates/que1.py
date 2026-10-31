from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/Login", methods=["POST"])
def login():
    username=request.form["username"]
    password=request.form["password"]

    return "Login Successfuli"


if __name__ == "__main__":
    app.run(debug=True)