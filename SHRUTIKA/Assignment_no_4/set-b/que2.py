from flask import Flask

app=Flask(__name__)

@app.route('/square/<int:num>')
def square(num):
    return f"Number:{num}<br>square:{num*num}"

if __name__=="__main__":
    app.run(debug=True)