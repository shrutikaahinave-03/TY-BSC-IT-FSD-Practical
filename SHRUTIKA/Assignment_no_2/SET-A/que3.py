from flask import Flask, request
 app=Flask(__name__)

 @app.route("/", methods=["GET","POST"])
 def home():
     if request.method == "POST":
         a=float(request.form["a"])
         b=float(request.form["b"])
         return f"Product = {a*b}"
    
     return """ 
        <form method='POST'> 
         A:<input name='a'><br><br> 
        B:<input name='b'><br><br> 
         <input type='submit'>
         </form>
      """

 if __name__ == "__main__": 
     app.run(debug=True)
    