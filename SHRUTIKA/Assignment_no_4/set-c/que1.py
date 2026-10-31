from flask import Flask

app=Flask(__name__)

@app.route('/product/<int:product_id>')
def product(product_id):
    return f"Product Id:{product_id}<br>product Name:Sample product<br>price:Rs.600"

if __name__=="__main__":
    app.run(debug=True)