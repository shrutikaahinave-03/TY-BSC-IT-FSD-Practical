from flask import Flask

app=Flask(__name__)

@app.route('/contact')
def contact():
    return"Welcome To The Contact Page"

@app.route('/service')
def service():
    return"This page is about services which provided"

if __name__=="__main__":
    app.run(debug=True)