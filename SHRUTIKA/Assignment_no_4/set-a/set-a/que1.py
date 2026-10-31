from flask import Flask

app=Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to Home page"

@app.route('/about')
def about():
    return "This is the About page"

if __name__=="__main__":
    app.run(debug=True)