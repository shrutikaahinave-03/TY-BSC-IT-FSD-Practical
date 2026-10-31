from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Name: Shrutika Ahinave,Roll Number: 05"

if __name__== '__main__':
    app.run(debug=True)