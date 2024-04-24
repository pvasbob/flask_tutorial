from flask import Flask
app = Flask(__name__)



@app.route("/")
@app.route("/home")
@app.route("/root")
@app.route("/qunqun")
# we can have as many @app.** as we want, they all equal, and the function name defined below
# can be anything, not limited to the names shown above. 
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"




if __name__ == "__main__":
    app.run(debug=True)


